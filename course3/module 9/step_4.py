def non_negative_even(numbers):
    data = map(lambda x: x >= 0 and x % 2 == 0, numbers)
    return all(data)
