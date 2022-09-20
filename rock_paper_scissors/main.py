#ROCK, PAPER, SCISSOR
import random

play = True
while play == True:
    choices = ["Rock", "Paper", "Scissor"]
    results = ["Win", "Lose", "Draw"]

    rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        ''')
    paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
        ''')
    scissor = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
        ''')

    hand_signals = [rock, paper, scissor]

    user_choice = int(input('\nWhat do you choose?' + ' ' +
    f'Type "0" for Rock, "1" for Paper or "2" for Scissor.\n'))
    print(f"\nYou chose: {choices[user_choice]}\n" + 
    hand_signals[user_choice])

    computer_choice = random.randint(0, len(choices)-1)
    print(f"\nComputer chose: {choices[computer_choice]}\n" + 
    hand_signals[computer_choice])

    if user_choice == computer_choice:
        result = "It's a Draw."
    else:
        if (user_choice == 0 and computer_choice == 2) \
        or (user_choice == 1 and computer_choice == 0) \
        or (user_choice == 2 and computer_choice == 1):
            result = "You Win!"
        else:
            result = "You Lose."
    print(result)
    
    play_again = input('\nDo you want to continue? (y/n): ').lower()
    if play_again == "n":
        play = False
        print("Goodbye.")
