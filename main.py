s = input()
stek = []
if len(s) % 2 == 0:
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stek.append(s[i])
        elif (stek[-1] == '(' and s[i] == ')') or (stek[-1] == '[' and s[i] == ']') or (
                stek[-1] == '{' and s[i] == '}'):
            stek = stek[:-1]
else:
    print('NO')
print('YES' if s else 'NO')
