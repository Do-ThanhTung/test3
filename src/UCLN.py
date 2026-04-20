def gcd(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers")
    if a == 0 and b == 0:
        raise ValueError("at least one of a or b must be non-zero")

    x, y = abs(a), abs(b)
    while y != 0:
        x, y = y, x % y
    return x
