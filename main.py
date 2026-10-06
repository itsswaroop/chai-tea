MENU = {
    "masala": {
        "ingredients": {"water": 100, "milk": 100, "tea": 6},
        "cost": 20,
    },
    "ginger": {
        "ingredients": {"water": 100, "milk": 120, "tea": 6},
        "cost": 25,
    },
    "cutting": {
        "ingredients": {"water": 50, "milk": 50, "tea": 4},
        "cost": 10,
    },
}

profit = 0
resources = {
    "water": 500,
    "milk": 400,
    "tea": 100,
}

# Friendly names for messages (e.g. "Sorry, there is not enough tea leaves.")
LABELS = {"water": "water", "milk": "milk", "tea": "tea leaves"}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {LABELS[item]}.")
            return False
    return True


def read_count(coin_name):
    """Asks for a number of coins and returns a whole number (0 if input is invalid)."""
    try:
        return max(0, int(input(f"How many ₹{coin_name} coins?: ")))
    except ValueError:
        print("Invalid number, counting it as 0.")
        return 0


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = read_count(10) * 10
    total += read_count(5) * 5
    total += read_count(2) * 2
    total += read_count(1) * 1
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = money_received - drink_cost
        if change > 0:
            print(f"Here is ₹{change} in change.")
        return True
    print("Sorry, that's not enough money. Money refunded.")
    return False


def make_chai(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} chai. Enjoy! ☕")


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Tea leaves: {resources['tea']}g")
    print(f"Money: ₹{profit}")


is_on = True

while is_on:
    choice = input("What would you like? (masala/ginger/cutting): ").strip().lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    elif choice in MENU:
        drink = MENU[choice]
        print(f"{choice.capitalize()} chai costs ₹{drink['cost']}.")
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_chai(choice, drink["ingredients"])
    else:
        print("Sorry, that is not on the menu. Please choose masala, ginger or cutting.")
