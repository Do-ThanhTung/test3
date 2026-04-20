from .GiaiThua import factorial


def sum_factorials(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be > 0")

    return sum(factorial(i) for i in range(1, n + 1))
