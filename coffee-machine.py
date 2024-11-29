MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}

profit = 0


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """returns value of coins inserted"""
    print("please insert coins:")
    quarter = int(input("how many quarters?: ")) * 0.25
    dime = int(input("how many dimes?: ")) * 0.10
    nickel = int(input("how many nickels?: ")) * 0.05
    penny = int(input("how many pennies?: ")) * 0.01
    total = quarter + dime + nickel + penny
    return total


def is_transaction_successful(money_received, drink_cost):
    """return true when the payment is accepted, else false"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is the change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """deduct resources after a drink"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}")


isOn = True

while isOn:
    choice = input("what would you like to have? (latte/espresso/cappuccino):")
    if choice == "off":
        isOn = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
