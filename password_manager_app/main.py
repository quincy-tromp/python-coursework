import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():  
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm' 
            , 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 
            , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M' 
            , 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                            f"\nUsername: {username} "
                                                            f"\nPassword: {password} "
                                                            f"\nIs it ok to save?")
    if is_ok:
        with open("passwords.txt", mode="a") as f:
            f.write(f"{website} | {username} | {password}\n")
            website_input.delete(0, "end")
            password_input.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=1)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(column=1, row=2)
username_label = tk.Label(text="Email/Username:")
username_label.grid(column=1, row=3)
password_label = tk.Label(text="Password:")
password_label.grid(column=1, row=4)

# Entries
website_input = tk.Entry(width=35)
website_input.grid(column=2, row=2, columnspan=2)
website_input.focus()
username_input = tk.Entry(width=35)
username_input.grid(column=2, row=3, columnspan=2)
username_input.insert(0,"quincy@gmail.com")
password_input = tk.Entry(width=20)
password_input.grid(column=2, row=4)

# Buttons
generate_password_button = tk.Button(text="Generate Password", width=11, command=generate_password)
generate_password_button.grid(column=3, row=4)
add_button = tk.Button(text="Add", width=33, command=save)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()