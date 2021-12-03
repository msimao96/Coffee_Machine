from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = MoneyMachine()
coffee_machine = CoffeeMaker()
products = Menu()

wants_more = True

while wants_more:
    drinks_in_menu = products.get_items()
    drink_chosen = input(f"What would you like? ({drinks_in_menu}): ")
    if drink_chosen == "off":
        wants_more = False
    elif drink_chosen == "report":
        coffee_machine.report()
        machine.report()
    else:
        drink = products.find_drink(drink_chosen)

        if coffee_machine.is_resource_sufficient(drink) and machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
