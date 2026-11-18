"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

"""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action["tool"]
    if tool not in ("issue_refund", "file_carrier_fault", "notify_carrier"):
        return Verdict.allow()

    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if tool == "notify_carrier":
        if policy is None:
            return Verdict.deny("Thiếu chính sách hiệu lực cho thông báo gửi hãng")
        payload = action["payload"]
        allowed_fields = policy["carrier_notice_fields"]
        filtered_payload = {key: payload[key] for key in allowed_fields if key in payload}
        if filtered_payload != payload:
            return Verdict.modify("Chỉ gửi hãng các trường chính sách cho phép", payload=filtered_payload)
        return Verdict.allow()

    order = ctx.tools.lookup_order(action["order_id"])
    if order is None or policy is None or not order.get("parcels"):
        return Verdict.escalate("Thiếu đơn, kiện hoặc chính sách hiệu lực để xác minh")

    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    requested_parcel_id = ctx.ticket.get("parcel_id")
    if requested_parcel_id and parcel["parcel_id"] != requested_parcel_id:
        return Verdict.escalate("Kiện được yêu cầu không thuộc đơn")
    delay_days = H.db_delay_days(parcel, ctx.as_of)

    if tool == "issue_refund":
        return _refund_gate(ctx, action, order, parcel, policy, delay_days)

    if not H.carrier_at_fault(policy, parcel, delay_days):
        return Verdict.deny("Tracking không xác nhận đủ căn cứ ghi lỗi hãng")
    recorded_fields = {
        "parcel_id": parcel["parcel_id"],
        "carrier_id": parcel["carrier_id"],
        "driver_id": parcel.get("driver_id"),
        "delay_days": delay_days,
    }
    if any(action.get(key) != value for key, value in recorded_fields.items()):
        return Verdict.modify("Dùng đúng kiện, hãng và độ trễ từ tracking", **recorded_fields)
    return Verdict.allow()


def _refund_gate(ctx, action, order, parcel, policy, delay_days):
    cause = parcel.get("delay_cause")
    entitlement = H.entitlement_vnd(policy, order, delay_days, cause)
    if entitlement == 0:
        return Verdict.deny("Tracking và chính sách không xác nhận quyền hoàn tiền")
    if not cause:
        return Verdict.escalate("Tracking thiếu nguyên nhân trễ để xác minh quyền hoàn")
    if action["amount_vnd"] != entitlement or action["payer"] != "LOGIX":
        return Verdict.escalate("Đề xuất tiền hoàn hoặc bên trả khác căn cứ nghiệp vụ")

    approval_id = action.get("approval_id")
    if entitlement <= policy["auto_limit_vnd"] and not approval_id:
        return _customer_daily_refund_gate(ctx, order["customer_id"], entitlement)

    approvals = ctx.tools.lookup_approvals(
        approval_id=approval_id,
        ticket_id=action["ticket_id"],
        order_id=order["order_id"],
        customer_id=order["customer_id"],
        status="valid",
    )
    approver_id = ctx.gates.get("operations", {}).get("approver_id")
    if any(
        approval.get("expires_at", "") >= ctx.as_of
        and approval.get("max_vnd", 0) >= entitlement
        and (not approver_id or approval.get("approver_id") == approver_id)
        for approval in approvals
    ):
        return Verdict.allow()
    return Verdict.escalate("Chưa có phê duyệt hợp lệ cho khoản hoàn của yêu cầu này")


def _customer_daily_refund_gate(ctx, customer_id, amount_vnd):
    limit = ctx.tools.ops_limits().get("max_auto_refund_per_customer_per_day_vnd")
    if limit is None:
        return Verdict.allow()

    # Ledger rows lack dates in the simulator. The host's daily total identifies
    # the suffix of automatic rows written today, excluding opening history.
    remaining = ctx.tools.auto_refund_today_vnd()
    customer_total = 0
    if remaining:
        for row in reversed(ctx.tools.ledger_rows()):
            if row.get("approval_id"):
                continue
            if row["customer_id"] == customer_id:
                customer_total += row["amount_vnd"]
            remaining -= row["amount_vnd"]
            if remaining == 0:
                break

    if customer_total + amount_vnd > limit:
        ctx.log("customer_auto_refund_cap_hit", spent_vnd=customer_total,
                requested_vnd=amount_vnd, cap_vnd=limit)
        return Verdict.escalate("Vượt trần hoàn tự động theo khách/ngày, cần người duyệt")
    return Verdict.allow()
