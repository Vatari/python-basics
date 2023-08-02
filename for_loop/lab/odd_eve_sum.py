num = int(input())

even_sum = 0
odd_sum = 0

for i in range(0, num):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if even_sum == odd_sum:
    print(f"Yes \n"
          f"Sum = {even_sum}")
else:
    print(f"No \n"
          f"Diff = {abs(even_sum-odd_sum)}")

