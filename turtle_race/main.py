from turtle import Turtle, Screen
import random as r

screen = Screen()
screen.setup(width=500, height=400)
colors = ['purple', 'orange', 'red', 'blue', 'green', 'yellow']
y_positions = [-60, -36, -12, 12, 36, 60]
all_turtles = []

for turtle_index in range(6):
    turtle = Turtle(shape='turtle')
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(turtle)

race_on = False
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ').lower()
print(user_bet)
if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            turtle.hideturtle()
            turtle.goto(x=-200, y=0)
            turtle.color('black')
            turtle.pensize(100)
            if winning_color == user_bet:
                turtle.write(f"You won! The {winning_color} turtle is the winner!")
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                turtle.write(f"You've lost. The {winning_color} turtle is the winner.")
                print(f"You've lost. The {winning_color} turtle is the winner.")
        turtle.forward(r.randint(0, 10))

screen.exitonclick()