def sandwich(func):
    def name(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        result = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return result
    return name