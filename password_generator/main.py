#PASSWORD GENERATOR
import random

greeting = "\nWelcome to the PyPassword Generator!"
print(greeting)

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
'''
import string
letters = []
for letter in string.ascii_uppercase:
    letters.append(letter)
for letter in string.ascii_lowercase:
    letters.append(letter)
numbers = []
for number in range(0, 10):
    numbers.append(str(number))
'''

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

password_list = []
for letter in range(nr_letters + 1):
    password_list.append(random.choice(letters))
for number in range(nr_numbers + 1):
    password_list.append(random.choice(numbers))
for symbol in range(nr_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for character in password_list:
    password += character

print(f"Here is your password: {password}")
