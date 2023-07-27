record = float(input())
distance = float(input())
time_in_seconds = float(input())

time = distance * time_in_seconds
additional_meters = int(distance / 15)
bonus = additional_meters * 12.5
total_time = time + bonus

if total_time < record:
    print(f"Yes, he succeeded! The new world record is"
          f" {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time-record:.2f}"
          f" seconds slower.")
