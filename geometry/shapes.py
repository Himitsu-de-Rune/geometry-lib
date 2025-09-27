import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError('Радиус должен быть положительным')
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f'Circle(radius={self.radius})'


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if min(a, b, c) <= 0:
            raise ValueError('Стороны должны быть положительными')
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError('Треугольник с такими сторонами не существует')
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9)

    def __repr__(self):
        return f'Triangle(a={self.a}, b={self.b}, c={self.c})'