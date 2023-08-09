width = int(input())
length = int(input())
height = int(input())

free_space = height * width * length
used_space = 0

while used_space <= free_space:
    command = input()
    if command == 'Done':
        left_area = free_space - used_space
        print(f'{left_area} Cubic meters left.')
        break
    else:
        box_qty = int(command)
        used_space += box_qty

if used_space > free_space:
    needed_area = used_space - free_space
    print(f'No more free space! You need {needed_area} Cubic meters more.')
