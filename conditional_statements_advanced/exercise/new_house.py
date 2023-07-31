flowers_type = input()
flowers_qty = int(input())
budget = int(input())

price = 0

if flowers_type == "Roses":
    price = 5
    if flowers_qty > 80:
        price *= 0.9
elif flowers_type == "Dahlias":
    price = 3.80
    if flowers_qty > 90:
        price *= 0.85
elif flowers_type == "Tulips":
    price = 2.80
    if flowers_qty > 80:
        price *= 0.85
elif flowers_type == "Narcissus":
    price = 3
    if flowers_qty < 120:
        price *= 1.15
elif flowers_type == "Gladiolus":
    price = 2.50
    if flowers_qty < 80:
        price *= 1.20

total_sum = price * flowers_qty
difference = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Hey, you have a great garden with {flowers_qty} {flowers_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")

