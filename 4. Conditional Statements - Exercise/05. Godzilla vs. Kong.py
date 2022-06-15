movie_budget = float(input())
number_extras = int(input())
prize_dress_one_extra = float(input())

movie_decor = movie_budget * 0.10

if number_extras > 150:
    prize_dress_one_extra = prize_dress_one_extra * 0.90

dressed_extras = prize_dress_one_extra * number_extras

price_cost = dressed_extras + movie_decor
money_not_enough = price_cost - movie_budget
money_enough = movie_budget - price_cost

if price_cost > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {money_not_enough:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money_enough:.2f} leva left.")