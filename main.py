from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

#Turn the machine on (start the while loop)
is_on = True 

while is_on: 
    coffee_options = menu.get_items()
    choice = input(f"What would you like? ({coffee_options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice in ("espresso", "latte", "cappuccino"):
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print("Please check your spelling, thank you!")