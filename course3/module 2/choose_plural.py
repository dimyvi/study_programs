def choose_plural(amount, declensions):
    if amount % 10 == 1 and amount % 100 != 11:
        return f"{amount} {declensions[0]}"
    elif 2 <= amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        return f"{amount} {declensions[1]}"
    else:
        return f"{amount} {declensions[2]}"