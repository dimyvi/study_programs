def is_greater(lists, number):
    flag = False
    for i in lists:
        if sum(i) > number:
            flag = True
    return flag
