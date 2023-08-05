climber_groups = int(input())

musala_climbers = 0
monblan_climbers = 0
kilimandjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

total_climbers = 0


for i in range(climber_groups):
    climbers = int(input())
    total_climbers += climbers
    if climbers <= 5:
        musala_climbers += climbers
    elif climbers <= 12:
        monblan_climbers += climbers
    elif climbers <= 25:
        kilimandjaro_climbers += climbers
    elif climbers <= 40:
        k2_climbers += climbers
    else:
        everest_climbers += climbers

musala_percent = musala_climbers / total_climbers * 100
monblan_percent = monblan_climbers / total_climbers * 100
kilimandjaro_percent = kilimandjaro_climbers / total_climbers * 100
k2_percent = k2_climbers / total_climbers * 100
everest_percent = everest_climbers / total_climbers * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimandjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")

