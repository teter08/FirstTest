from math import ceil

# n = int(input())
n = 4
a = [[0] * n for _ in range(n)]
x, y = 0, 0
nom = 1
size = n
for qqq in range(ceil(n)):
    for i in range(size):
        a[x][y] = nom
        nom += 1
        y += 1
    y -= 1
    x += 1
    size -= 1
    for i in range(size):
        a[x][y] = nom
        nom += 1
        x += 1
    x -= 1
    y -= 1
    for i in range(size):
        a[x][y] = nom
        nom += 1
        y -= 1
    y += 1
    x -= 1
    size -= 1
    for i in range(size):
        a[x][y] = nom
        nom += 1
        x -= 1
    x += 1
    y += 1

for line in a:
    print('\t'.join(map(str, line)))
