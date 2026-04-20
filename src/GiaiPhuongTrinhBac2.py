import math
from typing import Union


Number = Union[int, float]


def _validate_number(value: Number, name: str) -> None:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be int or float")


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
