# HW 31
class Calculator:
    def __init__(self, a):
        if not self.is_valid_a(a):
            raise ValueError('Must be int or float!!')
        self.__a = a

    @staticmethod
    def is_valid_a(a):
        return isinstance(a, int | float)

    def __str__(self):
        return f'The number is: {self.__a}'

    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__a + other.__a)
        return Calculator(self.__a + other)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__a - other.__a)
        return Calculator(self.__a - other)

    def __rsub__(self, other):
        return Calculator(other - self.__a)

    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__a * other.__a)
        return Calculator(self.__a * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__a / other.__a)
        return Calculator(self.__a / other)

    def __rtruediv__(self, other):
        return Calculator(other / self.__a)

    def __floordiv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__a // other.__a)
        return Calculator(self.__a // other)

    def __rfloordiv__(self, other):
        return Calculator(other // self.__a)

    def __mod__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__a % other.__a)
        return Calculator(self.__a % other)

    def __rmod__(self, other):
        return Calculator(other % self.__a)

    def __pow__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__a ** other.__a)
        return Calculator(self.__a ** other)

    def __rpow__(self, other):
        return Calculator(other ** self.__a)

    def __iadd__(self, other):
        if isinstance(other, Calculator):
            self.__a += other.__a
        else:
            self.__a += other
        return self

    def __isub__(self, other):
        if isinstance(other, Calculator):
            self.__a -= other.__a
            return self
        self.__a -= other
        return self

    def __imul__(self, other):
        if isinstance(other, Calculator):
            self.__a *= other.__a
            return self
        self.__a *= other
        return self

    def __itruediv__(self, other):
        if isinstance(other, Calculator):
            self.__a /= other.__a
            return self
        self.__a *= other
        return self

    def __ifloordiv__(self, other):
        if isinstance(other, Calculator):
            self.__a //= other.__a
            return self
        self.__a //= other
        return self

    def __imod__(self, other):
        if isinstance(other, Calculator):
            self.__a %= other.__a
            return self
        self.__a %= other
        return self

    def __ipow__(self, other):
        if isinstance(other, Calculator):
            self.__a **= other.__a
            return self
        self.__a **= other
        return self

    def __eq__(self, other):
        if isinstance(other, Calculator):
            return self.__a == other.__a
        return self.__a == other

    def __ne__(self, other):
        if isinstance(other, Calculator):
            return self.__a != other.__a
        return self.__a != other

    def __lt__(self, other):
        if isinstance(other, Calculator):
            return self.__a < other.__a
        return self.__a < other

    def __le__(self, other):
        if isinstance(other, Calculator):
            return self.__a <= other.__a
        return self.__a <= other

    def __gt__(self, other):
        if isinstance(other, Calculator):
            return self.__a > other.__a
        return self.__a > other

    def __ge__(self, other):
        if isinstance(other, Calculator):
            return self.__a >= other.__a
        return self.__a >= other


# x = Calculator(6)
# x1 = Calculator(7)
# x += 5
# print(x)
# print(x + x1)
# print(x + 5)
# print(6 + x)
# print(x1 - 8)
# print(7 * x)
# print(x * 7)
# print(3 / x)
# print(3 // x)
# print(3 ** x)
# print(x / 12)
# print(x / 7)
# print(x1 // x)
# print(x1 % x)
# print(x1 ** x)
# print(x >= 5)
