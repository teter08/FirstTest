from string import ascii_letters


class Registration:
    def __init__(self, newlogin, newpassword):
        self.login = newlogin
        self.password = newpassword

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, newpassword):
        if not isinstance(newpassword, str): raise TypeError("Пароль должен быть строкой")
        if not (5 <= len(newpassword) < 12): raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(newpassword): raise ValueError(
            'Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(newpassword): raise ValueError(
            'Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(newpassword): raise ValueError(
            'Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(newpassword): raise ValueError(
            'Ваш пароль содержится в списке самых легких')

    @staticmethod
    def is_include_digit(newpassword):
        return 1 in [1 if a.isdigit() else 0 for a in newpassword]

    @staticmethod
    def is_include_all_register(newpassword):
        return newpassword != newpassword.lower() and newpassword != newpassword.upper()

    @staticmethod
    def is_include_only_latin(newpassword):
        return not 0 in [1 if a in ascii_letters else 0 for a in newpassword if not a.isdigit()]

    @staticmethod
    def check_password_dictionary(newpassword):
        with open('easy_passwords.txt') as file:
            lines = [line.rstrip() for line in file]
        return newpassword in lines

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, newlogin):
        if not isinstance(newlogin, str): raise TypeError
        if newlogin.count('@') != 1: raise ValueError
        if not newlogin.count('.', newlogin.find('@')) > 0: raise ValueError
        self.__login = newlogin


a = Registration('1@dfghj.kl2', 'QwerT123')
# print(Registration.is_include_only_latin('dgdfgFFF'))
