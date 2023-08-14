num = int(input())

for current_num in range(1111, 9999 + 1):
    current_num_as_str = str(current_num)
    is_special = True
    for current_digit in current_num_as_str:
        if int(current_digit) == 0 or num % int(current_digit) != 0:
            is_special = False
            break
    if is_special:
        print(current_num, end=" ")
