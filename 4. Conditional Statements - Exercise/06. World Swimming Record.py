from math import floor

world_record_seconds = float(input())
meters_to_do = float(input())
seconds_for_meter = float(input())

every_15_meters = floor(meters_to_do / 15)
slowed_time = every_15_meters * 12.5

time_to_complete_without_slow = meters_to_do * seconds_for_meter
time_to_complete = time_to_complete_without_slow + slowed_time
time_slower = time_to_complete - world_record_seconds

if time_to_complete < world_record_seconds:
    print(f"Yes, he succeeded! The new world record is {time_to_complete:.2f} seconds.")
else:
    print(f"No, he failed! He was {time_slower:.2f} seconds slower.")
