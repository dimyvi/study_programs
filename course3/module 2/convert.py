def convert(string):
    lower_count = sum(1 for char in string if char.islower())
    upper_count = sum(1 for char in string if char.isupper())

    if lower_count > upper_count:
        return string.lower()
    elif upper_count > lower_count:
        return string.upper()
    else:
        return string.lower()
