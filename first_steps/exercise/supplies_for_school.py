pens = int(input())
markers = int(input())
detergent = int(input())
percent = int(input()) / 100

price_for_pens = pens * 5.80
price_for_markers = markers * 7.20
price_for_detergent = detergent * 1.20


total_sum = price_for_pens + price_for_markers + price_for_detergent
discount = total_sum * percent
print((total_sum - discount))
