import tkinter as tk
import pandas as pd
import random 

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pd.read_csv("data/cards_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    cards_to_learn = data.to_dict(orient="records")

# ------------------------- GENERATE NEW CARD --------------------------------#
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(cards_to_learn)
    canvas.itemconfig(card_background, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)

# ----------------------------- FLIP CARD ------------------------------------#
def flip_card():
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

# --------------------------- SAVE PROGRESS ----------------------------------#
def is_known():
    global cards_to_learn
    cards_to_learn.remove(current_card)
    data = pd.DataFrame(cards_to_learn)
    data.to_csv("data/cards_to_learn.csv", index=False)
    next_card()

# ----------------------------- UI SETUP -------------------------------------#
window = tk.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_card)

# Canvas
card_front_image = tk.PhotoImage(file="images/card_front.png")
card_back_image = tk.PhotoImage(file="images/card_back.png")
canvas = tk.Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

# Buttons
cross_image = tk.PhotoImage(file="images/wrong.png")
unknown_button = tk.Button(image=cross_image, highlightthickness=0, borderwidth=0, command=next_card)
unknown_button.grid(column=1, row=2)
check_image = tk.PhotoImage(file="images/right.png")
known_button = tk.Button(image=check_image, highlightthickness=0, borderwidth=0, command=is_known)
known_button.grid(column=2, row=2)

next_card()

window.mainloop()