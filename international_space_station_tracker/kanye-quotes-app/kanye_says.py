import tkinter as tk
import requests

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text=data["quote"])

window = tk.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Canvas
canvas = tk.Canvas(width=300, height=414)
quote_box = tk.PhotoImage(file="background.png")
canvas.create_image(150, 207, image=quote_box)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"))
canvas.grid(column=1, row=1)

# Button
kanye = tk.PhotoImage(file="kanye.png")
kanye_button = tk.Button(image=kanye, command=get_quote, highlightthickness=0)
kanye_button.grid(column=1, row=2)

get_quote()

window.mainloop()