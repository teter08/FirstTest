class Order:
    def __init__(self, cart: list, customer: str):
        self.cart, self.customer = cart, customer

    def __add__(self, other):
        return Order(self.cart + [other], self.customer)

    def __radd__(self, other):
        return Order([other] + self.cart, self.customer)

    def __sub__(self, other):
        try:
            self.cart.remove(other)
        except:
            pass
        return Order(self.cart, self.customer)

    def __rsub__(self, other):
        return self - other


order = Order(['banana', 'apple'], 'Гена Букин')

order_2 = order + 'orange'
assert order.cart == ['banana', 'apple']
assert order.customer == 'Гена Букин'
assert order_2.cart == ['banana', 'apple', 'orange']

order = 'mango' + order
assert order.cart == ['mango', 'banana', 'apple']
order = 'ice cream' + order
assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

order = order - 'banana'
assert order.cart == ['ice cream', 'mango', 'apple']

order3 = order - 'banana'
assert order3.cart == ['ice cream', 'mango', 'apple']

order = order - 'mango'
assert order.cart == ['ice cream', 'apple']
order = 'lime' - order
assert order.cart == ['ice cream', 'apple']
print('Good')
