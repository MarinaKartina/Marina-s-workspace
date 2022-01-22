per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите сумму вклада: '))
bank_list = list(per_cent.values())
deposit = []
for i in range(4):
    deposit.append(round(bank_list[i] * money/100, 2))
dep_dict = {'ТКБ': deposit[0], 'СКБ': deposit[1], 'ВТБ': deposit[2], 'СБЕР': deposit[3]}
print("Сумма процентов в каждом банке за год: ", dep_dict)
print("Максимальная сумма, которую вы можете заработать: ", max(deposit))
