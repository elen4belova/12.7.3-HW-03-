# исходный словарь
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# ввод суммы с клавиатуры
money = float(input("Введите начальную сумму: "))

# список ставок
list_pc = list(map(float, per_cent.values()))

# список накопленных средств за год вклада и его вывод на экран
deposit = [round(money*list_pc[0]/100, 4), round(money*list_pc[1]/100, 4), round(money*list_pc[2]/100, 4), round(money*list_pc[3]/100, 4)]
print("В этих банках вы можете заработать", deposit)

# максимальный заработок и его вывод на экранpo[p[]][][][][

kjpiopoiopp
print("Максимальная сумма, которую вы можете заработать —", max(deposit))





