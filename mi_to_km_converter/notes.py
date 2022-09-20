# *args: Many positional arguments
def add(*args):
    print(args)
    print(type(args))
    print(args[0])
    return sum(args)

result = add(9, 5, 3, 8, 7, 2, 2)
print(result)

# **kwargs: Many keyworded arguments
def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)
print(my_car.color)

# Tkinter
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    label.config(text=new_text)

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label 
label = Label(text="I am a label", font=("Arial", 24, "bold"))
label["text"] = "new text"
label.config(text="New text")
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# New Button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=20)
input.grid(column=3, row=3)

window.mainloop()