import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

data = pd.read_csv("us-states-game-start/50_states.csv")
states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another state's name?").rstrip().title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(answer_state)

