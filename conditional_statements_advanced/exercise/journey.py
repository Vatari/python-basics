budget = float(input())
season = input()

destination = ""
type_vacation = ""
spent_money = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent_money = budget * 1.30
        type_vacation = "Camp"
    elif season == "winter":
        spent_money = budget * 1.70
        type_vacation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_vacation = "Camp"
        spent_money = budget * 1.40
    elif season == "winter":
        type_vacation = "Hotel"
        spent_money = budget * 1.80
else:
    destination = "Europe"
    spent_money = budget * 1.90
    type_vacation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_vacation} - {abs(budget-spent_money):.2f}")
