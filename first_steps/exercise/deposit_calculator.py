deposit = float(input())
deposit_range = int(input())
annual_percentage = float(input())

interest_made = deposit * annual_percentage / 100
interest_monthly = interest_made / 12

total_sum = deposit + deposit_range * interest_monthly

print(total_sum)