qty = int(input())

arr = []

for _ in range(0, qty):
    number = int(input())
    arr.append(number)

print(f"Max number: {max(arr)}")
print(f"Min number: {min(arr)}")


