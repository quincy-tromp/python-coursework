from ascii_art import logo
from my_function import deal_card, calculate_score, result   
from replit import clear

print(logo)
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if play == 'y': 
    game_on = True
while game_on:
    clear()
    print(logo)

    player_hand = []
    computer_hand = []
    for _ in range(2):
        deal_card(player_hand)
        deal_card(computer_hand)

    game_over = False
    while not game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}\n")
        print(f"Computer's first card: {computer_hand[0]}\n")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            another_card = input("Type 'y' to hit, type 'n' to stand: ").lower()
            clear()
            print(logo)
            if another_card == 'y':
                deal_card(player_hand)
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        deal_card(computer_hand)
        computer_score = calculate_score(computer_hand)
    
    clear()
    print(logo)
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"\nComputer's final hand: {computer_hand}, computer's final score: {computer_score}\n")
    print(result(player_score, computer_score))

    play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
    if play_again == 'n':
        game_on = False
        print("Goodbye")