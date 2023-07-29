hour = int(input())
day = input()

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
weekend = ["Sunday"]

if day in working_days and hour in range(10, 18):
    print("open")
else:
    print("closed")
