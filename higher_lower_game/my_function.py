from ascii_art import logo
import random
from game_data import data
from replit import clear


def refresh():
    '''
    Clears the console and prints the Higher Lower logo.
    '''
    clear()
    print(logo)


def new_person() -> dict:
    '''
    Returns a person's data from the game data.
    --------
    Returns
        person (dict): person's 'name', 'follower_count', 'description', and 'country' in a dictionary.
    '''
    person = random.choice(data)
    return person


def check_answer(guess: str, person_a: dict, person_b: dict) -> int:
    '''
    Takes the player's guess, person A data, and person B data, 
    and checks if the player guess is correct or not.
    -------------
    Args
        guess (str): player's guess: 'a' or 'b'.
        person_a (dict): dictionary with data for person A
        person_b (dict): dictionary with data for person B
    Returns
        answer (bool): correct or not correct
    '''
    answer = False
    if guess == 'a':
        answer = person_a['follower_count'] > person_b['follower_count']
    elif guess == 'b':
        answer = person_b['follower_count'] > person_a['follower_count']
    return answer
