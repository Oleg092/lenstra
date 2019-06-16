import sys


class Fractions:

    def __init__(self, a, b):
        try:
            a = int(a)
            b = int(b)
        except Exception as e:
            print(e)
            print("invalid value for fractions, please get int value")
            sys.exit()
        self.a = a
        self.b = b

    def reductionFract(self):
        d = self.gcd()
        while d != 1:
            self.a = self.a // d
            self.b = self.b // d
            d = self.gcd()

    def gcd(self):
        a = self.a
        b = self.b
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

    def getA(self):
        return self.a

    def getB(self):
        return self.b


if __name__ == '__main__':
    print("get numerator")
    a = input()
    print("get denominator")
    b = input()
    fractions = Fractions(a, b)
    fractions.reductionFract()
    print(str(fractions.getA()) + "/" + str(fractions.getB()))
