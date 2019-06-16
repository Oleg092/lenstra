#!/usr/bin/env python3
from fractions import Fraction, gcd

class PointsCurve:
    def __init__(self, x=float('inf'), y=float('inf'), b=0):
        self.x = x
        self.y = y
        self.b = b

    def copy(self):
        return PointsCurve(self.x, self.y)

    def isZero(self):
        return self.x > 1e20 or self.x < -1e20

    def negative(self):
        return PointsCurve(self.x, -self.y)

    def dbl(self):
        if self.isZero():
            return self.copy()
        try:
            L = (3 * self.x * self.x + self.b) / (2 * self.y)
        except ZeroDivisionError:
            return PointsCurve()

        x = L * L - 2 * self.x
        return PointsCurve(x, L * (self.x - x) - self.y)

    def add(self, q):
        if self.x == q.x and self.y == q.y:
            return self.dbl()

        if self.isZero():
            return q.copy()

        if q.isZero():
            return self.copy()

        try:
            L = (q.y - self.y) / (q.x - self.x)
        except ZeroDivisionError:
            return PointsCurve()

        x = L * L - self.x - q.x
        return PointsCurve(x, L * (self.x - x) - self.y)

    def __str__(self):
        return "({:.3f}, {:.3f})".format(self.x, self.y)

    def mltdblmltpp(self, n):
        p = self.copy()
        r = PointsCurve()
        i = 1
        while i <= n:
            if i & n:
                r = r.add(p)
            p = p.dbl()
            i <<= 1
        return r


def show(s, p):
    print(s, "Zero" if p.isZero() else p)


def from_y(y):
    n = y * y - 7
    x = n ** (1. / 3) if n >= 0 else -((-n) ** (1. / 3))
    return PointsCurve(x, y)


# demonstrate
x = 2
y = -8
b = -36
curve = PointsCurve(x, y, b)
curve1 = PointsCurve(3, 10, b)
c = curve.add(curve1)
show("", c)

f = Fraction(float(c.y))
print(f)

#show("c = a + b =", f)
