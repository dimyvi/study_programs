def is_valid(string):

    if not string:
        return False

    if len(string) not in [4, 5, 6]:
        return False

    if not string.isdigit():
        return False

    return True
