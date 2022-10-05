def nsdfunc(a, b):
    while a*b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a + b


class Rational:
    def __init__(self, num=1,  den=1):
        self.num = int(num / nsdfunc(num, den))
        self.den = int(den / nsdfunc(num, den))

    def drob(self):
        print(f'{self.num}/{self.den}')

    def ration(self):
        print(self.num/self.den)


drib = Rational()
drib.drob()
drib.ration()
drib1 = Rational(4, 16)
drib1.drob()
drib1.ration()
