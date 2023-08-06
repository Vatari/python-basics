numbers = []

while True:
    command = input()

    if command == "Stop":
        print(max(numbers))
        break
    numbers.append(int(command))
