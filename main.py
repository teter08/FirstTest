s = input()
s = list(map(int, s))
count = [0] * 10
for i in s:
    count[i] += 1
for i, v in enumerate(count):
    if v != 0: print(i, v)
