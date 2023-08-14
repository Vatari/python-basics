jury = int(input())
presentations = 0
final_grade = 0
command = input()

while command != "Finish":
    presentations += 1
    current_grade = 0
    for grade in range(jury):
        current = float(input())
        current_grade += current
    average_grade = current_grade / jury
    print(f"{command} - {average_grade:.2f}.")
    final_grade += average_grade
    command = input()

final_average_grade = final_grade / presentations
print(f"Student's final assessment is {final_average_grade:.2f}.")
