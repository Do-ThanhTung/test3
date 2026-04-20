def alternating_sum(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be > 0")

    total = 0
    for i in range(1, n + 1):
        total = total + i if i % 2 == 1 else total - i
    return total
