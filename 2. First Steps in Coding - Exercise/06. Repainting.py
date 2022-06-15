#Needed Materials
need_naylon_kvm = int(input())
need_paint_liters = int(input())
need_thinner_liters = int(input())
need_hours_masters = int(input())

#Price per unit
price_naylon_kvm = 1.50
price_paint_liter = 14.50
price_thinner_liter = 5.00
price_bags = 0.40

#Rumens add 10% paint + 2kvm naylon
changed_naylon_kvm = need_naylon_kvm + 2
changed_paint_liters = need_paint_liters + (need_paint_liters * 0.1)

#Materials Costs
price_naylon_all = changed_naylon_kvm * price_naylon_kvm
price_paint_all = changed_paint_liters * price_paint_liter
price_thinner_all = need_thinner_liters * price_thinner_liter
price_all = price_naylon_all + price_paint_all + price_thinner_all + price_bags

#Masters Price per hour = 30% of materials cost
price_masters_hourly = price_all * 0.3
price_masters_all = price_masters_hourly * need_hours_masters

#да се отпечата на конзолата един ред: "сумата на всички разходи"
overall = price_all + price_masters_all

print(overall)