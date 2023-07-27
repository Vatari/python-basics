budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

price_for_video_cards = video_cards * 250
price_for_processors = processors * (price_for_video_cards * 0.35)
price_for_ram = ram * (price_for_video_cards * 0.1)

total_sum = price_for_video_cards + price_for_processors + price_for_ram

if video_cards > processors:
    total_sum *= 0.85


if budget >= total_sum:
    print(f"You have {budget-total_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum-budget:.2f} leva more!")



