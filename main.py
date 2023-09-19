d = {}
while (x := input()) != 'конец':
    if x.split(': ')[0] in d:
        if x.split(': ')[1] in d:
            d[x.split(': ')[0]][x.split(': ')[1]] += 1
        else:
            d[x.split(': ')[0]][x.split(': ')[1]] = 1
    else:
        d[x.split(': ')[0]] = 1

print(d)
