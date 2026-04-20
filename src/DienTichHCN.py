from typing import Union


Number = Union[int, float]


def _validate_number(value: Number, name: str) -> None:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be int or float")


def rectangle_area(length: Number, width: Number) -> float:
    _validate_number(length, "length")
    _validate_number(width, "width")
    if length <= 0 or width <= 0:
        raise ValueError("length and width must be > 0")
    return length * width
