hour = int(input())
day = str(input())

if 10 <= hour <= 18:
    work_time = 1
else:
    work_time = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" \
        or day == "Saturday":
    work_day = 1
else:
    work_day = 0

if work_day == 1 and work_time == 1:
    print("open")
else:
    print("closed")
