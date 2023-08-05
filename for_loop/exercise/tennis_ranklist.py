import math

tournaments = int(input())
start_points = int(input())

points_won = 0
wins = 0

for i in range(tournaments):
    stages = input()
    if stages == "W":
        points_won += 2000
        wins += 1
    elif stages == "F":
        points_won += 1200
    elif stages == "SF":
        points_won += 720

final_points = start_points + points_won
average_points = points_won / tournaments
wins_percent = wins / tournaments * 100

print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{wins_percent:.2f}%")
