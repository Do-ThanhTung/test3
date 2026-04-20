"""Core functions for black-box testing practice."""

from __future__ import annotations

import math
from typing import Tuple, Union


Number = Union[int, float]


def _validate_number(value: Number, name: str) -> None:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be int or float")


def rectangle_perimeter(length: Number, width: Number) -> float:
    _validate_number(length, "length")
    _validate_number(width, "width")
    if length <= 0 or width <= 0:
        raise ValueError("length and width must be > 0")
    return 2 * (length + width)


def rectangle_area(length: Number, width: Number) -> float:
    _validate_number(length, "length")
    _validate_number(width, "width")
    if length <= 0 or width <= 0:
        raise ValueError("length and width must be > 0")
    return length * width


def solve_quadratic(a: Number, b: Number, c: Number):
    _validate_number(a, "a")
    _validate_number(b, "b")
    _validate_number(c, "c")

    if a == 0:
        raise ValueError("a must not be 0 for quadratic equation")

    delta = b * b - 4 * a * c
    if delta < 0:
        return {"type": "no_real_root", "roots": ()}
    if delta == 0:
        x = -b / (2 * a)
        return {"type": "double_root", "roots": (x,)}

    sqrt_delta = math.sqrt(delta)
    x1 = (-b + sqrt_delta) / (2 * a)
    x2 = (-b - sqrt_delta) / (2 * a)
    return {"type": "two_roots", "roots": (x1, x2)}


def days_in_month(month: int, year: int) -> int:
    if not isinstance(month, int) or not isinstance(year, int):
        raise TypeError("month and year must be integers")
    if year <= 0:
        raise ValueError("year must be > 0")
    if month < 1 or month > 12:
        raise ValueError("month must be in [1, 12]")

    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30

    is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    return 29 if is_leap else 28


def is_prime(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


def alternating_sum(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be > 0")

    total = 0
    for i in range(1, n + 1):
        total = total + i if i % 2 == 1 else total - i
    return total


def gcd(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers")
    if a == 0 and b == 0:
        raise ValueError("at least one of a or b must be non-zero")

    x, y = abs(a), abs(b)
    while y != 0:
        x, y = y, x % y
    return x


def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be >= 0")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def sum_factorials(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be > 0")

    return sum(factorial(i) for i in range(1, n + 1))
