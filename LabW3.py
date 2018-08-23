### Chris Kasper ECE-C301 Lab Week 3 ###

from Question import Question
from Question import ChoiceQuestion
from Question import presentQuestion

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
