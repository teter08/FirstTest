a, b, c = map(int, input().split())

mystr = list(map(int, input().split()))

n = int(input())
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(4):
    a.append(input())

a, b = map(int, input().split())
a1, b1 = a, b
while b > 0:
    c = a % b
    a = b
    b = c
print((a1 * b1) // a)
