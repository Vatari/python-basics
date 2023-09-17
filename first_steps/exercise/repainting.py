nylon = int(input()) + 2
paint = int(input()) * 1.1
thinner = int(input())
hours = int(input())

price_for_nylon = nylon * 1.50
price_for_paint = paint * 14.50
price_for_thinner = thinner * 5
bags = 0.40

total_sum = price_for_nylon + price_for_paint + price_for_thinner + bags
sum_per_hour = total_sum * 0.30 * hours
final_sum = total_sum + sum_per_hour

print(final_sum)