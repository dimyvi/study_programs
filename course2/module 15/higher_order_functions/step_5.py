def func_apply(fn, ls):
    new_ls = []
    for i in ls:
        new_ls.append(fn(i))
    return new_ls