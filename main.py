s = ''
com = {'Дили': set(), 'Били': set(), 'Вили': set()}
while s != 'конец':
    s = input()
    if s.split()[0] == 'Дили:':
        com['Дили'].add(s.split()[1])
    if s.split()[0] == 'Вили:':
        com['Вили'].add(s.split()[1])
    if s.split()[0] == 'Били:':
        com['Били'].add(s.split()[1])
s = sorted(com.items(), key=lambda x: len(x[1]), reverse=True)
print(f'Количество уникальных комментаторов у {s[0][0]} - {len(s[0][1])}')
print(f'Количество уникальных комментаторов у {s[1][0]} - {len(s[1][1])}')
print(f'Количество уникальных комментаторов у {s[2][0]} - {len(s[2][1])}')