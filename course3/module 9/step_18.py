def get_digits(number: int | float) -> list[int]:
    answer = [int(i) for i in str(number) if i.isdigit()]
    return answer

annotations = get_digits.__annotations__

print(annotations['return'])