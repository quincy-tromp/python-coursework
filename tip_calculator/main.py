#TIP CALCULATOR
greeting = "\nWelcome to the tip calculator!"
print(greeting)

bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

split_bill = bill / people
tip_percentage = tip / 100 + 1
bill_per_person = round(split_bill * tip_percentage , 2)
message = f"Each person should pay: ${bill_per_person}"

print(message)
