from functools import wraps
from types import NoneType


def returns_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ans = func(*args, **kwargs)
        if not isinstance(ans, str) or type(ans) == None:
            raise TypeError
        return ans
    return wrapper


@returns_string
def nothing():
    return

print(nothing.__name__)
print(nothing.__doc__)

try:
    nothing()
except TypeError as e:
    print(type(e))