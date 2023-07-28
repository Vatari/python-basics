fruit = input()
day = input()
qty = float(input())

price = 0

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend_days = ["Saturday", "Sunday"]
fruits = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]

correct_input = False

if day in working_days:
    correct_input = True
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
elif day in weekend_days:
    correct_input = True
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20

if fruit not in fruits:
    correct_input = False

if not correct_input:
    print("error")
else:
    print(f"{price * qty:.2f}")


