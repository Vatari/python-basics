import sys

num = int(input())
max_num = -sys.maxsize
sum_numbers = 0


for i in range(num):
    number = int(input())

    sum_numbers += number

    if number > max_num:
        max_num = number


if max_num == sum_numbers - max_num:
    print(f"Yes \n"
          f"Sum = {max_num}")
else:
    sum_numbers = sum_numbers - max_num
    print(f"No \n"
          f"Diff = {abs(max_num - sum_numbers)}")





