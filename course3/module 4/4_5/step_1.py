import pickle


def filter_dump(name, ls, type_):
    ans_ls = [i for i in ls if isinstance(i, type_)]
    with open(name, 'wb') as file:
        pickle.dump(ans_ls, file)