import math
need_meters = float(input())
price_meters = 7.61
discount = 0.18

final_price = need_meters * 7.61
discounted_price = final_price - (final_price * discount)
discount = final_price - discounted_price

print(f"The final price is: {discounted_price:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")