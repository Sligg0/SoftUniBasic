from math import ceil
series_name = str(input())
episode_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
rest_time = break_time / 4

time_left = break_time - (lunch_time + rest_time)

time_to_use = time_left - episode_time
need_time = episode_time - time_left

if time_left >= episode_time:
    print(f"You have enough time to watch {series_name} and left with {ceil(time_to_use)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(need_time)} more minutes.")