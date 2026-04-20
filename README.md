# Bài thực hành 03 - Kiểm thử hộp đen

Đây là bài thực hành xây dựng chương trình và thiết kế kiểm thử hộp đen cho 8 bài toán cơ bản. Repository đã bao gồm mã nguồn, test case, kết quả chạy kiểm thử và mô tả ngắn gọn cách áp dụng black-box testing.

## Các bài toán

1. Tính chu vi hình chữ nhật
2. Tính diện tích hình chữ nhật
3. Giải phương trình bậc 2
4. Tính số ngày của một tháng
5. Kiểm tra số nguyên tố
6. Tính tổng S = 1 - 2 + 3 - 4 + ... + n
7. Tìm UCLN của a và b
8. Tính tổng S = 1! + 2! + 3! + ... + n!

## Cấu trúc thư mục

- [main.py](main.py): chương trình menu để chạy trực tiếp
- [src/](src): các file chương trình theo từng bài toán
- [tests/](tests): test tự động cho 2 issue
- [docs/](docs): test case, mô tả black-box và kết quả chạy test

## Mã nguồn chương trình

- [src/ChuViHCN.py](src/ChuViHCN.py)
- [src/DienTichHCN.py](src/DienTichHCN.py)
- [src/GiaiPhuongTrinhBac2.py](src/GiaiPhuongTrinhBac2.py)
- [src/SoNgayTrongThang.py](src/SoNgayTrongThang.py)
- [src/SoNguyenTo.py](src/SoNguyenTo.py)
- [src/TinhTongS.py](src/TinhTongS.py)
- [src/UCLN.py](src/UCLN.py)
- [src/GiaiThua.py](src/GiaiThua.py)
- [src/TongCacGiaiThua.py](src/TongCacGiaiThua.py)

File tổng hợp để import chung:

- [src/algorithms.py](src/algorithms.py)
- [src/**init**.py](src/__init__.py)

## Danh sách test case

- Hợp lệ: [docs/testcases_issue1_valid.md](docs/testcases_issue1_valid.md)
- Không hợp lệ, biên và ngoại lệ: [docs/testcases_issue2_invalid_boundary.md](docs/testcases_issue2_invalid_boundary.md)

## Mô tả áp dụng kiểm thử hộp đen

- [docs/blackbox_application.md](docs/blackbox_application.md)

## Kết quả chạy kiểm thử

- [docs/test_results.txt](docs/test_results.txt)

## Cách chạy chương trình

Chạy menu nhập liệu trực tiếp:

```bash
python main.py
```

## Cách chạy kiểm thử

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## GitHub Issues và commit

Đã chia công việc theo 2 issue:

### Issue 1

- Thiết kế và viết các ca kiểm thử hộp đen cho các trường hợp dữ liệu hợp lệ.

### Issue 2

- Thiết kế và viết các ca kiểm thử hộp đen cho các trường hợp dữ liệu không hợp lệ, biên và ngoại lệ.
