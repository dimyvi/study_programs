def my_pow(number):
    return sum(j[1]**j[0] for j in enumerate([int(i) for i in str(number)], 1))
