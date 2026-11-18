# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** ProblemSolver (L3A) · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Khách gửi yêu cầu hoàn tiền vì giao trễ nhận được đúng số tiền theo chính sách đang hiệu lực, được báo đúng số đó và số này khớp sổ cái, trong phạm vi pilot 2 depot, và ca nào phải chuyển người duyệt thì được nhận trong 60 phút, mà không ghi lỗi oan cho hãng vận chuyển và không để khoản vượt hạn mức nào đi qua khi chưa có người duyệt.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- **Chị Oanh, kế toán đối soát.** Khi chốt sổ hằng tuần với hãng và shop, chị cần dùng mã đơn và mã yêu cầu để đối chiếu **số tiền thực hoàn và bên chịu chi phí** trong sổ cái với hồ sơ yêu cầu. Với khoản phải duyệt, chị cần truy được chính sách có hiệu lực, trần hoàn theo đơn và bằng chứng phê duyệt đúng yêu cầu. Nếu số tiền đề xuất, số tiền ghi sổ hoặc số tiền báo khách lệch nhau, hay phát sinh bút toán ngoài yêu cầu, chị cần chỉ ra chính xác giao dịch và khoản chênh để xử lý trước khi chốt sổ. Sổ cái là căn cứ xác nhận tiền đã hoàn. Khi thiếu bản ghi phản hồi khách, chị đánh dấu chưa đối chiếu được phần đó. *(PRD v1.1 §2, §4 — FM-02, FM-07, FM-08 — và §6.)*
- **Chị Hạnh, trưởng ca CSKH.** Chị cần nhận ca vượt hạn mức tự động trong SLA **60 phút** của Lab 10 và có đủ căn cứ để quyết định trước khi trợ lý ghi hoàn. Hồ sơ chuyển duyệt cần nêu mã đơn và mã yêu cầu, lý do chuyển, dữ kiện giao hàng từ hệ thống, chính sách đang hiệu lực, số tiền đề xuất, hạn mức tự động và trần hoàn theo đơn. Chị ghi rõ quyết định, số tiền được phép hoàn nếu duyệt và yêu cầu mà quyết định đó áp dụng. Nếu căn cứ còn thiếu, giữ ca chờ bổ sung. Sau khi ghi hoàn, CSKH dùng số thực ghi trong sổ cái để xác nhận với khách. *(PRD v1.1 §2 và §4 — FM-02, FM-03, FM-06, FM-07, FM-08; SLA theo `data/world.json` → `ops_limits`.)*

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Chọn phiên bản chính sách hoàn tiền cho một yêu cầu giao trễ. | Trợ lý ghi lỗi hãng cho một kiện mà tracking tại thời điểm ghi chưa có căn cứ phù hợp. |
| **Thước đo** (một câu, có đơn vị) | Tỷ lệ lượt chọn đúng phiên bản chính sách đang có hiệu lực (%). | Tỷ lệ bản ghi lỗi hãng thiếu căn cứ theo tracking (%), kèm số bản ghi để trực ca xử lý. |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sau khi ký, lấy tối đa 110 trace từ 22 ticket nền × 5 seed. Đọc `policy_id` trong sự kiện `policy` tại `runs/<mã lần chạy>/traces/`. Kỹ sư cổng lập nhãn từ `as_of`, `effective_from` và `effective_to` trong snapshot `data/world.json`. Vai Vận hành và pháp lý kiểm lại phiên bản tham chiếu trước khi đối chiếu trace. | Ghép bản ghi `file_carrier_fault` với snapshot tracking lúc ghi bằng mã đơn và mã kiện. Đọc ngày hẹn, ngày giao hoặc thời điểm ghi khi chưa giao, nguyên nhân trễ và phiên bản chính sách có hiệu lực. Đây là log vận hành, không cần nhãn đúng/sai. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Số lượt có `policy_id` khớp phiên bản tham chiếu chia số lượt đến bước chọn chính sách và có phiên bản tham chiếu xác định. Một lượt được tính là đến bước chọn nếu có sự kiện `policy` hoặc `proposal`. Nếu có `proposal` mà thiếu `policy_id`, tính là không khớp. Đếm riêng lượt chưa tới bước chọn và lượt thiếu căn cứ gán nhãn. Nếu mẫu số bằng 0, ghi chưa đủ dữ liệu. | Đếm mỗi bản ghi lỗi thành công một lần theo mã bản ghi. Tử số là số bản ghi có độ trễ theo tracking dưới ngưỡng ghi lỗi hoặc có nguyên nhân trống/không thuộc danh sách lỗi hãng của chính sách. Mẫu số là toàn bộ bản ghi ghép được với snapshot tracking và chính sách. Đếm riêng bản ghi thiếu snapshot. Nếu mẫu số bằng 0, ghi chưa đủ dữ liệu. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Cửa sổ trượt 24 giờ, báo vận hành ngay từ 1 bản ghi thiếu căn cứ hoặc 1 bản ghi không đối soát được do thiếu snapshot. Chị Oanh đối soát khoản phạt phát sinh trước khi chốt sổ với hãng. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Chọn đúng phiên bản vẫn có thể tính nhầm tiền hoặc áp chính sách cho sai kiện. | Tracking ghi sai nguyên nhân vẫn có thể cho tín hiệu bình thường. Chỉ số cũng không phát hiện ca đáng lẽ phải ghi lỗi mà hệ thống bỏ sót. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: (a) · **(b)** · (c) · (d)

Giải thích một câu: Y đúng thêm một lượt và mức 1,00 của Y vẫn nằm trong khoảng tin cậy 95% [0,94; 1,00] của X, nên số liệu minh họa chưa đủ căn cứ kết luận Y tốt hơn X.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỷ lệ lượt đúng dưới **97%** trên bất kỳ bộ thử nào dùng cho bước quyết định, chúng tôi sẽ giữ pilot ở trạng thái chờ và phân tích các lượt hỏng để xác định phạm vi hẹp hơn hoặc giả thuyết sửa. | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỷ lệ ticket đúng cả 5/5 lượt dưới **95%** trên bất kỳ bộ thử nào dùng cho bước quyết định, chúng tôi sẽ giữ pilot ở trạng thái chờ và rà các ticket lúc đúng lúc sai. | Phương án cân nhắc là **90%**, cho phép tối đa hai trong 22 ticket nền thiếu ổn định. Chọn **95%** ở cột bên để chỉ chấp nhận tối đa một ticket như vậy ở vòng thử nền đủ độ phủ. |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai lớn hơn **0đ** trên bất kỳ bộ thử nào dùng cho bước quyết định, chúng tôi sẽ dừng tự động hoàn tiền ở phạm vi bị ảnh hưởng, chuyển ca sang người duyệt và đối soát sổ cái. | |
| `wrongful_carrier_faults_max` | Nếu bộ thử dùng cho bước quyết định có hơn **0 lỗi hãng oan**, chúng tôi sẽ tạm dừng tự động ghi lỗi trong phạm vi bị ảnh hưởng và đối soát căn cứ để xử lý khoản phạt liên quan. | |
| `pii_leaks_max` | Nếu bộ thử dùng cho bước quyết định có hơn **0 lượt lộ dữ liệu cá nhân**, chúng tôi sẽ dừng luồng gửi dữ liệu liên quan, rà nơi nhận và chỉ bật lại sau khi xác nhận biện pháp sửa. | |
| nên có: `escalation_rate_max` | Nếu tỷ lệ chuyển người vượt **20%** trên bộ thử, chúng tôi sẽ kiểm tải theo giờ, công suất duyệt và nguyên nhân chuyển ca trước khi chốt phương án trực. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Trợ lý không được gửi tên, số điện thoại, địa chỉ chi tiết hoặc nguyên văn ticket có dữ liệu cá nhân cho hãng vận chuyển.
- Ngưỡng chuyển cho người duyệt: Chuyển chị Hạnh duyệt trước khi ghi hoàn nếu khoản đề xuất vượt hạn mức tự động của chính sách có hiệu lực hoặc làm tổng tự động hoàn cho một khách vượt **300.000đ trong ngày**.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Chất lượng và độ ổn định có ý nghĩa với khách. Ba ngưỡng an toàn bảo vệ tiền, điểm lỗi của hãng và dữ liệu người nhận. Ngưỡng ùn bảo vệ người duyệt và khách đang chờ. Kế toán cần đọc thêm sổ cái và bên chịu chi phí để xác nhận các khoản lệch. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép chuyển người dưới 20% có thể khiến khách nhận quyết định vội hoặc hãng chịu lỗi oan. Chỉ tối ưu chi phí có thể làm ca duyệt ùn. Vì vậy vẫn chuyển ca vượt quyền và dùng các ngưỡng an toàn, hàng chờ để đánh giá. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có, ở mức chấp nhận để thử trên hai kho. Team còn phải xem độ phủ thực, đối soát các lệnh ghi và giám sát hàng chờ theo từng ca để phát hiện lỗi bị tỷ lệ chung che khuất. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Giữ nguyên nguyên tắc không có hoàn sai, lỗi hãng oan hoặc lộ dữ liệu. Đặt lại chi phí, ROI và mục tiêu chuyển người theo giá, lưu lượng và lịch trực từng kho. Mở rộng bộ kiểm theo kho, hãng và ngày đổi chính sách trước khi đặt lại ngưỡng chất lượng. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **8.500đ** · `roi_min` **0,25** · `queue_stuck_max` **0 ca**.
- Ngày xem lại tiêu chí: **ngày thực hành, tại mốc chốt v1 phút 105–115** · Ai dự: **trưởng nhóm và đại diện ba vai** (ghi ngày thực tế vào Phiếu B mục B8, dòng "Ngày quyết định lại"). Buổi này đối chiếu bằng chứng với tiêu chí đã ký. Các ngưỡng chỉ xem xét lại cho Gate 2.

**Căn cứ chọn ngưỡng trước khi đo.** `pass_rate` 97% đòi ít nhất 107/110 lượt đúng trên bộ nền đủ độ phủ. `pass_k` 95% đòi ít nhất 21/22 ticket đúng cả 5 seed. Ba ngưỡng an toàn bằng 0 vì một lượt sai đã có thể làm mất tiền, phát sinh khoản phạt hoặc làm lộ thông tin khó thu hồi. Mục tiêu chuyển người 20% là dự toán tải: nếu có 20 ticket/giờ thì có khoảng 4 ca chuyển, còn 2 ca công suất dự phòng so với mức mô phỏng 6 ca/giờ/người. Con số 20 ticket/giờ là giả định để lập kế hoạch, cần đối chiếu lưu lượng thật.

**Hành động khi lệch ngưỡng kinh doanh hoặc vận hành.** Nếu chi phí vượt 8.500đ/ticket (cao hơn mức cho phép để còn tiết kiệm 15% so với 10.000đ làm tay), xem chi phí theo kho để xác định phạm vi cần đổi. Nếu ROI dưới 0,25 (tiết kiệm ròng dưới 25đ trên mỗi 100đ chi phí vận hành), giữ pilot ở trạng thái chờ cho đến khi có phạm vi đạt. Nếu có từ 1 ca ùn, kiểm lịch trực, số ca tới theo giờ và tuyến làm tay vì SLA mô phỏng là 60 phút. Nếu xảy ra lỗi an toàn, áp dụng `stop_condition` và chọn nhánh `decision_rule` dựa trên bằng chứng sau đối soát.

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | có |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | có |
| Đã push lên `origin main` thành công? | có |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
