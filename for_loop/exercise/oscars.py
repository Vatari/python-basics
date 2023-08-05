actor = input()
academy_points = float(input())
judges = int(input())

for i in range(judges):
    judge_name = input()
    judge_points = float(input())
    academy_points += len(judge_name) * judge_points / 2
    if academy_points > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {academy_points:.1f}!")
        break

if academy_points < 1250.5:
    print(f"Sorry, {actor} you need {1250.5 - academy_points:.1f} more!")
