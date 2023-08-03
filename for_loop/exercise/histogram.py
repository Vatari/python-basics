num = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(num):
    number = int(input())
    if number < 200:
        p1 += 1
    elif number < 400:
        p2 += 1
    elif number < 600:
        p3 += 1
    elif number < 800:
        p4 += 1
    else:
        p5 += 1

p1_percentage = p1 / num * 100
p2_percentage = p2 / num * 100
p3_percentage = p3 / num * 100
p4_percentage = p4 / num * 100
p5_percentage = p5 / num * 100

print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")
print(f"{p4_percentage:.2f}%")
print(f"{p5_percentage:.2f}%")
