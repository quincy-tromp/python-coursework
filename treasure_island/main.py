#TREASURE ISLAND
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
play = True
while play:

    greeting = "Welcome to Treasure Island."
    introduction = "Your mission is to find the treasure."
    print(f"{greeting}\n{introduction}")

    choice1 = input('You\'re at a cross road.' + ' ' +
    'Where do you want to go? Type "left" or "right"\n').lower()
    if choice1 == "left":
        choice2 = input('You come to a lake.' + ' ' +
        'There is an island in the middle of the lake.' + ' ' +
        'Type "wait" to wait for a boat.' + ' ' + 
        'Type "swim" to swim across.\n').lower() 
        if choice2 == "wait":
            choice3 = input('You arrive at the island unharmed.' + ' ' + 
            'There is a house with 3 doors.' + ' ' + 
            'One red, one yellow, and one blue.' + ' ' +
            'Which color do you choose?\n').lower()
            if choice3 == "yellow":
                print("You found the treasure! You Win!")
            elif choice3 == "red":
                print("You enter a room full of fire.\nGame over.")
            elif choice3 == "blue":
                print("You enter a room of beasts.\nGame over.")
            else:
                print("Game over.")
        else:
            print("You were attacked by trout.\nGame over.")
    else:
        print("You fell into a hole.\nGame over.")

    play_again = input('Do you want to play again? "Y" or "N"\n').lower()
    if play_again == "n":
        play = False
        print("Goodbye.")
