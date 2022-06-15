chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15
delivery_price = 2.50
#desert = 20% overall (without delivery)

amount_chicken_menu = int(input())
amount_fish_menu = int(input())
amount_vegan_menu = int(input())

all_chicken_price = amount_chicken_menu * chicken_menu_price
all_fish_price = amount_fish_menu * fish_menu_price
all_vegan_price = amount_vegan_menu * vegan_menu_price
chicken_fish_vegan_price = all_chicken_price + all_fish_price + all_vegan_price

desert_price = chicken_fish_vegan_price * 0.20

#Да се отпечата на един ред цена на поръчката (2 / 4 / 3 = 116,2)

overall = chicken_fish_vegan_price + desert_price + delivery_price

print(overall)