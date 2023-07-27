from math import ceil
serial_name = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
break_time = break_length / 4


time_left = break_length - lunch_time - break_time

if time_left >= episode_length:
    print(f"You have enough time to watch {serial_name} and left with {ceil(time_left-episode_length)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(episode_length-time_left)} more minutes.")
