#test / 85 / 75 / 47 / 17 / = 248.68875

length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

cubic_cm = length * width * height
space_liters = cubic_cm * 0.001
water_liters = space_liters * (1 - (percentage / 100))

#литрите вода, които ще събира аквариума.

print(water_liters)