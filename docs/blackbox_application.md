# Mô tả ngắn: cách áp dụng kiểm thử hộp đen

Với mỗi bài toán, kiểm thử được thiết kế dựa trên đặc tả (hợp đồng đầu vào/đầu ra), không dựa vào cấu trúc bên trong của mã nguồn.

Quy trình chung:

1. Xác định miền đầu vào và đầu ra mong đợi.
2. Chia miền đầu vào thành các lớp tương đương:
   - lớp hợp lệ (dữ liệu chấp nhận)
   - lớp không hợp lệ (dữ liệu bị từ chối)
3. Chọn các giá trị biên quanh các ràng buộc.
4. Thiết kế test case cho:
   - hành vi hợp lệ thông thường
   - dữ liệu không hợp lệ và hành vi ngoại lệ
5. Đối chiếu kết quả thực tế/ngoại lệ với kết quả mong đợi.

Áp dụng theo từng bài toán:

- Chu vi/diện tích hình chữ nhật: ràng buộc kích thước phải là số dương.
- Phương trình bậc 2: phân lớp theo biệt thức (delta > 0, = 0, < 0) và trường hợp không hợp lệ a = 0.
- Số ngày trong tháng: phân lớp theo nhóm tháng (31/30/tháng 2), năm nhuận và không nhuận, cùng biên miền tháng.
- Kiểm tra số nguyên tố: phân lớp số nguyên tố, hợp số, n < 2 và sai kiểu dữ liệu.
- Tổng luân phiên: phân lớp theo tính chẵn/lẻ của n và ràng buộc n > 0.
- UCLN: phân lớp hai số khác 0, một số bằng 0, và cả hai bằng 0 là không hợp lệ.
- Tổng giai thừa: phân lớp n > 0 là hợp lệ, n <= 0 là không hợp lệ; đồng thời kiểm tra sai kiểu dữ liệu.
