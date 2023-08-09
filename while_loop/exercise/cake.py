width = int(input())
lenght = int(input())

cake_pieces = width * lenght
cake_taken = 0

command = input()

while command != 'STOP':
    pieces = int(command)
    cake_taken += pieces
    if cake_taken >= cake_pieces:
        break
    command = input()
pieces_left = abs(cake_pieces - cake_taken)
if cake_pieces > cake_taken:
    print(f"{pieces_left} pieces are left.")
else:
    print(f"No more cake left! You need {pieces_left} pieces more.")
