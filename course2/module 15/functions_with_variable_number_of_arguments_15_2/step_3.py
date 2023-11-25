def mean(*args):
    ls = [i for i in args if type(i) is int or type(i) is float]
    if len(ls) == 0:
        return 0.0
    return sum(ls)/len(ls)