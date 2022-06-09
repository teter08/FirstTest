s = input()
stek = []
bool = True
if len(s) % 2 == 0:
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stek.append(s[i])
        elif stek:
            if (stek[-1] == '(' and s[i] == ')') or (stek[-1] == '[' and s[i] == ']') or (
                    stek[-1] == '{' and s[i] == '}'):
                stek = stek[:-1]
            else:
                bool = False
                break
        else:
            bool = False
            break
else:
    bool = False
print('YES' if s and bool else 'NO')
