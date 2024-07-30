def convert(number):
    if number >= 0:
        return (bin(number)[2:], oct(number)[2:], hex(number)[2:].upper())
    if number < 0:
        return ('-' + str(bin(number)[3:]), '-' + str(oct(number)[3:]), '-' + str(hex(number)[3:].upper()))