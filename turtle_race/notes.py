#ETCH A SKETCH
from turtle import Turtle, Screen

squirtle = Turtle()

def move_forward():
    squirtle.forward(10)

def move_backward():
    squirtle.backward(10)

def counter_clockwise():
    squirtle.left(10)

def clockwise():
    squirtle.right(10)

def clear():
    squirtle.clear()
    squirtle.penup()
    squirtle.home()
    squirtle.pendown()

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()