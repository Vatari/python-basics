budget = float(input())
stat_people = int(input())
dress_for_one = float(input()) * stat_people
decor = budget - budget * 0.9

if stat_people > 150:
    dress_for_one *= 0.9

final_sum = decor + dress_for_one

if final_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {final_sum-budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget-final_sum:.2f} leva left.")