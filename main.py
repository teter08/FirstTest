class GroceryItem:
    def __init__(self, name, price, quantity):
        self.name, self.price, self.quantity = name, price, quantity

    def __str__(self):
        return f'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}'

    def __repr__(self):
        return f'GroceryItem({self.name}, {self.price}, {self.quantity})'


banana = GroceryItem('Banana', 10, 5)
print(banana)
print(f"{banana!r}")

dragon_fruit = GroceryItem('Dragon fruit', 5, 350)
print(dragon_fruit)
print(f"{dragon_fruit!r}")
