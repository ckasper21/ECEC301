### Chris Kasper ECE-C301 Lab Week 2 ###
#Declaring Class
class Person(object):
    def __init__(self,name,byear):
        self.name=name
        self.byear=byear
    def getName(self):
        print self.name
    def getBirthYear(self):
        print self.byear
    def __repr__(self):
        return ' Person \n Name:%s \n Birth Year:%i' % (self.name,self.byear)
                 
class Student(Person):
    def __init__(self,name,byear,major=None,gpa=None):
        super(Student,self).__init__(name,byear)
        if major is not None:
            self.major=major
        else:
            self.major='N/A'
        if gpa is not None:
            self.gpa=gpa
        else:
            self.gpa=0
    def getMajor(self):
        return self.gpa

    def getGPA(self):
        return self.gpa

    def setMajor(self,major):
        self.major=major

    def setGPA(self,gpa):
        self.gpa=gpa
    def __repr__(self):
        return 'Student \n Name:%s \n Birth Year:%i \n Major:%s \n GPA:%.2f' % (self.name,self.byear,self.major,self.gpa)
                

class Instructor(Person):
    def __init__(self,name,byear,salary=None):
        super(Instructor,self).__init__(name,byear)
        if salary is not None:
            self.salary=salary
        else:
            self.salary=0
    def setSalary(self,x):
        self.salary=x
    def getSalary(self):
        return self.salary
    def __repr__(self):
        return ' Instructor \n Name:%s \n Birth Year:%i \n Salary:$%s' % (self.name,self.byear,self.salary)
    
        
