number1 = int(input())
number2 = int(input())
operator = input()

result = ""
odd_even = ""

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        result = number1 / number2
        print(f"{number1} {operator} {number2} = {result:.2f}")
elif operator == "%":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        result = number1 % number2
        print(f"{number1} {operator} {number2} = {int(result)}")

if operator == "+" or operator == "-" or operator == "*":
    if result % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"
    print(f"{number1} {operator} {number2} = {result} - {odd_even}")








