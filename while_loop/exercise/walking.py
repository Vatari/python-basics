goal_steps = 10000
total_steps = 0

while True:

    steps = input()

    if steps == "Going home":
        last_steps = int(input())
        total_steps += last_steps
        if total_steps >= goal_steps:
            print(f"Goal reached! Good job!")
            print(f"{abs(goal_steps - total_steps)} steps over the goal!")
            break
        print(f"{abs(goal_steps - total_steps)} more steps to reach goal.")
        break
    total_steps += int(steps)

    if total_steps >= goal_steps:
        print(f"Goal reached! Good job!")
        print(f"{abs(goal_steps - total_steps)} steps over the goal!")
        break

