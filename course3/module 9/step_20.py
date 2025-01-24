def cyclic_shift(numbers: list[int | float], step: int) -> None:
    step %= len(numbers)
    numbers[:] = numbers[-step:] + numbers[:-step]
