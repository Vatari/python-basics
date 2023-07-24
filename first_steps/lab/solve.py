length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100


volume = length * width * height
volume_in_litres = volume / 1000
litres_needed = volume_in_litres * (1 - percent)

print (litres_needed)