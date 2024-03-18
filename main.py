from data import MENU, resources


def print_report():
    """Prints input resources, each in new line."""
    machine_water = resources['water']
    machine_milk = resources['milk']
    machine_coffee = resources['coffee']
    machine_money = resources['money']
    print(f"Water: {machine_water}")
    print(f"Milk: {machine_milk}")
    print(f"Coffee: {machine_coffee}")
    print(f"Money: ${machine_money}")


def check_resources(chosen_drink):
    """Returns True if resources are sufficient for the chosen drink, else returns False and prints insufficient
    resources."""
    drink_water = MENU[chosen_drink]['ingredients']['water']
    drink_milk = MENU[chosen_drink]['ingredients']['milk']
    drink_coffee = MENU[chosen_drink]['ingredients']['coffee']
    machine_water = resources['water']
    machine_milk = resources['milk']
    machine_coffee = resources['coffee']
    if machine_water < drink_water:
        print(f"Sorry, there is not enough water.")
    if machine_milk < drink_milk:
        print(f"Sorry, there is not enough milk.")
    if machine_coffee < drink_coffee:
        print(f"Sorry, there is not enough coffee.")
    return machine_water > drink_water and machine_milk > drink_milk and machine_coffee > drink_coffee


def insert_coins():
    """Asks user to insert different coins and returns summed value of inserted coins."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    user_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return user_money


def check_successful(user_money, chosen_drink):
    """Checks if user's money is sufficient to buy chosen drink, if able, prints change, adds drink's cost to
    machine money and returns True, else prints user that his money is insufficient and returns False"""
    chosen_drink_cost = MENU[chosen_drink]['cost']
    if chosen_drink_cost > user_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if chosen_drink_cost < user_money:
            change = round(user_money - chosen_drink_cost, 2)
            print(f"Here is ${change} dollars in change.")
        resources['money'] += chosen_drink_cost
        return True


def make_coffee(chosen_drink):
    """Subtracts resources needed to make chosen drink from machine resources and prints <3 words"""
    drink_water = MENU[chosen_drink]['ingredients']['water']
    drink_milk = MENU[chosen_drink]['ingredients']['milk']
    drink_coffee = MENU[chosen_drink]['ingredients']['coffee']
    resources['water'] -= drink_water
    resources['milk'] -= drink_milk
    resources['coffee'] -= drink_coffee
    print(f"Here is your {chosen_drink}. Enjoy!")


def coffee_machine():
    """Starts coffee machine."""
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'off':
        return
    elif user_input == 'report':
        print_report()
        coffee_machine()
    else:
        if check_resources(user_input):
            money = insert_coins()
            if check_successful(money, user_input):
                make_coffee(user_input)
                coffee_machine()
            else:
                coffee_machine()
        else:
            coffee_machine()


# ODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
# a. Check the user’s input to decide what to do next
#user_input = input("What would you like? (espresso/latte/cappuccino): ")
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer

# ODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
#a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
#the machine. Your code should end execution when this happens.
#if user_input == 'off':

# ODO: 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
#if user_input == 'report':
#    print_report(resources)

# ODO: 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
#are_there_resources = check_resources(resources, user_input)
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

# ODO: 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
#money = insert_coins()
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# ODO: 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
#check_succesful
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

# ODO: 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink
coffee_machine()