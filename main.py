def shift_letter(letter: str, shift: int) -> str:
    '''Функция сдвигает символ letter на shift позиций'''
    return chr((ord(letter) - 96 + shift) % 26 + 96)


print(shift_letter.__doc__)
