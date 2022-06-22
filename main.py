n = int(input())
d = {}
for i in range(n):
    s = input().split()
    if s[1] in d:
        d[s[1]].append(s[0])
    else:
        d[s[1]] = [s[0]]
n = int(input())
a = []
for i in range(n):
    a.append(input())
for i in a:
    print(*d.get(i,['Неизвестный номер']))
