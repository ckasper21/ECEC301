### Chris Kasper ECE-C301 Project 2- Spirograph ###
## Declaring class
import turtle
from math import cos
from math import sin
from math import pi
from math import radians
from fractions import gcd

class Spirograph(object):
    def __init__(self,R):
        self.t=0
        self.R=R
        self.r=0
        self.l=0 #l will get set to d/r

    def setSmallCircle(self,r):
        self.r=r

    def setPen(self,l,color):
        self.l=l
        self.color=color

    def draw(self): # Draws the spirograph
        turtle.home()
        turtle.pencolor(self.color)
        turtle.speed(0) # makes speed quick
        revs=int(self.r / gcd(self.r,self.R))
        k=self.r/float(self.R)
        theta=range(0,(360*revs)+1)
        for i in theta:
            theta[i]=radians(theta[i])
        for j in range(len(theta)):
            if j==0:
                turtle.penup()
                Px=self.R*((1-k)*cos(theta[j])+self.l*k*cos(((1-k)/k)*theta[j]))
                Py=self.R*((1-k)*sin(theta[j])-self.l*k*sin(((1-k)/k)*theta[j]))
                turtle.goto(Px,Py)
                turtle.pendown()
            else:
                Px=self.R*((1-k)*cos(theta[j])+self.l*k*cos(((1-k)/k)*theta[j]))
                Py=self.R*((1-k)*sin(theta[j])-self.l*k*sin(((1-k)/k)*theta[j]))
                turtle.goto(Px,Py)
        turtle.penup()
        turtle.hideturtle()

    def clear(self): # Clears turtle window
        turtle.reset()

    def pause(self):
        raw_input('Press any key to continue')

    def close(self): # Closes the turtle window
        turtle.bye()

if __name__=="__main__":
    ans='y'
    while ans=='y':
        print 'Lets make a spirograph!'
        print '-----------------------'
        R=float(raw_input('Enter the radius of the big circle: '))
        r=float(raw_input('Enter the radius of the small circle: '))
        l=float(raw_input('Pick a decimal between 0 and 1: '))
        color=raw_input('Pick a color: ')
        new=Spirograph(R)
        new.setSmallCircle(r)
        new.setPen(l,color)
        new.draw()
        print 'Done!'
        new.pause()
        newpage=raw_input('Do you want a clean piece of paper? y/n  ')
        if newpage=='y':
            new.clear()
            print ' '
            continue
        ans=raw_input('Would you like to create another spirograph? y/n  ')
        if ans=='y':
            print ' '
            continue
        elif ans=='n':
            new.close()
    
    
    
        
