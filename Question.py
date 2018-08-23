### Chris Kasper ECE-C301 Lab Week 3 ###
# Declaring Class
class Question(object):
    def __init__(self,question=0,answer=0):
        self.q=question
        self.a=answer
    def setText(self,question):
        self.q=question
    def setAnswer(self,answer):
        self.a=answer
    def display(self):
        print self.q
    def checkAnswer(self,attempt):
        if attempt==self.a:
            print 'Correct!'
        else:
            print 'Wrong!'
            
class ChoiceQuestion(Question):
    def __init__(self,question=0,answer=0):
        super(ChoiceQuestion,self).__init__(question=0,answer=0)
        self.q=question
        self.choices=[]
        self.a=answer

    def addChoice(self,choice,rightorwrong): # Answers are stored in list of lists 
        self.choices=self.choices+[[choice,rightorwrong,0]]
        if rightorwrong==1:
            super(ChoiceQuestion,self).setAnswer(choice)

    # Implemented for WK4 HW
    def __iter__(self):
        index=0
        while index < len(self.choices):
            yield index
            index+=1

    # NEW DISPLAY METHOD FOR WK4 HW
    def display(self):
        print '%s' % self.q
        for i in self:
            print '%i. %s' % (i+1, self.choices[i][0])
            self.choices[i][2]=str(i+1)

    # WK3 LAB DISPLAY METHOD
##    def display(self):
##        super(ChoiceQuestion,self).display() # Calls the Question's display method
##        for i in range(len(self.choices)):
##            print '%i. %s' % (i+1, self.choices[i][0])
##            self.choices[i][2]=str(i+1) #Makes third column for answer choice
        
    def checkAnswer(self,numchoice):
        numchoice=int(numchoice)
        if numchoice > int(self.choices[-1][-1]):
            numchoice=raw_input('Not a valid choice, try again. ')
            self.checkAnswer(numchoice)
        else:
            attempt=self.choices[numchoice-1][0]
            super(ChoiceQuestion,self).checkAnswer(attempt)


#Polymorphic Function
def presentQuestion(Question):
    Question.display()
    attempt=raw_input('What is your answer? If multiple choice, input number. ') or 0
    Question.checkAnswer(attempt)
    
    
## Making Quiz ##
question1=Question()
question1.setText('True or False, I have an iPhone')
question1.setAnswer('True')

question2=ChoiceQuestion()
question2.setText('How old am I?')
question2.addChoice('21',1)
question2.addChoice('20',0)
question2.addChoice('19',0)

question3=ChoiceQuestion()
question3.setText('What major am I?')
question3.addChoice('Computer Engineering',1)
question3.addChoice('Mechanical Engineering',0)
question3.addChoice('Electrical Engineering',0)

question4=Question()
question4.setText('True or False, I like veggies')
question4.setAnswer('False')

question5=Question()
question5.setText('True or False, I have a Mac')
question5.setAnswer('True')

quiz=[question1,question2,question3,question4,question5]
print 'TEST TIME!'
for i in range(len(quiz)):
    presentQuestion(quiz[i])
    print' '
