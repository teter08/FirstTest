def linear(a, b):
    return lambda x: x * a + b


gp1 = linear(2, 3)
gp2 = lambda x: x * 2 + 3
print(gp2(2))
