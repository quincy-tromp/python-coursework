def check_difficulty():
    '''Choose difficulty. Returns the number of attempts.
    '''
    easy_level_attempts = 10
    hard_level_attempts = 5
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return easy_level_attempts
    elif difficulty == "hard":
        return hard_level_attempts

def check_answer(guess: int, answer: int, attempts: int):
    '''Checks answer against guess. Returns the number of attempts remaining.
    '''
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")