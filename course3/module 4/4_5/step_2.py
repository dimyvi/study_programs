import pickle

file_name = input()
num = int(input())

with open(file_name, 'rb') as file:
    control_summ = 0
    obj = pickle.load(file)
    if isinstance(obj, list):
        us = [i for i in obj if type(i) == int]
        if len(us) > 0:
            control_summ = min(us) * max(us)
    elif isinstance(obj, dict):
        control_summ = sum([j for j in obj if isinstance(j, int)])
    elif isinstance(obj, int):
        control_summ = obj

    if control_summ == num:
        print('Контрольные суммы совпадают')
    else:
        print('Контрольные суммы не совпадают')