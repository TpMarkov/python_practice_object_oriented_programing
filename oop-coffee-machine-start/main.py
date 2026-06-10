import coffee_maker
from money_machine import MoneyMachine
from menu import Menu
from coffee_maker import Car

coffee_maker = coffee_maker.CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

money_machine.report()
coffee_maker.report()

while is_on:
    options = menu.get_items()
    choice = input("What would you like?")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "add":
        ingredient = input("What ingredient would you like to add in to the coffee machine?")
        amount = int(input("How much would you like to top up?"))
        coffee_maker.add_resources(ingredient, amount)
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

car = Car()

print(car.print_top_speed())
