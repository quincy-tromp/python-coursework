#Hangman
import random
import ascii_art as hangman
import words as w
from replit import clear

print(hangman.logo)

end_program = False
while end_program == False:
  chosen_word = random.choice(w.words)
  lives = 6

  display = []
  for letter in chosen_word:
    display += "_"

  print(' '.join(display))
  print(hangman.stages[0])

  game_on = True
  already_guessed = []
  while game_on:
    guess = input("\nGuess a letter: ").lower()
    clear()
    if guess in already_guessed:
      print(f"You already guessed {guess}.")
    else:
      already_guessed += guess

      word_length = len(chosen_word)
      for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
          display[position] = letter 
      
      if guess not in chosen_word:
        lives -= 1

      print(hangman.logo)
      print(f"Already guessed: {already_guessed}")
      print(f"Lives remaining: {lives}")
      print("\n")
      print(' '.join(display))
      print(hangman.stages[6 - lives])

    
      
      if "_" not in display:
        game_on = False
        print("You Win!")
        print("\n")
      if lives == 0:
        game_on = False
        print("You lose.")
        print(f"The word was: {chosen_word}")
        print("\n")
  
  play_again = input('Type "quit" to end the game. ')
  if play_again == "quit":
    end_program = True
    print("Goodbye")