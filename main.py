class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name, self.last_name, self.age = first_name, last_name, age

    def full_name(self) -> str:
        return f'{self.last_name} {self.first_name}'

    def is_adult(self) -> bool:
        return self.age >= 18


p1 = Person('Jimi', 'Hendrix', 18)
print(p1.full_name())  # выводит "Hendrix Jimi"
print(p1.is_adult()) # выводит "True"
