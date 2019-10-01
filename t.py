from turtle import *

myTurtle = Turtle()
screen = myTurtle.getscreen()

myTurtle.forward(50)

def writeName():
	name = screen.textinput("name box","What is your name?")
	myTurtle.write(name, move=True, align="left", font=("Arial",30,"normal"))
	screen.listen()

def Forward():
	myTurtle.forward(10)
def Right():
	myTurtle.right(90)
def Left():
	myTurtle.left(90)
def Backward():
	myTurtle.backward(10)
def Reset():
  myTurtle.reset()

def Home():
  myTurtle.home()

def Color1():
  myTurtle.pencolor("red")

def Color2():
  myTurtle.pencolor("green")

def Color3():
  myTurtle.pencolor("blue")

def Dot():
  myTurtle.dot(15, "yellow")

def penUp():
  myTurtle.penup()

def penDown():
  myTurtle.pendown()

def sizeUp():
  myTurtle.pensize(10)

def sizeDown():
  myTurtle.pensize(1)




screen.onkey(writeName, "w")

screen.onkey(Forward, "Up")
screen.onkey(Right, "Right")
screen.onkey(Left, "Left")
screen.onkey(Backward, "Down")
screen.onkey(Reset, "r")
screen.onkey(Home, "h")
screen.onkey(Color1, "1")
screen.onkey(Color2, "2")
screen.onkey(Color3, "3")
screen.onkey(Dot, "d")
screen.onkey(penUp, "u")
screen.onkey(penDown, "n")
screen.onkey(sizeUp, "f")
screen.onkey(sizeDown, "j")



screen.listen()

screen.mainloop()