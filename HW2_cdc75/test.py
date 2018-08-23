### Chris Kasper ECE-C301 HW Week 2 ###
from fraction import Fraction

# Adding test fractions
x1=Fraction(2,4)
print 'x1 = %s ' % str(x1)
x2=Fraction(3,9)
print 'x2 = %s ' % str(x2)
x3=Fraction(12,13)
print 'x3 = %s ' % str(x3)
x4=Fraction(1,5)
print 'x4 = %s ' % str(x4)
# Testing add
result=x1+x2
print 'x1+x2= %s ' % str(result)
# Testing sub
result=x3-x2
print 'x3-x2= %s ' % str(result)
# Testing eq
result=x1==x1
print 'Does x1 equal x1? eq returns %s' % str(result)
result=x2==x1
print 'Does x2 equal x1? eq returns %s' % str(result)
# Testing lt
result=x1<x4
print 'Is x1 less than x4? lt returns %s' % str(result)
# Testing ne
result=x1!=x1
print 'Does x1 not equal x1? ne returns %s' % str(result)
result=x3!=x4
print 'Does x3 not equal x4? ne returns %s' % str(result)
# Testing le
result=x1<=x1
print 'Is x1 less than or equal to x1? le returns %s' % str(result)
# Testing gt
result=x4>x1
print 'Is x4 greater than x1? gt returns %s' % str(result)
# Testing ge
result=x3>=x1
print 'Is x3 greater than x1? ge returns %s' % str(result)
# Testing float
print 'x1 in decimal form is %f ' % float(x1)
print 'x2 in decimal form is %f ' % float(x2)
# Testing repr

