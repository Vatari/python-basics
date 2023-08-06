total = 0

while True:
    command = input()
    if command == "NoMoreMoney":
        break
    current_sum = float(command)
    if current_sum < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {current_sum:.2f}")
        total += current_sum

print(f"Total: {total:.2f}")
