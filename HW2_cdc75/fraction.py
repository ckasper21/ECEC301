### Chris Kasper ECE-C301 HW Week 2 ###
#Declaring Class
from fractions import gcd

class Fraction(object):
    def __init__(self,num,den):
        self.num=num
        self.den=den
        self.__simplify()

    def __simplify(self):
        gcd1=gcd(self.num,self.den)
        if gcd1!=1:
            self.num=self.num/gcd1
            self.den=self.den/gcd1


    def __add__(self,y):
        shareden=self.den*y.den
        result=Fraction(self.num*y.den+self.den*y.num,shareden)
        result.__simplify()
        return result

    def __sub__(self,y):
        shareden=self.den*y.den
        result=Fraction(self.num*y.den-self.den*y.num,shareden)
        result.__simplify()
        return result

    def __eq__(self,y):
        fract1=float(self.num)/float(self.den)
        fract2=float(y.num)/float(y.den)
        return fract1==fract2

    def __lt__(self,y):
        fract1=float(self.num)/float(self.den)
        fract2=float(y.num)/float(y.den)
        return fract1<fract2

    def __ne__(self,y):
        fract1=float(self.num)/float(self.den)
        fract2=float(y.num)/float(y.den)
        return fract1!=fract2

    def __le__(self,y):
        fract1=float(self.num)/float(self.den)
        fract2=float(y.num)/float(y.den)
        return fract1<=fract2

    def __gt__(self,y):
        fract1=float(self.num)/float(self.den)
        fract2=float(y.num)/float(y.den)
        return fract1>fract2

    def __ge__(self,y):
        fract1=float(self.num)/float(self.den)
        fract2=float(y.num)/float(y.den)
        return fract1>=fract2

    def __float__(self):
        return float(self.num)/float(self.den)

    def __repr__(self):
        return '%i/%i' % (self.num,self.den)
