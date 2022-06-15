puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

excursion = float(input())
number_of_puzzles = int(input())
number_of_talking_doll = int(input())
number_of_teddy_bear = int(input())
number_of_minion = int(input())
number_of_truck = int(input())

number_all_toys = number_of_puzzles + number_of_talking_doll + number_of_teddy_bear + \
                     number_of_minion + number_of_truck
price_all_toys = (puzzle_price * number_of_puzzles) + \
                     (talking_doll_price * number_of_talking_doll) + \
                     (teddy_bear_price * number_of_teddy_bear) + \
                     (minion_price * number_of_minion) + \
                     (truck_price * number_of_truck)

if number_all_toys >= 50:
    price_all_toys = price_all_toys * 0.75

final_price_all_toys = price_all_toys - (price_all_toys * 0.10)
money_left = final_price_all_toys - excursion
not_enough = excursion - final_price_all_toys

if final_price_all_toys >= excursion:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {not_enough:.2f} lv needed.")