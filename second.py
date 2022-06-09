a, b, c = map(int, input().split())

a = input().lower()
b = input().lower()

a = int(input())
mystr = list(map(int, input().split()))
a, b = map(int, input().split())
a1, b1 = a, b
while b > 0:
    c = a % b
    a = b
    b = c
print((a1*b1)//a)
