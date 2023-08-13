student_tickets = 0
standard_tickets = 0
kid_tickets = 0
movie_name = input()
while movie_name != "Finish":
    free_seats = int(input())
    sold_seats = 0
    for free_ticket in range(free_seats):
        current_ticket = input()
        if current_ticket == "End":
            break
        elif current_ticket == "student":
            student_tickets += 1
        elif current_ticket == "standard":
            standard_tickets += 1
        elif current_ticket == "kid":
            kid_tickets += 1

        sold_seats += 1

    percentage = sold_seats / free_seats * 100
    print(f"{movie_name} - {percentage:.2f}% full.")
    movie_name = input()

total_sold_tickets = student_tickets + standard_tickets + kid_tickets
student_percentage = student_tickets / total_sold_tickets * 100
standard_percentage = standard_tickets / total_sold_tickets * 100
kid_percentage = kid_tickets / total_sold_tickets * 100

print(f"Total tickets: {total_sold_tickets}")
print(f"{student_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kid_percentage:.2f}% kids tickets.")
