def reverse_args(func):
    def wrapper(*args, **kwargs):
        reverse = args[::-1]
        ans = func(*reverse, **kwargs)
        return ans
    return wrapper

@reverse_args
def power(a, n):
    return a ** n


print(power(2, 3))