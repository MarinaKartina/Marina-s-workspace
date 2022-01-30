cost = [0, 990, 1390]
price = 0

count = None
while type(count) != int:
    try:
        count = int(input("Введите количество билетов: "))
    except ValueError as error:
        print("Вы ввели некорректное значение, повторите ввод")

for per in range(count):
    age = None
    while type(age) != int or int(age) <= 0 or int(age) >= 100:
        try:
            age = int(input(f"Введите возраст участника № {per+1}: "))
            if age <= 0 or age >= 100:
                print("Участнику не может быть столько лет, повторите ввод")
        except ValueError as error:
            print("Вы ввели некорректное значение, повторите ввод")
    if 0 < age < 18:
        price += cost[0]
        print(f"Билет для этого участника стоит {cost[0]} рублей")
    elif 18 <= age < 25:
        price += cost[1]
        print(f"Билет для этого участника стоит {cost[1]} рублей")
    else:
        price += cost[2]
        print(f"Билет для этого участника стоит {cost[2]} рублей")

if count > 3 and price:
    price *= 0.9
    print("Вы получаете скидку 10%")

print(f"Сумма к оплате за {count} билетов составляет: {price} рублей")

