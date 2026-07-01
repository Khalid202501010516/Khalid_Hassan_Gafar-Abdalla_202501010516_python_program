COFFEE_PRICE = 8.50
TEA_PRICE = 6.00
SANDWICH_PRICE = 12.00


def calculate_total(coffee_qty, tea_qty, sandwich_qty):
    total = (coffee_qty * COFFEE_PRICE) + \
            (tea_qty * TEA_PRICE) + \
            (sandwich_qty * SANDWICH_PRICE)
    return total


def get_customer_input():
    name = input("Customer name: ")
    coffee = int(input("Coffee quantity: "))
    tea = int(input("Tea quantity: "))
    sandwich = int(input("Sandwich quantity: "))

    return name, coffee, tea, sandwich