def longest_word_in_file(file_name: str) -> str:
    with open(file_name, 'r', encoding='utf-8') as inf:
        lines = inf.read().split()
    col = [int(x) for x in lines if len(x)==2]
    return sum(col)


print(longest_word_in_file(r'C:\Новая папка\numbers.txt'))
