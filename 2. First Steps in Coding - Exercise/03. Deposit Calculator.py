#Вход -> Депозирана сума - реално число в интервала
deposit_value = float(input())
#Вход -> Срок на депозита (в месеци - цяло число в интервала
deposit_term = int(input())
#Вход -> Годишен лихвен процент
deposit_percent = float(input())

#Изход -> да се отпечата на конзолата сумата в края на срока
overall = deposit_value + deposit_term * ((deposit_value * (deposit_percent / 100)) / 12)
print(overall)