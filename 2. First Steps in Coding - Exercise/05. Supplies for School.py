packages_pens = int(input())
packages_markers = int(input())
liters_detergent = int(input())
discount_percentage = int(input())

pen_price = 5.80
marker_price = 7.20
detergent_liter_price = 1.20

packages_pens_price = packages_pens * pen_price
packages_markers_price = packages_markers * marker_price
liters_detergent_price = liters_detergent * detergent_liter_price

consumatives_price = packages_pens_price + packages_markers_price + liters_detergent_price
overall = consumatives_price - (consumatives_price * (discount_percentage / 100))

print(overall)