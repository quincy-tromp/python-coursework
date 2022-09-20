from ascii_art import logo
from replit import clear

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

def calculate():
    '''Basic arithmetic calculator. Takes two numbers and an operation, 
    performs the operation on the numbers, and displays the answer of this calculation.
    '''
    print(logo)

    num1 = float(input("What's the first number: "))
    for symbol in operations:
            print(symbol)

    calculating = True
    while calculating:
        
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number: "))
        calc_function = operations[operation] 
        answer = calc_function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}," + " " + 
        "or type 'n' to start a new calculation.: ") == 'y':
            num1 = answer
        else:
            calculating = False
            clear()
            calculate()

calculate()