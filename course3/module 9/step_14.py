def numbers_sum(elems):
    '''Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
    return sum(i for i in elems if isinstance(i, int) or isinstance(i, float))


print(numbers_sum([1, '2', 3, 4, 'five']))
print(numbers_sum(['beegeek', 'stepik', '100']))
print(numbers_sum.__doc__)