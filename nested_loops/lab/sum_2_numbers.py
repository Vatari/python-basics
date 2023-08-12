start_range = int(input())
end_range = int(input())
magic_number = int(input())
combinations_counter = 0
is_number_found = False

for num1 in range(start_range, end_range + 1):
    for num2 in range(start_range, end_range + 1):
        combinations_counter +=1

        if num1 + num2 == magic_number:
            print(f'Combination N:{combinations_counter} ({num1} + {num2} = {magic_number})')
            is_number_found = True
            break
    if is_number_found:
        break
if not is_number_found:
    print(f'{combinations_counter} combinations - neither equals {magic_number}')
