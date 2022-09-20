def the_winning_bid(bids):
    winning_bid = 0
    winner = ""
    for bidder in bids:
        if bids[bidder] > winning_bid:
            winning_bid = bids[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${winning_bid}")