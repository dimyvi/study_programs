def info_kwargs(**kwargs):
    print('age:' ,kwargs.get('age'))
    print('age:', kwargs.get('age'))
    print('age:', kwargs.get('age'))
    print('age:', kwargs.get('age'))


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
