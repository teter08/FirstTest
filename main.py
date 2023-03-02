class Circle:
    @classmethod
    def from_diameter(cls, d):
        return Circle(d / 2)

    @staticmethod
    def is_positive(number):
        return number > 0

    @staticmethod
    def area(radius):
        return 2 * 3.14 * radius * radius

    def __init__(self, radius):
        if not Circle.is_positive(radius):
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius


# код ниже не нужно удалять, в нем находятся проверки
circle_1 = Circle.from_diameter(10)
assert isinstance(circle_1, Circle)
assert circle_1.radius == 5.0
print(f"circle_1.radius={circle_1.radius}")
assert Circle.is_positive(10)
assert not Circle.is_positive(-5)
assert Circle.area(1) == 6.28
