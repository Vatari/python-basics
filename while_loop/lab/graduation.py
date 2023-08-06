name = input()
class_ = 0
count = 0
grades = 0


while True:
    grade = float(input())

    if grade < 4:
        count += 1

    if grade >= 4:
        class_ += 1
        grades += grade
        if class_ == 12:
            print(f"{name} graduated. Average grade: {grades / class_:.2f}")
            break

    if count > 1:
        print(f"{name} has been excluded at {class_ + 1} grade")
        break
