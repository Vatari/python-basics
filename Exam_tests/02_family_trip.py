budget = float(input())
overnight_stay = int(input())
price_per_night = float(input())
additional_expense = int(input())

if overnight_stay > 7:
    price_per_night *= 0.95

expenses = budget * additional_expense / 100

total_sum = overnight_stay * price_per_night

final_sum = total_sum + expenses
left_money = abs(budget - final_sum)

if final_sum <= budget:
    print(f"Ivanovi will be left with {left_money:.2f} leva after vacation.")
else:
    print(f"{left_money:.2f} leva needed.")
