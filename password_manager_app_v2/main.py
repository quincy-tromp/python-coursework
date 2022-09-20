import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
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
    new_entry = {website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as f:
                # Reading old data
                data = json.load(f)
                # Updating old data with new data
                data.update(new_entry)
        except FileNotFoundError:
            with open("data.json", mode="w") as f:
                json.dump(new_entry, f, indent=4)
        else:
            with open("data.json", mode="w") as f:
                # Saving updated data
                json.dump(data, f, indent=4)
        finally:
            website_input.delete(0, "end")
            password_input.delete(0, "end")
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists")
    finally:
        website_input.delete(0, "end")
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
website_input = tk.Entry(width=20)
website_input.grid(column=2, row=2)
website_input.focus()
username_input = tk.Entry(width=35)
username_input.grid(column=2, row=3, columnspan=2)
username_input.insert(0,"quincy@gmail.com")
password_input = tk.Entry(width=20)
password_input.grid(column=2, row=4)

# Buttons
search_button = tk.Button(text="Search", width=11, command=find_password)
search_button.grid(column=3, row=2)
generate_password_button = tk.Button(text="Generate Password", width=11, command=generate_password)
generate_password_button.grid(column=3, row=4)
add_button = tk.Button(text="Add", width=33, command=save)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()