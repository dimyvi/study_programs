def pri(func):
    def werd(*args, **kwargs):
        answer = str(func(*args, **kwargs)).upper()
        return answer
    return werd


@pri
def print1():
    return
print1('hi', 'there', end='!\n')
print1('are you in trouble?')
print1(111, 222, 333, sep='xxx')
