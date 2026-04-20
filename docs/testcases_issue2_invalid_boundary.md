# Issue 2 - Các test case kiểm thử hộp đen cho dữ liệu không hợp lệ, biên, ngoại lệ

Tài liệu này tập trung vào:

- lớp tương đương không hợp lệ
- dữ liệu ngoài miền giá trị
- xử lý ngoại lệ

## 1) Tính chu vi hình chữ nhật

| Mã TC | Đầu vào             | Kỹ thuật          | Hành vi mong đợi |
| ----- | ------------------- | ----------------- | ---------------- |
| RP-I1 | length=-1, width=3  | Lớp không hợp lệ  | Raise ValueError |
| RP-I2 | length=0, width=3   | Biên không hợp lệ | Raise ValueError |
| RP-I3 | length="5", width=3 | Sai kiểu dữ liệu  | Raise TypeError  |

## 2) Tính diện tích hình chữ nhật

| Mã TC | Đầu vào            | Kỹ thuật          | Hành vi mong đợi |
| ----- | ------------------ | ----------------- | ---------------- |
| RA-I1 | length=0, width=3  | Biên không hợp lệ | Raise ValueError |
| RA-I2 | length=-2, width=3 | Lớp không hợp lệ  | Raise ValueError |

## 3) Giải phương trình bậc 2

| Mã TC | Đầu vào         | Kỹ thuật               | Hành vi mong đợi  |
| ----- | --------------- | ---------------------- | ----------------- |
| QE-I1 | a=0, b=2, c=1   | Lớp không hợp lệ       | Raise ValueError  |
| QE-I2 | a=1, b=0, c=1   | Lớp hợp lệ (delta < 0) | type=no_real_root |
| QE-I3 | a="1", b=2, c=1 | Sai kiểu dữ liệu       | Raise TypeError   |

## 4) Tính số ngày của một tháng

| Mã TC | Đầu vào              | Kỹ thuật                       | Hành vi mong đợi |
| ----- | -------------------- | ------------------------------ | ---------------- |
| DM-I1 | month=0, year=2024   | Biên không hợp lệ (nhỏ hơn 1)  | Raise ValueError |
| DM-I2 | month=13, year=2024  | Biên không hợp lệ (lớn hơn 12) | Raise ValueError |
| DM-I3 | month=2, year=0      | Lớp không hợp lệ (year <= 0)   | Raise ValueError |
| DM-I4 | month="2", year=2024 | Sai kiểu dữ liệu               | Raise TypeError  |

## 5) Kiểm tra số nguyên tố

| Mã TC | Đầu vào | Kỹ thuật                           | Hành vi mong đợi |
| ----- | ------- | ---------------------------------- | ---------------- |
| PR-I1 | n=1     | Giá trị biên                       | False            |
| PR-I2 | n=0     | Miền không hợp lệ cho số nguyên tố | False            |
| PR-I3 | n=3.5   | Sai kiểu dữ liệu                   | Raise TypeError  |

## 6) Tính tổng luân phiên

| Mã TC | Đầu vào | Kỹ thuật          | Hành vi mong đợi |
| ----- | ------- | ----------------- | ---------------- |
| AS-I1 | n=0     | Biên không hợp lệ | Raise ValueError |
| AS-I2 | n=-2    | Lớp không hợp lệ  | Raise ValueError |
| AS-I3 | n="5"   | Sai kiểu dữ liệu  | Raise TypeError  |

## 7) Tìm UCLN

| Mã TC  | Đầu vào     | Kỹ thuật         | Hành vi mong đợi |
| ------ | ----------- | ---------------- | ---------------- |
| GCD-I1 | a=0, b=0    | Lớp không hợp lệ | Raise ValueError |
| GCD-I2 | a=5, b="10" | Sai kiểu dữ liệu | Raise TypeError  |

## 8) Tính tổng giai thừa

| Mã TC | Đầu vào | Kỹ thuật          | Hành vi mong đợi |
| ----- | ------- | ----------------- | ---------------- |
| SF-I1 | n=0     | Biên không hợp lệ | Raise ValueError |
| SF-I2 | n=-1    | Lớp không hợp lệ  | Raise ValueError |
| SF-I3 | n=2.2   | Sai kiểu dữ liệu  | Raise TypeError  |
