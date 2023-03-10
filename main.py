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

    def add(self, product: Product, col=1):
        if not self.goods.get(product):
            self.goods[product] = col
        else:
            self.goods[product] = col + self.goods[product]
        self.__total += col * product.price

    def remove(self, product: Product, col=1):
        if self.goods.get(product):
            if col >= self.goods[product]:
                self.__total -= self.goods[product] * product.price
                del self.goods[product]
            else:
                self.goods[product] = self.goods[product] - col

    @property
    def total(self):
        return self.__total

    def order(self):
        print('Заказ оплачен' if self.user.payment(self.__total) else 'Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        [print(f'{a[0].name} {a[0].price} {a[1]} {a[0].price * a[1]}') for a in
         sorted(self.goods.items(), key=lambda x: x[0].name)]
        print(f'---Total: {self.total}---')


billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20