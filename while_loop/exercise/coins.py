import math

coins = 0
change = float(input())
change_to_str = change * 100

while change_to_str > 0:

    if change_to_str >= 200:
        change_to_str -= 200
        coins += 1
    elif 200 > change_to_str >= 100:
        change_to_str -= 100
        coins += 1
    elif 100 > change_to_str >= 50:
        change_to_str -= 50
        coins += 1
    elif 50 > change_to_str >= 20:
        change_to_str -= 20
        coins += 1
    elif 20 > change_to_str >= 10:
        change_to_str -= 10
        coins += 1
    elif 10 > change_to_str >= 5:
        change_to_str -= 5
        coins += 1
    elif 5 > change_to_str >= 2:
        change_to_str -= 2
        coins += 1
    elif 2 > change_to_str >= 1:
        change_to_str -= 1
        coins += 1

    change_to_str = math.floor(change_to_str)

print(coins)
