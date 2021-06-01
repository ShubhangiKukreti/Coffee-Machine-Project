MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
ask_again = True


# TODO: 3.Check resources
def check_resources(choice):
    """
    Checks the resources like milk, water etc required to make coffee before making coffee for the customer.
    :param choice: user input about the kind of coffee
    :return: boolean value True if resources are there otherwise False
    """
    if MENU[choice]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    elif MENU[choice]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


# TODO: 4. Process Coins
def process_coins():
    """
    Processes the coins entered by the customer and calculates the total value for the coins they have entered.
    :return: sum of the value of coins entered
    """
    print("Please Insert Coins.")
    quarter = float(input(print("How many quarters?")))
    dimes = float(input(print("How many dimes?")))
    nickels = float(input(print("How many nickels?")))
    pennies = float((input(print("How many pennies?"))))
    total_coin_cost = quarter * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total_coin_cost


# print(process_coins(user_input))
# TODO: 5. Check successful transaction?
def transaction(choice):
    """
    Check if the transaction is successful by comparing the money entered by a customer against the value of th coffee ordered.
    :param choice: user input
    :return: True if the money entered by the customer is more or equal to the cost of coffee
    """
    cost = process_coins()
    if cost > MENU[choice]["cost"]:
        change = cost - MENU[choice]["cost"]
        print(f"Here is the ${change} in change.")
        return True
    elif cost < MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif cost == MENU[choice]["cost"]:
        return True


def update_resources(choice):
    """
    Updates the resources after a coffee has been made.
    :param choice: user input
    :return: None
    """
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    resources["money"] += MENU[choice]["cost"]


# TODO: 6. Make Coffee
def make_coffee():
    """
    Takes input from the user and only makes coffee if all conditions are satisfied. Can also check resources or turn the coffee machine off.
    :return: None
    """
    while ask_again:
        user_input = input(print("What would you like? Espresso, Cappuccino, Latte.\n ")).lower()
        if user_input == "off":
            exit()
        elif user_input == "report":
            print(resources)
        else:
            if check_resources(user_input) and transaction(user_input):
                update_resources(user_input)
                print(f"Enjoy your {user_input}")


make_coffee()
