number = int(input())
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if number not in range(1, 8):
    print("Error")
else:
    print(days[number-1])

