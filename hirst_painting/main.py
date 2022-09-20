import colorgram
import turtle as t
import random

t.colormode(255)
colors = colorgram.extract('notes/image.jpg', 12)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))
rgb_colors.pop(0)
rgb_colors.pop(7)

def draw_hirst_painting(horizontal, vertical, color_list):
    timmy = t.Turtle()
    timmy.hideturtle()
    timmy.speed('fast')
    timmy.penup()
    timmy.goto(-250, -250)
    coord_y = -250
    for _ in range(vertical):
        for _ in range(horizontal):
            timmy.dot(20, random.choice(color_list))
            timmy.forward(50)
        coord_y += 50
        timmy.goto(-250, coord_y)

draw_hirst_painting(10, 10, rgb_colors)

screen = t.Screen()
screen.exitonclick()