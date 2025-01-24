from functools import wraps


def square(func):
    @wraps(func)
    def wrappers(*args, **kwargs):
        ans = func(*args, **kwargs)
        return ans ** 2

    return wrappers


@square
def add(a, b):
    return a + b


print(add(3, 7))
print(add.__name__)
print(add.__doc__)
