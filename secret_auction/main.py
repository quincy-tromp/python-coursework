from ascii_art import logo, gavel
from replit import clear
from my_function import the_winning_bid

print(logo)
print("Welcome to the Secret Auction program.")

bids = {}
bidding = True
while bidding:
    name = input("What is your name?: ")
    amount = int(input("What is your bid?: $"))
    bids[name] = amount
    
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
    clear()
    if more_bidders == 'no':
        bidding = False
        print(gavel)
        the_winning_bid(bids=bids)