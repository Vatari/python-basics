square_meters = float(input())
price_for_greening = square_meters * 7.61

discount = price_for_greening * 0.18

price_total = price_for_greening - discount

print(f"The final price is: {price_total} lv.")
print(f"The discount is: {discount} lv.")
