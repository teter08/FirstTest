# n, m = map(int, input().split())
n, m = 3, 4
a = []
x=0
for i in range(n):
    if i%2!=0:
        a.append([x for x in range(m)])

print(a)
