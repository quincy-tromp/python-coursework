from replit import clear
import my_function as mf
from resources_data import resources
from time import sleep

machine_on = True
inventory = resources
inventory['money'] = 0

while machine_on:
    customer_order = mf.take_order()
    if customer_order == 'report':
        mf.report(inventory)
        sleep(7)
    elif customer_order == 'latte' or customer_order == 'espresso' or customer_order == 'cappuccino':
        sufficient_resources = mf.check_resources(customer_order, inventory)
        if sufficient_resources:
            payment = mf.process_coins(customer_order)
            transaction_successful = mf.transact(payment)
            if transaction_successful:
                mf.make_order(customer_order)
                mf.update_resource_quantities(customer_order, payment, inventory)
                sleep(3.5)
            else:
                print("Sorry, that's not enough money. Money refunded.")
                sleep(3.5)
        else:
           mf.not_sufficient_resources(customer_order, inventory)
           sleep(3.5)
    elif customer_order == 'off':
        machine_on = False
    else:
        print(f"Sorry, there is no {customer_order}.")
        sleep(3.5)
    clear()



