import turtle as t
import random

t.colormode(255)
timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.speed('fastest')
timmy.pensize(10)

def draw_square():
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)
# draw_square()

def draw_dashed_line():
    for _ in range(10):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()
# draw_dashed_line()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b,)
    return random_color

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)
        timmy.color(random_color())
# for num in range(3, 11):
#     draw_shape(num)

def random_walk(steps,step_size):
    directions = [0, 90, 180, 270]
    while steps > 0:
        timmy.color(random_color())
        timmy.forward(step_size)
        timmy.setheading(random.choice(directions))
        steps -= step_size
# random_walk(5000, 25)

def spirograph(gap_size):
    timmy.pensize(3)
    for _ in range(int(360 / gap_size)):
        timmy.color(random_color())
        timmy.setheading(timmy.heading() + gap_size)
        timmy.circle(100)
spirograph(5)


screen = t.Screen()
screen.exitonclick()