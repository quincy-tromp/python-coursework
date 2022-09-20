from ascii_art import logo
import random
from my_function import check_difficulty, check_answer

def game():
    '''The Number Guessing Game'''
    print("\n", logo)
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")


    answer = random.randint(1, 100)
    attempts = check_difficulty()

    player_guess = 0
    while player_guess != answer:
        print(f"You have {attempts} remaining to guess the number.")
        player_guess = int(input("Make a guess: "))

        attempts = check_answer(player_guess, answer, attempts)

        if attempts == 0:
            print("You've run out of guesses. You lose.")
            print(f"The number was {answer}.")
            return 
        elif player_guess != answer:
            print("Guess again.")
game()