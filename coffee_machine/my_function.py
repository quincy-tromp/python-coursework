from ascii_art import logo
from resources_data import MENU


def take_order():
    ''' 
    Takes the customer's order, and then returns the customer's order in lowercase.
    Also displays the logo and menu.
    -------
    Returns
        customer_order (str): customer's order in lowercase
    '''
    print(logo)
    for item in MENU:
        print(f"{item.title()}: $", "{:.2f}".format(MENU[item]['cost']))
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return choice


def report(inventory: list) -> print:
    '''
    Takes the inventory and displays the quantity of each resource, right-aligned.
    ------
    Args
        inventory (list): list with variables that hold the quantity of each resource
    '''
    print(f"Water: {inventory['water']: > 5}")
    print(f"Milk: {inventory['milk'] : > 6}")
    print(f"Coffee: {inventory['coffee'] : > 4}")
    print("Money: ${:<.2f}".format(inventory['money']))


def check_resources(customer_order: str, inventory: list) -> bool:
    '''
    Checks the inventory and returns True or False, there are sufficient resources or not.
    --------
    Args
        customer_order (str): the customer's order (espresso/latte/cappuccino)
        inventory (list): list with variables that hold the quantity of each resource
    Returns
        sufficient_resources (bool): result of the check; True or False
    '''
    sufficient_resources = False

    water_needed = MENU[customer_order]['ingredients'].get('water', 0)
    milk_needed = MENU[customer_order]['ingredients'].get('milk', 0)
    coffee_needed = MENU[customer_order]['ingredients'].get('coffee', 0)
   
    if ((inventory['water'] >= water_needed) and
        (inventory['milk'] >= milk_needed) and
        (inventory['coffee'] >= coffee_needed)):
        sufficient_resources = True

    return sufficient_resources


def not_sufficient_resources(customer_order: str, inventory: list) -> print:
    '''
    Fucntion to be called when there's not enough inventory; 
    displays the resource(s) that there is not enough of.
     --------
    Args
    customer_order (str): the customer's order (espresso/latte/cappuccino)        
    inventory (list): list with variables that hold the quantity of each resource
    '''
    water_needed = MENU[customer_order]['ingredients'].get('water', 0)
    milk_needed = MENU[customer_order]['ingredients'].get('milk', 0)
    coffee_needed = MENU[customer_order]['ingredients'].get('coffee', 0)
    
    if inventory['water'] < water_needed:
        print("Sorry, there is not enough water.")
    if inventory['milk'] < milk_needed:
        print("Sorry, there is not enough milk.")
    if inventory['coffee'] < coffee_needed:
        print("Sorry, there is not enough coffee.")


def process_coins(customer_order: str) -> float:
    '''
    Gathers the cost of the customer order, and processes the payment.
    If the money received is not enough, the money is refunded. Else the payment is processed 
    and the change is calculated. Returns the payment amount accepted.
    ---------
    Args
        customer_order (str): the customer's order (espresso/latte/cappuccino)
    Returns
        payment (float): the total money accepted, with a 2 point precision
    '''
    print("Please insert coins.")

    drink_cost = MENU[customer_order]['cost']

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    money_received = ((quarters * 0.25) +
            (dimes * 0.10) +
            (nickels * 0.05) + 
            (pennies * 0.01))
    
    if money_received < drink_cost:
        payment = 0
    elif money_received > drink_cost:
        change = money_received - drink_cost
        payment = money_received - change
        print("Here is ${:.2f} in change.".format(change))
    else:
        payment = money_received

    return float(payment)


def transact(payment: float) -> bool:
    '''
    Returns if the transaction was successful or not.
    -----
    Args
        payment (float): the total money processed, with a 2 point precision
    '''
    transaction_successful = False
    if payment > 0:
        transaction_successful = True  
    return transaction_successful


def make_order(customer_order: str) -> print:
    '''
    Displays the order made.
    '''
    print(f"Here is your {customer_order} ☕ Enjoy!")


def update_resource_quantities(customer_order: str, payment: float, inventory: list) -> list:
    '''
    Updates the current inventory of all resources, after a drink is made.
    ----
    Args
        customer_order (str): the customer's order (espresso/latte/cappuccino)
        payment (float): the total money processed, with a 2 point precision
        inventory (list): list with variables that hold the quantity of each resource
    '''
    water_needed = MENU[customer_order]['ingredients'].get('water', 0)
    milk_needed = MENU[customer_order]['ingredients'].get('milk', 0)
    coffee_needed = MENU[customer_order]['ingredients'].get('coffee', 0)
    inventory['water'] -= water_needed
    inventory['milk'] -= milk_needed
    inventory['coffee'] -= coffee_needed
    inventory['money'] += payment
    return inventory
