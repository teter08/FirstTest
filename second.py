def fac(n):
    pr=1
    for i in range(1,1+n):
        pr*=i
        yield pr

for i in fac(6):
    print(i)