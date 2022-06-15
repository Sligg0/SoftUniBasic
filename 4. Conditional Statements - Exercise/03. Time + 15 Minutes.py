import math
hours_now = int(input())
minutes_now = int(input())

hours_to_minutes = hours_now * 60
minutes_hours = minutes_now + hours_to_minutes
minutes_hours_15 = minutes_hours + 15

hours = minutes_hours_15 // 60
minutes = minutes_hours_15 % 60
hours = math.floor(hours)

if hours <= 23:
    hours_correct = hours
else:
    hours_correct = 0

if minutes < 10:
    print(f"{hours_correct}:0{minutes}")
else:
    print(f"{hours_correct}:{minutes}")