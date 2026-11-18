# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `ProblemSolver`
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-ProblemSolver-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S2`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Hoàng Quốc Anh | `2A202603707` | Kỹ sư 1 · phụ trách cổng | Có |
|   2 | Đỗ Thị Thanh Bình | `2A202603709` | Sản phẩm và kinh doanh | |
|   3 | Lê Gia Hưng | `2A202603713` | Kỹ sư 2 · phụ trách kiểm thử và monitor | |
|   4 | Hà Quang Vinh | `2A202603720` | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Kế hoạch phân việc

Quốc Anh chịu trách nhiệm thay đổi `lab10/guards.py`. Gia Hưng chịu trách nhiệm kiểm thử cổng và viết `lab10/monitors.py`. Thanh Bình phụ trách tiêu chí, chi phí và phạm vi pilot. Quang Vinh phụ trách vận hành, pháp lý và kiểm đủ hồ sơ.

| Mốc | Quốc Anh · Cổng | Thanh Bình · Sản phẩm và kinh doanh | Gia Hưng · Kiểm thử và monitor | Quang Vinh · Vận hành và pháp lý |
|---|---|---|---|---|
| **0–15 · Cài đặt** | Chuẩn bị repo, nhánh và remote. | Chọn bản PRD v1.1 và eval card dùng chung. | Chạy bộ test công khai, kiểm môi trường Python. | Xác nhận danh sách thành viên và quyền đọc của team chấm. |
| **15–65 · Phiếu A và ký** | Rà xem các tiêu chí có thể kiểm được bằng report hoặc trace. Sau khi cả nhóm chốt, ký, commit và push trước lần đo đầu. | Chủ trì A1–A4, chọn ngưỡng chất lượng, chi phí và ROI, điền `acceptance_criteria.json`. | Góp ý cách đo (A2) và cách đọc khoảng tin cậy (A3). Kiểm file khóa và mã commit để nhóm ghi A5. | Đề xuất tiêu chí về quyền ghi, trần chờ duyệt và điều kiện dừng. Rà mục tiêu của kế toán và trưởng ca. |
| **65–115 · Bộ nền, cổng vòng 1 và v1** | Viết ba cổng từ B6 và mô tả ở B7.1. Chốt `prepared` sau khi có kết quả hồi quy từ Gia Hưng. | Viết bản đồ dữ liệu và drift ở B3. Điền mục `business` và lý do chọn số ở B7.4. Soạn v1 ở B8 theo report `prepared`. | Chạy baseline, gate và trace `T-002@55`, ghi B0–B2. Làm B7.2–B7.3, chạy hai ca tự soạn và kiểm ca mới hỏng trước khi bàn giao cho Quốc Anh chốt. | Viết HAZOP và checklist B4–B5. Điền `operations`, `legal` và runbook B7.5–B7.6. Cả nhóm cùng viết B6 và chốt v1. |
| **125–155 · Đo và phân tích S2** | Nhận đúng thẻ S2. Cùng Gia Hưng đọc các sự kiện trước lệnh ghi và đặt nhánh kỹ thuật trong cây nguyên nhân C6. | Đọc ROI, tiền trừ oan shop và tổng hoàn theo khách ở C1. Viết điều kiện nghiệp vụ kiểm được ở C5 và góp nhánh kinh doanh vào C6. | Ghi thẻ vào Phiếu C và chạy `grade` trước khi sửa. Ghi C0–C2, đối chiếu trace nguồn ticket, ghi chú đặt hàng và chuỗi hoàn cùng khách. | Điền quyền kiểm soát của người duyệt ở C3.1, HAZOP ở C4 và giả định sổ liên kênh ở C5. Rà C6 với cả nhóm. |
| **155–200 · Sửa, kiểm lại và chốt v2** | Thêm cổng tổng hoàn theo khách/ngày. Viết C7 và cập nhật cây nguyên nhân C9 với Gia Hưng. | Đối chiếu tác hại, ROI, chi phí và độ phủ giữa ba mốc. Soạn C12 và ba câu bắt buộc theo quyết định cả nhóm chốt. | Viết monitor và C8. Chạy lại S2, bộ nền và `grade`, ghi mã lần chạy và xác nhận các chỉ số gửi Thanh Bình. | Đọc tỷ lệ chuyển người và tải hàng chờ. Viết risk register và runbook C10–C11. Đối chiếu ba câu C12 với `submission/submission.json`. |
| **200–240 · Demo và bàn giao bài** | Giải thích cổng mới chuyển hai khoản vượt trần cho người duyệt trước khi ghi. Là đầu mối commit và push sau khi cả nhóm kiểm bài. | Dẫn phần so ba mốc và trình bày lý do chọn v2. | Chạy trace đối chiếu `S2-43@11` và ca hợp lệ `O-1026`. Nếu demo đổi config, khôi phục bản v2 và chạy lại `grade`. | Trình bày phương án trực và giới hạn còn lại. Chạy kiểm đủ thành phần sau khi hồ sơ cuối đã khớp, rồi bàn giao cho Quốc Anh. |

**Điểm bàn giao quan trọng.** Thanh Bình bàn giao ngưỡng đã được cả nhóm đồng ý cho Quốc Anh trước khi ký. Gia Hưng bàn giao report hồi quy trước khi Quốc Anh chốt `prepared`, và bàn giao report ba mốc trước khi cả nhóm quyết v2. Quang Vinh soát hồ sơ cuối. Trưởng nhóm đẩy bài chung và **mỗi thành viên tự nộp link trên LMS**.

## Cá nhân

## HoangQuocAnh-2A202603707

- **Phần việc phụ trách:** Sở hữu cổng ghi tiền, lỗi hãng và thông báo ở vòng 1. Chốt `prepared`, rồi bổ sung trần hoàn tự động theo khách/ngày ở vòng 2. Giải thích điểm chặn trước `issue_refund` khi demo.
- **Đóng góp cụ thể:** Dựng ba cổng xác minh quyền hoàn và phê duyệt, đối chiếu lỗi hãng với tracking, và lọc dữ liệu gửi hãng. Chốt bản vòng 1 rồi bổ sung kiểm tổng hoàn theo khách/ngày. Ở `S2-43@11`, cổng thấy khách đã nhận tự động 282.000đ và chuyển khoản đề xuất 104.000đ sang người duyệt trước khi ghi sổ hoặc báo hãng.
- **Bằng chứng:** [Cổng ghi và trần theo khách](lab10/guards.py), bản chốt `cca0b11d` trong commit vòng 1 `7d64e52`, [Phiếu B mục B7](templates/form-b-evaluation-gates.md#b7), [Phiếu C mục C7](templates/form-c-incident.md#c7) và trace `S2-43@11` của `R-S2-after-20261118-165145-adba56`.
- **Exit ticket:** Tôi học được rằng kiểm hạn mức từng đơn vẫn có thể bỏ sót nhiều khoản nhỏ cộng lại vượt quyền tự động. Tôi còn chưa chắc cách giữ bước kiểm trần và ghi sổ nhất quán khi hai kênh xử lý đồng thời cho cùng một khách.

## DoThiThanhBinh-2A202603709

- **Phần việc phụ trách:** Chủ trì Phiếu A, bản đồ dữ liệu, ngưỡng trong tiêu chí và cổng kinh doanh. So sánh tác hại, ROI, chi phí và độ phủ, rồi cầm bút viết v1/v2.
- **Đóng góp cụ thể:** Chuẩn bị mục tiêu, cách đo và ngưỡng chấp nhận trước lần chạy đầu. Lập bản đồ dữ liệu, giải thích trần hoàn toàn hệ thống và chi phí, rồi đối chiếu ba mốc S2. Đề xuất giữ v2 **Tiếp tục chuẩn bị pilot** vì chi phí 5.980đ/ticket và ROI 0,67 đạt ngưỡng đã ký. Nêu riêng tỷ lệ chuyển người 33,33% và điều kiện kiểm sổ liên kênh trước khi chạy thật.
- **Bằng chứng:** [Phiếu A mục A4](templates/form-a-criteria.md#a4), commit ký tiêu chí `4c1e1cc`, [cấu hình cổng kinh doanh](config/operating_gates.json), [quyết định v1 ở B8](templates/form-b-evaluation-gates.md#b8), [quyết định v2 ở C12](templates/form-c-incident.md#c12) và báo cáo `R-S2-grade-20261118-165145-adba56`.
- **Exit ticket:** Tôi học được rằng cần chốt ngưỡng trước khi nhìn số và đọc tác hại, chi phí, ROI cùng với tỷ lệ đúng. Tôi còn chưa chắc chi phí và tỷ lệ chuyển người ở hai kho dự kiến sẽ thay đổi thế nào khi dùng dữ liệu thật theo giờ cao điểm.

## LeGiaHung-2A202603713

- **Phần việc phụ trách:** Sở hữu các lần chạy và bằng chứng trace. Viết hai ca tự soạn, kiểm hồi quy độc lập với người viết cổng, bổ sung monitor tổng hoàn tự động theo khách/ngày và điều khiển terminal khi demo.
- **Đóng góp cụ thể:** Chạy baseline và đối chiếu trace `T-002@55`. Thử `O-1024` để kiểm ca không đủ điều kiện và `O-1026` để kiểm ca hợp lệ vẫn được phục vụ. Ở vòng 2, thêm monitor tổng hoàn tự động cao nhất theo khách/ngày, kiểm S2 đạt 75/75 và bộ nền giữ 110/110, rồi chuẩn bị trace so `prepared` với `after` cho demo.
- **Bằng chứng:** Baseline `R-base-before-20261118-152720-bde05c`, [hai ca tự soạn ở B7](templates/form-b-evaluation-gates.md#b7), [mã monitor](lab10/monitors.py), [định nghĩa và kết quả monitor ở C8](templates/form-c-incident.md#c8), lần chạy S2 `R-S2-after-20261118-165125-adba56` và hồi quy `R-base-after-20261118-165141-adba56`.
- **Exit ticket:** Tôi học được rằng kiểm thử phải có cả ca cần chặn và ca hợp lệ cần giữ. Tôi còn chưa chắc thiết kế bộ thử thế nào để phân biệt việc bị chuyển người đúng quy tắc với chuyển người quá nhiều khi các ca đến dồn dập.

## HaQuangVinh-2A202603720

- **Phần việc phụ trách:** Sở hữu HAZOP, checklist, quy trình trực và pháp lý. Phân tích quyền duyệt của thẻ S2, cập nhật runbook và kiểm hồ sơ nộp khớp report cuối.
- **Đóng góp cụ thể:** Lập HAZOP và checklist 9 nhóm việc, quy định ai duyệt khoản vượt hạn mức và ai có quyền tắt luồng. Với S2, phân tích quyền duyệt của chị Hạnh khi khoản mới làm vượt 300.000đ/khách/ngày. Cập nhật runbook với ngưỡng gọi dự phòng khi có 4 ca chờ hoặc ca lâu nhất chờ từ 30 phút, cùng tuyến đối soát cho shop và hãng.
- **Bằng chứng:** [Cấu hình vận hành và pháp lý](config/operating_gates.json), [HAZOP và checklist vòng 1](templates/form-b-evaluation-gates.md#b4), [bảng quyền kiểm soát của S2](templates/form-c-incident.md#c3), [sổ rủi ro](templates/form-c-incident.md#c10), [runbook vòng 2](templates/form-c-incident.md#c11) và [thông tin hồ sơ nộp](submission/submission.json).
- **Exit ticket:** Tôi học được rằng chuyển ca cho người chỉ có ích khi người duyệt nhận được căn cứ và còn công suất xử lý. Tôi còn chưa chắc một người trực có giữ được SLA 60 phút khi nhiều ca vượt trần đến cùng lúc.
