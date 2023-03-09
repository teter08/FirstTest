import collections


class Product:
    def __init__(self, name, price):
        self.name, self.price = name, price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, newbalance):
        self.__balance = newbalance

    def deposit(self, newdeposit):
        self.__balance += newdeposit

    def payment(self, newpayment):
        if self.__balance - newpayment >= 0:
            self.__balance = self.__balance - newpayment
            return True
        else:
            print('Не хватает средств на балансе. Пополните счет')
            return False


class Cart:
    def __init__(self, user):
        self.user = user
        self.goods = collections.defaultdict()
        self.__total = 0
