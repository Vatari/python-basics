numbers = []

while True:
    command = input()

    if command == "Stop":
        print(min(numbers))
        break
    numbers.append(int(command))
