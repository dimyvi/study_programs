is_num = lambda x: "-" not in x[1:] and x.replace('.', '', 1).replace("-", '').isdigit()
print(is_num('1233'))
