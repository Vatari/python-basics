month = input()
qty = int(input())

studio_price = 0
apartment_price = 0
total_sum_studio = 0
total_sum_apartment = 0

if month == "May" or month == "October":
    total_sum_studio = 50 * qty
    total_sum_apartment = 65 * qty
    if 7 < qty <= 14:
        total_sum_studio *= 0.95
    elif qty > 14:
        total_sum_studio *= 0.70
elif month == "June" or month == "September":
    total_sum_studio = 75.20 * qty
    total_sum_apartment = 68.70 * qty
    if qty > 14:
        total_sum_studio *= 0.80
elif month == "July" or month == "August":
    total_sum_studio = 76 * qty
    total_sum_apartment = 77 * qty

if qty > 14:
    total_sum_apartment *= 0.90

print(f"Apartment: {total_sum_apartment:.2f} lv.")
print(f"Studio: {total_sum_studio:.2f} lv.")

