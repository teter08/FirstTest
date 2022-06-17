def factorial(n: int):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def trailing_zeros(n: int) -> int:
    '''

    :param n:
    :return:
    '''
    s = str(factorial(n))
    return len(s) - len(s.rstrip('0'))


print(trailing_zeros.__doc__)
