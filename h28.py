# HW 29

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.h = None
        self.alpha = None
        self.r = None
        self.pi = None

    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r, pi):
        self.r = r
        self.pi = 3.14

    def perimetr(self):
        return f'{2 * self.pi * self.r} Circle->P'

    def area(self):
        return f'{self.pi * self.r ** 2}Circle->S'


class Triangle(Shape):
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def perimetr(self):
        return f'{(self.a + self.b + self.c) / 2} Triangle->P'

    def area(self):
        P = (self.a + self.b + self.c) / 2
        if self.h == None:
            return f'{(P * (P - self.a) * (P - self.b) * (P - self.c)) ** 0.5} Triangle->S'
        elif self.c > self.a and self.b:
            return f'{(self.c * self.h) / 2} Triangle->S'
        elif self.a > self.c and self.b:
            return f'{(self.a * self.h) / 2} Triangle->S'
        elif self.b > self.a and self.c:
            return f'{(self.b * self.h) / 2} Triangle->S'
        else:
            raise ValueError


class Rectangle(Shape):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def perimetr(self):
        return f'{(self.a + self.b) * 2} Rectangle->P'

    def area(self):
        if self.h == None:
            return f'{self.a * self.b} Rectangle->S'
        elif self.a == None:
            return f'{self.b * self.h} Rectangle->S'
        elif self.b == None:
            return f'{self.a * self.h} Rectangle->S'
        else:
            raise ValueError


P1 = Circle(6, pi=None)
print(P1.perimetr(), P1.area())
P2 = Triangle(6, 8, 10, h=None)
P2_1 = Triangle(24, 7, 25, 10)
print(P2.perimetr())
print(P2.area(), P2_1.area())
P3 = Rectangle(10, 5, h=None)
P3_1 = Rectangle(34, b=None, h=14)
print(P3.perimetr())
print(P3.area(), P3_1.area())
