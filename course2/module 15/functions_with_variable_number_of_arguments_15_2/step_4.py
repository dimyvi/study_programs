def greet(*args):
    args[0]
    ls = [i for i in args]
    s = ' and '.join(j for j in ls)
    print('Hello, ' + s + '!', sep='')

greet('Timur')
greet('Timur', 'Roman')
greet('Timur', 'Roman', 'Ruslan')