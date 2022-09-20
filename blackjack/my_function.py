import random

def generate_cards() -> list:   
    '''Generates a pack of cards.
    -------
    Returns
        cards (list): list of all cards in a pack of cards
    '''
    suits = ["♣️", "♦️", "♥️", "♠️"]
    ranks = ["A", 2 , 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    cards = [] 
    for suit in suits:
        for rank in ranks:
            cards.append(f"{rank}{suit}")
    return cards
    
    
def create_deck() -> dict:
    '''Creates a dictionary with cards as keys and the card_values as values.
    ---------
    Returns
        deck (dict): dictionary of cards and their corresponding values
    '''
    cards = generate_cards()
    card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deck = {}
    position = 0
    for card in cards:
        if position > 12: 
            position -= 13
        deck[card] = card_values[position]
        position += 1
    return deck
    

def deal_card(hand: list) -> list:
    '''Appends one card to a list of cards
    ----------
    Args
        hand (list): list of cards in hand
    Returns
        hand (list): Adds one card to the list and returns this list
    '''
    cards = generate_cards()
    random.shuffle(cards)
    hand.append(cards.pop())
    return hand


def calculate_score(hand: list) -> int:
    '''Take a list of cards and returns the score calculated from the cards.
    ---------
    Args
        hand (list): list of cards in hand
    Returns
        score (int): sum of all the cards in a hand
    '''
    deck = create_deck()
    aces = ["A♣️", "A♦️", "A♥️", "A♠️"]
    score = 0
    for card in hand:
        score += deck[card]
    for ace in aces:
        if ace in hand and score > 21:
            score -= 10
    if score == 21 and len(hand) == 2:
        score = 0
    return score 


def result(score1: int, score2: int):
    '''
    Takes two scores and returns who won the game.
    -----------
    Args
        score1 (int): player score 
        score2 (int): computer score
    Return
        (str): you won or you lost
    '''
    if score1 == score2:
        return "--- It's a draw ---"
    elif score1 == 0:
        return "YOU HAVE A BLACKJACK. YOU WIN!!💰💰"
    elif score2 == 0:
        return "Computer has a Blackjack. You lose."
    elif score1 > 21:
        return "You've gone bust. You lose..😔"
    elif score2 > 21:
        return "Computer's gone bust. You win!🤑"
    elif score1 > score2:
        return "You win!🤑"
    else:
        return "You lose..😔"