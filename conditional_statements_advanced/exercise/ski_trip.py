days = int(input()) - 1
room_type = input()
assessment = input()

total_sum = 0

if room_type == "room for one person":
    total_sum = days * 18
elif room_type == "apartment":
    if days < 10:
        total_sum = days * 25 * 0.70
    elif days <= 15:
        total_sum = days * 25 * 0.65
    elif days > 15:
        total_sum = days * 25 * 0.50
elif room_type == "president apartment":
    if days < 10:
        total_sum = days * 35 * 0.90
    elif days <= 15:
        total_sum = days * 35 * 0.85
    elif days > 15:
        total_sum = days * 35 * 0.80

if assessment == "positive":
    total_sum *= 1.25
elif assessment == "negative":
    total_sum *= 0.90

print(f"{total_sum:.2f}")
