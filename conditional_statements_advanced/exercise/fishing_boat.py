budget = int(input())
season = input()
fisher_man = int(input())

ship_rent = 0

if season == "Spring":
    ship_rent = 3000
elif season == "Summer" or season == "Autumn":
    ship_rent = 4200
elif season == "Winter":
    ship_rent = 2600

if fisher_man <= 6:
    ship_rent *= 0.9
elif fisher_man <= 11:
    ship_rent *= 0.85
else:
    ship_rent *= 0.75

if fisher_man % 2 == 0 and season != "Autumn":
    ship_rent *= 0.95


difference = abs(budget-ship_rent)

if budget >= ship_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")



