
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

#TODO : REPORT

resources["cash"] = 0

def report():
    return resources

#TODO : CHECK RESOURCES

def check_resources(product):
    for i in resources:
        if MENU[product]["ingredients"][i] > resources[i]:
            return False
        else:
            return True
#TODO : COINS

def calculate_change(q,d,n,p,product):
    quarters = 0.25
    dimes = 0.10
    nickels = 0.05
    pennies = 0.01
    total = q * quarters + d * dimes + n * nickels + p * pennies
    change = 0
    if total == MENU[product]["cost"]:
        return None
    elif total < MENU[product]["cost"]:
        change = total
        return change
    elif total > MENU[product]["cost"]:
        change = total - MENU[product]["cost"]
        return round(change,2)

def coins(q,d,n,p,product):
    quarters = 0.25
    dimes = 0.10
    nickels = 0.05
    pennies = 0.01
    total = q * quarters + d * dimes + n * nickels + p * pennies
    if total < MENU[product]["cost"]:
        return False
    elif total >= MENU[product]["cost"]:
        return True


#TODO : Transaction

def transaction(change, resources_okay, coins_okay,product):
    if resources_okay and coins_okay == True:
        return True
    else:
        return False




def coffee_machine(q,d,n,p,product):
    resources_okay = check_resources(product)
    coins_okay = coins(q,d,n,p,product)
    change = calculate_change(q,d,n,p,product)
    coffee_transaction = transaction(change,resources_okay,coins_okay,product)
    if coffee_transaction == True:
        for i in MENU[product]["ingredients"]:
            resources[i] -= MENU[product]["ingredients"][i]
        resources["cash"] += MENU[product]["cost"]
        return f"Your {product} is ready, your change is {change}, thank you."
    else:
        return "Sorry, insufficient resources or coins"

while True:
    product = str(input("What would you like to drink ? espresso, latte or cappuccino :  "))
    if product == "report":
        print(report())
    else:
        q = int(input("How many quarters : "))
        d = int(input("How many dimes : "))
        n = int(input("How many nickels : "))
        p = int(input("How many pennies : "))
        print(coffee_machine(q,d,n,p,product))