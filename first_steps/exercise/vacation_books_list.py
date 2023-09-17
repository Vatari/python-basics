book_pages = int(input())
pages_for_hour = int(input())
days_needed = int(input())

time_needed = book_pages / pages_for_hour
hours_needed_per_day = time_needed / days_needed

print(int(hours_needed_per_day))
