# Issue 1 - Các test case kiểm thử hộp đen cho dữ liệu hợp lệ

Tài liệu này liệt kê các test case dữ liệu hợp lệ theo kỹ thuật kiểm thử hộp đen:

- phân lớp tương đương
- phân tích giá trị biên (biên hợp lệ)

## 1) Tính chu vi hình chữ nhật

Đầu vào: length, width (> 0)
Đầu ra: perimeter = 2 \* (length + width)

| Mã TC | Đầu vào           | Kỹ thuật                             | Kết quả mong đợi |
| ----- | ----------------- | ------------------------------------ | ---------------- |
| RP-V1 | length=5, width=3 | Lớp tương đương hợp lệ               | 16               |
| RP-V2 | length=1, width=1 | Giá trị biên hợp lệ (nhỏ nhất dương) | 4                |

## 2) Tính diện tích hình chữ nhật

Đầu vào: length, width (> 0)
Đầu ra: area = length \* width

| Mã TC | Đầu vào           | Kỹ thuật               | Kết quả mong đợi |
| ----- | ----------------- | ---------------------- | ---------------- |
| RA-V1 | length=5, width=3 | Lớp tương đương hợp lệ | 15               |
| RA-V2 | length=1, width=2 | Giá trị biên hợp lệ    | 2                |

## 3) Giải phương trình bậc 2 ax^2 + bx + c = 0

Đầu vào: a, b, c với a != 0
Đầu ra: 2 nghiệm / nghiệm kép / vô nghiệm thực

| Mã TC | Đầu vào        | Kỹ thuật                | Kết quả mong đợi            |
| ----- | -------------- | ----------------------- | --------------------------- |
| QE-V1 | a=1, b=-3, c=2 | Lớp hợp lệ (delta > 0)  | type=two_roots, roots={1,2} |
| QE-V2 | a=1, b=2, c=1  | Biên hợp lệ (delta = 0) | type=double_root, root=-1   |

## 4) Tính số ngày của một tháng

Đầu vào: month trong [1..12], year > 0
Đầu ra: 28/29/30/31

| Mã TC | Đầu vào             | Kỹ thuật                                  | Kết quả mong đợi |
| ----- | ------------------- | ----------------------------------------- | ---------------- |
| DM-V1 | month=1, year=2024  | Lớp hợp lệ (tháng 31 ngày)                | 31               |
| DM-V2 | month=2, year=2024  | Lớp hợp lệ (năm nhuận)                    | 29               |
| DM-V3 | month=2, year=2023  | Lớp hợp lệ (không nhuận)                  | 28               |
| DM-V4 | month=12, year=2024 | Giá trị biên hợp lệ (biên trên của tháng) | 31               |

## 5) Kiểm tra số nguyên tố

Đầu vào: số nguyên n
Đầu ra: True/False

| Mã TC | Đầu vào | Kỹ thuật                                    | Kết quả mong đợi |
| ----- | ------- | ------------------------------------------- | ---------------- |
| PR-V1 | n=13    | Lớp hợp lệ (nguyên tố)                      | True             |
| PR-V2 | n=15    | Lớp hợp lệ (hợp số)                         | False            |
| PR-V3 | n=2     | Giá trị biên hợp lệ (số nguyên tố nhỏ nhất) | True             |

## 6) Tính tổng luân phiên S = 1 - 2 + 3 - ... + n

Đầu vào: số nguyên n > 0
Đầu ra: tổng nguyên

| Mã TC | Đầu vào | Kỹ thuật                         | Kết quả mong đợi |
| ----- | ------- | -------------------------------- | ---------------- |
| AS-V1 | n=5     | Lớp hợp lệ                       | 3                |
| AS-V2 | n=1     | Giá trị biên hợp lệ (n nhỏ nhất) | 1                |

## 7) Tìm UCLN của a và b

Đầu vào: số nguyên a, b (không đồng thời bằng 0)
Đầu ra: gcd(a,b)

| Mã TC  | Đầu vào    | Kỹ thuật                            | Kết quả mong đợi |
| ------ | ---------- | ----------------------------------- | ---------------- |
| GCD-V1 | a=48, b=18 | Lớp hợp lệ                          | 6                |
| GCD-V2 | a=0, b=5   | Giá trị biên hợp lệ (một số bằng 0) | 5                |

## 8) Tính tổng S = 1! + 2! + ... + n!

Đầu vào: số nguyên n > 0
Đầu ra: tổng nguyên

| Mã TC | Đầu vào | Kỹ thuật                         | Kết quả mong đợi |
| ----- | ------- | -------------------------------- | ---------------- |
| SF-V1 | n=3     | Lớp hợp lệ                       | 9                |
| SF-V2 | n=1     | Giá trị biên hợp lệ (n nhỏ nhất) | 1                |
