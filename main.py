class Config:
    pass


def create_instance(n: int) -> Config:
    obj = Config()
    [setattr(obj,f'attribute{i+1}', f"value{i+1}") for i in range(n)]
    return obj



create_instance(3)
print(create_instance(3).__dict__)