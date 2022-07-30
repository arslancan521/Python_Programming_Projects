from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True

while is_on:
    options = menu.get_items()
    choice = str(input(f"What would you like to drink : {options}"))
    if choice == "exit":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if money_machine.make_payment(drink.cost) and coffee_maker.is_resource_sufficient(drink):
            coffee_maker.make_coffee(drink)

