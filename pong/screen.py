from turtle import Screen

TITLE = "PONG"
BACKGROUND_COLOR = "black"
HEIGHT = 600
WIDTH = 900

screen = Screen()
screen.title(TITLE)
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.exitonclick()