num1 = int(input())
num2 = int(input())

for current_num in range(num1, num2 + 1):
    even_sum = 0
    odd_sum = 0
    current_num_as_str = str(current_num)
    for index, digit in enumerate(current_num_as_str):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)

    if odd_sum == even_sum:
        print(current_num, end=" ")

