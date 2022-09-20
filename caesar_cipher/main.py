from ascii_art import logo
from my_function import caesar_cipher

print(logo)
        
go = True
while go:  
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(direction=direction, text=text, shift=shift)

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if again == "no":
        go = False
        print("Goodbye")