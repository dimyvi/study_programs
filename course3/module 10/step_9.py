def do_twice(func):
    def qwerty(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return qwerty