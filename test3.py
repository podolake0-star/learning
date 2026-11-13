import turtle
from re import purge

# name = turtle.textinput('Требуются данные', 'Введите свое имя')
# name2 = turtle.numinput('Требуются данные', 'Арк земли')
# ark = name2 / 4046,86
# # print (name)
# print (ark)

# Коэффициент перевода квадратных метров в акры
# ACRES_PER_SQM = 1 / 4046.86

# try:
#     # Запрос ввода у пользователя
#     square_meters = float(input("Введите площадь участка в квадратных метрах:"))
#     if square_meters < 0:
#         print("Площадь не может быть отрицательной.")
#     else:
#         # Вычисление количества акров
#         acres = square_meters * ACRES_PER_SQM
#
#     # Вывод результата с округлением до 4 знаков после запятой
#     print(f"Площадь участка составляет {acres:.4f} акров.")
# except ValueError:
#     print("Ошибка: пожалуйста, введите корректное число.")
#
# number = 1234567.456
# print(f"{number:,.1f}")
#
# print('Джордж', 'Джон', 'Пол', 'Ринго', sep='0')

# import turtle
#
# # Создаём черепашку и задаём цвет
# t = turtle.Turtle()
# t.color("blue")
#
# # Рисуем круг радиусом 75 пикселей
# t.circle(75)
#
# # Показываем окно с рисунком
# turtle.done()

# import turtle
#
# # Создаём объект черепашки
# t = turtle.Turtle()
#
# # Настраиваем заливку синим цветом
# t.fillcolor('black')
#
# # Начинаем заливку
# t.begin_fill()
#
# # Рисуем квадрат
# for _ in range(4):
#     t.forward(100)  # Двигаемся вперёд на 100 пикселей
#     t.left(90)       # Поворачиваем налево на 90 градуса
#
# # Завершаем заливку
# t.end_fill()
#
# # Остальная часть программы (если нужно что-то нарисовать после)
# # ...
#
# # Закрываем окно по клику
# turtle.exitonclick()

#
# import turtle
#
# t = turtle.Turtle()
#
# # Рисуем квадрат без заливки
# for i in range(4):
#     t.forward(100)
#     t.left(90)
#
# # Перемещаем черепашку в центр квадрата
# t.penup()
# t.goto(50, 50 - 80)
# t.pendown()
#
# # Рисуем красный круг с радиусом 80 пикселей
# t.color("red")
# t.begin_fill()
# t.circle(80)
# t.end_fill()
#
# turtle.done()


total = 0

# for i in range(1,6):
#     price = float(input(f'Введите цену товара {i}: '))
#     total += price
#
# tax = total * 0.07
# final_TOTAL = total + tax

# class Automobile:
#     def __init__(self, speed):
#         self.speed = speed
#
#     def distance(self, hours):
#        return self.speed * hours
#
# car = Automobile(70)
#
# print("Расстояние за 6 часов", car.distance(6), "км")
# print("Расстояние за 10 часов", car.distance(10), "км")
# print("Расстояние за 15 часов", car.distance(15), "км")

# class SalesTax:
#     def __init__(self, purchase):
#         self.purchase = purchase
#         self.federal_tax = purchase * 0.05
#         self.regional_tax = purchase * 0.025
#
#     def total_tax(self):
#         return self.federal_tax + self.regional_tax
#
#     def total_sale(self):
#         return  self.purchase + self.total_tax()
#
#     def display(self):
#         print("Сумма покупки", round(self.purchase, 2))
#         print("Федеральный налог", round(self.federal_tax, 2))
#         print("Региональный налог", round(self.regional_tax, 2))
#         print("Общий налог", round(self.total_tax(), 2))
#         print("Общая сумма продажи", round(self.total_sale(), 2))
#
# purchase = float(input("Введите сумму покупки: "))
# sale = SalesTax(purchase)
# sale.display()

# class FuelConsumption:
#     def __init__(self, kilometer, liters):
#         self.kilometer = kilometer
#         self.liters = liters
#
#     def calculate(self):
#         return self.kilometer / self.liters
#
#     def display(self):
#         print("Расход бензина", round(self.calculate(), 2),"км/л")
#
# kilometer = float(input("Введите количество пройденных километров: "))
# liter = float(input("Введите количество израсходованого бензина в литрах: "))
# car = FuelConsumption(kilometer, liter)
# car.display()

# class RestaurantBill:
#     def __init__(self, food_cost):
#         self.food_cost = food_cost
#         self.tip = food_cost * 0.18
#         self.tax = food_cost * 0.07
#
#     def total(self):
#         return self.food_cost + self.tax + self.tip
#
#     def display(self):
#         print("Стоимость еды:", round(self.food_cost, 2))
#         print("Чаевые (18%):", round(self.tip, 2))
#         print("Налог с продаж (7%):", round(self.tax, 2))
#         print("Итоговая сумма:", round(self.total(), 2))
#
# food_cost = float(input("Введите стоимость еды: "))
# bill = RestaurantBill(food_cost)
# bill.display()

# class TemperatureConverter:
#     def __init__(self, celsius):
#         self.celsius = celsius
#
#     def to_fahrenheit(self):
#         return (self.celsius * (9 / 5)) + 32
#
#     def display(self):
#         print("Температура по Фаренгейту: ", round(self.to_fahrenheit(), 2))
#
# celsius = float(input("Введите температуру в градусах Цельсия: "))
#
# temp = TemperatureConverter(celsius)
# temp.display()

# class Recipe:
#     def __init__(self, buns):
#         self.buns = buns
#         self.sugar = 1.5 * buns / 48
#         self.butter = 1 * buns / 48
#         self.flour = 2.5 * buns / 48
#
#     def display(self):
#         print("Для приготовления", self.buns, "булочек потребуется:")
#         print("Сахар:", round(self.sugar, 2), "стакана")
#         print("Масло:", round(self.butter, 2), "стакана")
#         print("Мука:", round(self.flour, 2), "стакана")
#
# buns = int(input("Сколько булочек вы хотите приготовить? "))
# recipe = Recipe(buns)
# recipe.display()


# class Students:
#     def __init__(self, boys, girls):
#         self.boys = boys
#         self.girls = girls
#         self.total = boys + girls
#
#     def calculate_percentages(self):
#         boys_percent = self.boys / self.total * 100
#         girls_percent = self.girls / self.total * 100
#         return boys_percent, girls_percent
#
#     def display(self):
#         boys_percent, girls_percent = self.calculate_percentages()
#
#         print("Всего учащихся:", self.total)
#         print("Процент юношей:", round(boys_percent, 2), "%")
#         print("Процент девушек:", round(girls_percent, 2), "%")
#
#
# boys = int(input("Введите количество юношей: "))
# girls = int(input("Введите количество девушек: "))
#
# group = Students(boys, girls)
# group.display()

# class StockTransaction:
#     def __init__(self, shares, buy_price, sell_price, commission_rate):
#         self.shares = shares
#         self.buy_price = buy_price
#         self.sell_price = sell_price
#         self.commission_rate = commission_rate
#
#     def calculate(self):
#         buy_amount = self.shares * self.buy_price
#         buy_commission = buy_amount * self.commission_rate
#
#         sell_amount = self.shares * self.sell_price
#         sell_commission = sell_amount * self.commission_rate
#
#         profit = sell_amount - sell_commission - buy_amount - buy_commission
#
#         print("Сумма, уплаченная за акции: $", round(buy_amount, 2))
#         print("Комиссия брокера при покупке: $", round(buy_commission, 2))
#         print("Сумма от продажи акций: $", round(sell_amount, 2))
#         print("Комиссия брокера при продаже: $", round(sell_commission, 2))
#         print("Итоговая прибыль или убыток: $", round(profit, 2))
#
#         if profit > 0:
#             print("Джо получил прибыль.")
#         elif profit < 0:
#             print("Джо понес убытки.")
#         else:
#             print("Джо не получил ни прибыли, ни убытка.")
#
#
# shares = 2000
# buy_price = 40.00
# sell_price = 42.75
# commission_rate = 0.03
#
# stock = StockTransaction(shares, buy_price, sell_price, commission_rate)
# stock.calculate()

# class Vineyard:
#     def __init__(self, row_length, end_post, spacing):
#         self.row_length = row_length
#         self.end_post = end_post
#         self.spacing = spacing
#
#     def calculate(self):
#         return (self.row_length - 2 * self.end_post) / self.spacing
#
#     def display(self):
#         vines = int(self.calculate())
#         print("Количество виноградных лоз:", vines)
#
#
# row_length = float(input("Введите длину гряды в метрах: "))
# end_post = float(input("Введите пространство концевой опоры в метрах: "))
# spacing = float(input("Введите расстояние между лозами в метрах: "))
#
# vineyard = Vineyard(row_length, end_post, spacing)
# vineyard.display()
#

# class CompoundInterest:
#     def __init__(self, principal, rate, frequency, years):
#         self.principal = principal
#         self.rate = rate / 100
#         self.frequency = frequency
#         self.years = years
#
#     def calculate(self):
#         amount = self.principal * (1 + self.rate / self.frequency) ** (self.frequency * self.years)
#         return amount
#
#     def display(self):
#         print("Первоначальный вклад:", round(self.principal, 2))
#         print("Сумма на счете после начисления процентов:", round(self.calculate(), 2))
#         print("Полученный доход:", round(self.calculate() - self.principal, 2))
#
#
# principal = float(input("Введите первоначальную сумму вклада: "))
# rate = float(input("Введите годовую процентную ставку (%): "))
# frequency = int(input("Введите количество начислений процентов в год: "))
# years = int(input("Введите количество лет: "))
#
# deposit = CompoundInterest(principal, rate, frequency, years)
# deposit.display()
# A_SCORE = 90
# B_SCORE = 80
# C_SCORE = 70
# D_SCORE = 60
#
# scorif_score = 50
#
# if scorif_score >= A_SCORE:
#     print('Ваш уровень -А.')
# elif scorif_score >= B_SCORE:
#     print('Ваш уровень -В.')
# elif scorif_score >= C_SCORE:
#     print('Ваш уровень -С.')
# elif scorif_score >= D_SCORE:
#     print('Ваш уровень - D.')
# else:
#     print('Ваш уровень - F.')
#
# temp = 3
# if not (temp > 5):
#     print('Э т о ниже м аксим альной т е м п е р а т у р ы .')


end = 5
for num in range(1, end + 1):
    square = num ** 2
    print(f'{num}\t{square}')

