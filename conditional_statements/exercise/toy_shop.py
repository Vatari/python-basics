vacation_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

price_puzzles = 2.60 * puzzles
price_dolls = 3 * dolls
price_bears = 4.10 * bears
price_minions = 8.20 * minions
price_trucks = 2 * trucks
total_toys = puzzles + dolls + bears + minions + trucks
total_sum = price_puzzles + price_dolls + price_bears + price_minions + price_trucks
discount = total_sum * 0.25

if total_toys >= 50:
    total_sum -= discount

final_sum = total_sum * 0.9


if final_sum >= vacation_price:
    print(f"Yes! {final_sum-vacation_price:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price-final_sum:.2f} lv needed.")


