#TODO: 
# Create a letter using starting_letter.txt for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt") as l:
    text = l.read()

with open("Input/Names/invited_names.txt") as n:
    invitees = n.read()

names = invitees.split("\n")

for name in names:
    letter = open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w")
    letter.write(text.replace(PLACEHOLDER, name))
    letter.close()