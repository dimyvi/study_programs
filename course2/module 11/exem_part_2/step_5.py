def merge(dicts):
    result = {}
    for d in dicts:
        for x in d:
            result.setdefault(x, set()).add(d[x])
    return result


