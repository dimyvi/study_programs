def custom_isinstance(objects, typeinfo):
    return len([i for i in objects if isinstance(i, typeinfo)])
