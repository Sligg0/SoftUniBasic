#test 1 (365 = 811.76)
#test 2 (550 = 1223.2)

tax_per_year = int(input())

sneakers = tax_per_year * 0.60
outfit = sneakers * 0.80
ball = outfit / 4
accessories = ball / 5

overall = tax_per_year + sneakers + outfit + ball + accessories

print(overall)
