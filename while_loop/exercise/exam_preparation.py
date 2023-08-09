grades_limit = int(input())

average_score = 0
count = 0
tasks = 0
arr = []

while True:
    task = input()

    if task == "Enough":
        print(f"Average score: {average_score / tasks:.2f}")
        print(f"Number of problems: {tasks}")
        print(f"Last problem: {arr[-1]}")
        break

    grade = int(input())

    if grade <= 4:
        count += 1

    if count == grades_limit:
        print(f"You need a break, {count} poor grades.")
        break

    average_score += grade
    tasks += 1
    arr.append(task)
