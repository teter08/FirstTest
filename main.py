def info_kwargs(**kwargs):
    [print(f'{k} = {v}') for k, v in sorted(kwargs.items())]


info_kwargs(first_name="John", last_name="Doe", age=33)
