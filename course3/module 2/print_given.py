def print_given(*args, **kwargs):
    # Вывод позиционных аргументов
    for arg in args:
        print(f"{arg} {type(arg)}")

    # Вывод именованных аргументов
    for key in sorted(kwargs.keys()):
        print(f"{key} {kwargs[key]} {type(kwargs[key])}")
