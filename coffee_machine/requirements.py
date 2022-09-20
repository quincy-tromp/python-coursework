#REQUIREMENTS
#----------

#0. General
#----------
# Makes 3 hot flavours - Espresso, Latte, and Cappuccino.
# Espresso ($1.50): 50ml water, 18g coffee
# Latte ($2.50): 200ml water, 24g coffee, 150ml milk
# Cappuccino ($3.00): 250ml water, 24g coffee, 100ml milk

# The coffee machine has some resources that it has to manage. 
# It starts out with 300ml water, 200ml milk, 100g coffee

# Coin operated: 
    # Penny ($0.01)
    # Nickel ($0.05) 
    # Dime ($0.10)
    # Quarter ($0.25)

# Starts off with the prompt -> 'What would you like? (espresso/latte/cappuccino): ' 

# Turn off the Coffee Machine by entering 'off' into the prompt.

#1. Print report
#----------
# Needs to be able to print a report to tell us what resources it has left (how much water, milk, coffee).

# If you input 'report' into the prompt, it will return how much water, milk, coffee, money is in the machine ->
    # 'Water: 300ml'
    # 'Milk: 200ml'
    # 'Coffee: 100g'
    # 'Money: $0'

#2. Check resources sufficient?
#----------
# Needs to be able to check if the resources are sufficient when a user orders a drink.

# When you input one of the 3 options ('espresso', 'latte', 'cappuccino') in the prompt,
# it will check if there are enough resource (water/milk/coffee) for ordered drink.
# If there is sufficient resources, it will start processing coins.
# If there is NOT sufficient resources, it will tell you which resource specifically there is not enough of ->
    # 'Sorry, there is not enough water.'

#3. Process coins
#----------
# Needs to be able to process coins.

# If there is sufficient resources, it will start processing the coins -> 'Please insert coins.'
# And it will ask how many quarteres, dimes, nickels, and pennies you inserted, one for one ->
    # 'How many quarters?: '
    # 'How many dimes?: '
    # 'How many nickels?: '
    # 'How many pennies?: '

# After you inputed how many coins you inserted, it will compare the sum against the cost.
# If you inserted more than enough, it will return your change -> 'Here is $2.42 in change.' 
# If you didn't insert enough coins, it will refund your money -> 'Sorry, that's not enough money. Money refunded.'

# Finally, after you inserted (more than) enough coins, it will start the transaction process

#4. Check transaction successful?
#----------
# Needs to able to check if transaction was successful.

# After you've payed, it will check if the payment was successful before making the coffee.


#5. Make coffee
#----------
# Makes coffee.

# Makes and gives you your coffee -> 'Here is your latte *coffee-emoji* Enjoy!'

# After it's made your coffee, it will update the resource inventory to reflect 
# the current resource quantities.