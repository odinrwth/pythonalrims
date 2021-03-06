class Fraction(object):

    def __init__(self,top,bottom):
        if isinstance(top,int) and isinstance(bottom,int):
            common = gcd(top,bottom)
            self.num = top//common
            self.den = bottom//common
        else:
            raise RuntimeError("Numerator or denominator is not a valid integer")

    def __str__(self):
        return str(self.num)+'/'+str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

    def __sub__(self,otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

    def __mul__(self,otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

    def __truediv__(self,otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        return Fraction(newnum,newden)

    def __eq__(self,otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = self.den * otherfraction.num
        return (firstnum == secondnum)

    def __ne__(self,otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = self.den * otherfraction.num
        return (firstnum != secondnum)

    def __lt__(self,otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = self.den * otherfraction.num
        return (firstnum < secondnum)

    def __le__(self,otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = self.den * otherfraction.num
        return (firstnum <= secondnum)

    def __gt__(self,otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = self.den * otherfraction.num
        return (firstnum > secondnum)

    def __ge__(self,otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = self.den * otherfraction.num
        return (firstnum >= secondnum)

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n
