from src.algorithms import (
    alternating_sum,
    days_in_month,
    gcd,
    is_prime,
    rectangle_area,
    rectangle_perimeter,
    solve_quadratic,
    sum_factorials,
)


def read_int(prompt: str) -> int:
    return int(input(prompt))


def read_float(prompt: str) -> float:
    return float(input(prompt))


def run_rectangle_perimeter() -> None:
    length = read_float("Nhap chieu dai: ")
    width = read_float("Nhap chieu rong: ")
    print(f"Chu vi hinh chu nhat = {rectangle_perimeter(length, width)}")


def run_rectangle_area() -> None:
    length = read_float("Nhap chieu dai: ")
    width = read_float("Nhap chieu rong: ")
    print(f"Dien tich hinh chu nhat = {rectangle_area(length, width)}")


def run_quadratic_equation() -> None:
    a = read_float("Nhap a: ")
    b = read_float("Nhap b: ")
    c = read_float("Nhap c: ")
    result = solve_quadratic(a, b, c)
    print(f"Ket qua = {result}")


def run_days_in_month() -> None:
    month = read_int("Nhap thang: ")
    year = read_int("Nhap nam: ")
    print(f"So ngay cua thang = {days_in_month(month, year)}")


def run_prime_check() -> None:
    n = read_int("Nhap n: ")
    print(f"{n} la so nguyen to: {is_prime(n)}")


def run_alternating_sum() -> None:
    n = read_int("Nhap n: ")
    print(f"Tong S = {alternating_sum(n)}")


def run_gcd() -> None:
    a = read_int("Nhap a: ")
    b = read_int("Nhap b: ")
    print(f"UCLN = {gcd(a, b)}")


def run_sum_factorials() -> None:
    n = read_int("Nhap n: ")
    print(f"Tong cac giai thua = {sum_factorials(n)}")


def show_menu() -> None:
    print("1. Tinh chu vi hinh chu nhat")
    print("2. Tinh dien tich hinh chu nhat")
    print("3. Giai phuong trinh bac 2")
    print("4. Tinh so ngay cua mot thang")
    print("5. Kiem tra so nguyen to")
    print("6. Tinh tong S = 1 - 2 + 3 - ... + n")
    print("7. Tim UCLN cua a va b")
    print("8. Tinh tong cac giai thua")
    print("0. Thoat")


ACTIONS = {
    1: run_rectangle_perimeter,
    2: run_rectangle_area,
    3: run_quadratic_equation,
    4: run_days_in_month,
    5: run_prime_check,
    6: run_alternating_sum,
    7: run_gcd,
    8: run_sum_factorials,
}


def main() -> None:
    while True:
        show_menu()
        try:
            choice = read_int("Chon chuc nang: ")
        except EOFError:
            print("Da ket thuc nhap lieu.")
            break
        except ValueError:
            print("Lua chon khong hop le. Vui long nhap so nguyen.")
            continue

        if choice == 0:
            print("Da thoat chuong trinh.")
            break

        action = ACTIONS.get(choice)
        if action is None:
            print("Lua chon khong ton tai.")
            continue

        try:
            action()
        except EOFError:
            print("Da ket thuc nhap lieu.")
            break
        except Exception as exc:
            print(f"Loi: {exc}")


if __name__ == "__main__":
    main()
