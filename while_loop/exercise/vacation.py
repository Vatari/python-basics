needed_money = float(input())
budget = float(input())

spent_money = 0
saved_money = 0
days = 0
spend_counter = 0

while True:
    command = input()
    sum_ = float(input())
    days += 1
    if command == "spend":
        budget -= sum_
        if budget < 0:
            budget = 0
        spend_counter += 1
    elif command == "save":
        budget += sum_
        spend_counter = 0

    if budget >= needed_money:
        print(f"You saved the money for {days} days.")
        break
    if spend_counter == 5:
        print(f"You can't save the money.")
        print(f"{days}")
        break
