chicken_menu = int(input()) * 10.35
fish_menu = int(input()) * 12.40
vegetarian_menu = int(input()) * 8.15
shipment = 2.50

total_sum = chicken_menu + fish_menu + vegetarian_menu
desert = total_sum * 0.20

final_sum = total_sum + desert + shipment

print(final_sum)