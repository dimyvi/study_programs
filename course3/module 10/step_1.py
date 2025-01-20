def power(degree):
    def top(x):
        return x**degree
    return top


print(power(5))