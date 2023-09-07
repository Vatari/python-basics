drink = input()
sugar = input()
quantity = int(input())

drink_price = 0
discount = 0

if drink == "Espresso":
    if quantity >= 5:
        drink_price = 0.9 * quantity
        discount = 0.25
    else:
        drink_price = 1.2 * quantity
elif drink == "Cappuccino":
    drink_price = 1.6 * quantity
elif drink == "Tea":
    drink_price = 0.7 * quantity

if sugar == "Without":
    drink_price *= 0.65
elif sugar == "Extra":
    drink_price *= 1.2

if drink_price > 15:
    discount = 0.2

final_price = drink_price - (drink_price * discount)
formatted_price = "{:.2f}".format(final_price)

print(f"You bought {quantity} cups of {drink} for {formatted_price} lv.")