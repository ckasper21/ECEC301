### Chris Kasper ECE-C301 Lab Week 2 ###

from Person import Person
from Person import Student
from Person import Instructor

## Testing Person ##

person1=Person('Adam',1996)
person1.getName
person1.getBirthYear
print person1
print '\n'


## Testing Student ##

student1=Student('Chris',1995,'Computer Engineering', 3.30)
student1.getName()
student1.getBirthYear()
student1.getMajor()
student1.getGPA()
print student1

print '\n Changing major and gpa \n'

student1.setMajor('Business')
student1.setGPA(4.0)
print student1
print '\n'

## Testing Instructor

instructor1=Instructor('Mr.Smith',1980)
instructor1.getName()
instructor1.getBirthYear()
instructor1.getSalary()
print instructor1
print '\n Changing Salary\n'
instructor1.setSalary(400000)
instructor1.getSalary()
print instructor1
