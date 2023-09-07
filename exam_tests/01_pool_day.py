from math import ceil

people = int(input())
tax = float(input())
price_chair = float(input())
price_umbrella = float(input())

tax_sum = people * tax
sum_chairs = ceil(people * 0.75) * price_chair
sum_umbrella = ceil(people / 2) * price_umbrella

final_price = tax_sum + sum_chairs + sum_umbrella

print(f"{final_price:.2f} lv.")

