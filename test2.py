import turtle

# import turtle
# turtle.forward(200)
#
# turtle.right (90)
# turtle.forward(200)

# height = input("Введите свой рост: ")
# print(f"Привет, твой рост равняется {height}!")
#
# color = input("Введите свой любимый цвет: ")
# print(f"Ващ любимый цвет {color}")


# b = a + 2
# a = b * 4
# b = a / 3.14
# a = b - 8

# w = 5
# x = 4
# y = 8
# z = 2
# result = x + y
# print({result})
# result = z * 2
# print({result})
# result = y / x
# print({result})
# result = y - z
# print({result})
# result = w // z
# print({result})
# total = 10
# total = total + 14
# print(total)
#
# total = total + 10
# print(total)
#
# down_payment = 14
# due = total - down_payment
# print(due)
#
# subtotal = 0
# total = subtotal * 0.15
#
# sales = 4.444
# print(round(sales, 2))
# print(f"{sales:.2f}")
#
# number = 1234567.456
# print(f"{number:,.1f}")
#
# print('Джордж', 'Джон', 'Пол', 'Ринго', sep='@')

# import turtle
#
# # Создаём объект черепахи
# t = turtle.Turtle()

# # Рисуем круг радиусом 75 пикселей
# t.circle(75)
#
# # Завершаем программу и оставляем окно открытым до закрытия
# turtle.done()

# from turtle import *
#
# # Устанавливаем цвет заливки
# fillcolor("red")
#
# # Начинаем заполнение области
# begin_fill()
#
# # Рисуем квадрат
# for _ in range(4):
#     forward(100)  # Двигаемся вперёд на 100 пикселей
#     right(90)     # Поворачиваем направо на 90 градусов
#     circle(30)
#
# # Завершаем заполнение
# end_fill()
#
# circle(80)
#
# # Завершаем работу с библиотекой
# turtle.done()


# # Программа для расчёта 2


# # Программа для перевода квадратных метров в акры
#
# # Ввод площади в квадратных метрах от пользователя
# square_meters = float(input("Введите площадь участка в квадратных метрах:"))
#
# # Коэффициент перевода: 1 акр = 4046,86 м²
# ACRES_PER_SQUARE_METERS = 4046.86
#
# # Расчёт количества акров
# acres = square_meters / ACRES_PER_SQUARE_METERS
#
# # Вывод результата
# print(f"Площадь участка составляет {acres:.4f} акров.")

# # Программа для расчёта общей стоимости покупок с налогом
#
# # Ставка налога с продаж (7%)
# TAX_RATE = 0.07
#
# # Список для хранения цен товаров
# prices = []
#
# # Запрашиваем цену каждого из 5 товаров
# print("Введите цену каждого из 5 товаров:")
# for i in range(5):
#  price = float(input(f"Товар {i + 1}:"))
#  prices.append(price)
#
# # Вычисляем накопленную стоимость (сумму без налога)
# total_cost = sum(prices)
#
# # Рассчитываем сумму налога
# tax_amount = total_cost * TAX_RATE
#
# # Находим итоговую сумму (с налогом)
# final_amount = total_cost + tax_amount
#
# # Вывод результатов
# print("\n--- Результаты расчёта ---")
# print(f"Накопленная стоимость товаров: ${total_cost:.2f}")
# print(f"Сумма налога с продаж ({7}%): ${tax_amount:.2f}")
# print(f"Итоговая сумма к оплате: ${final_amount:.2f}")

# Скорость автомобиля (км/ч)
# speed = 70

# Время в часах для расчёта
# times = [6, 10, 15]
#
# # Вычисление и вывод расстояния для каждого времени
# for time in times:
#  distance = speed * time
#  print(f"За {time} часов автомобиль пройдёт {distance} км")
#
#
# # Ввод величины покупки
# purchase_amount = float(input("Введите величину покупки:"))
#
# # Ставки налогов (в десятичной форме)
# federal_tax_rate = 0.05 # 5%
# regional_tax_rate = 0.025 # 2.5%
#
# # Расчёт налогов
# federal_tax = purchase_amount * federal_tax_rate
# regional_tax = purchase_amount * regional_tax_rate
#
# # Общий налог
# total_tax = federal_tax + regional_tax
#
# # Общая сумма продажи
# total_amount = purchase_amount + total_tax
#
# # Вывод результатов
# print("\nРезультаты расчёта:")
# print(f"Сумма покупки: ${purchase_amount:.2f}")
# print(f"Федеральный налог с продаж: ${federal_tax:.2f}")
# print(f"Региональный налог с продаж: ${regional_tax:.2f}")
# print(f"Общий налог с продаж: ${total_tax:.2f}")
# print(f"Общая сумма продажи: ${total_amount:.2f}")

# distance = float(input("Укажите количество пройденных километров"))
# petrol = float(input("Сколько израсходовано бензина в литрах"))
# kilometers_per_liter = distance / petrol
#
# print(f"Расход бензина составил 1 литр на {kilometers_per_liter:.2f} километров")
#
# Food_price = float(input("Введите стоимость блюд: "))
# tax_rate = 0.07
# tips_rate = 0.18
#
# # Вычисления суммы
# dish_tax = Food_price * tax_rate
# dish_tips = Food_price * tips_rate
# total_amount = Food_price + dish_tax + dish_tips
#
# print(f"Стоимость заказанных блюд: {Food_price:.2f} рублей")
# print(f'Размер налогов (7%): {dish_tax:.2f} рублей')
# print(f"Размер чаяевых (18%): {dish_tips:.2f} рублей")
# print(f"Общая стоимость: {total_amount:.2f}  рублей")

# Формула перевода F = (9 / 5) * C + 32
# celsium = float(input("Enter a temperature in Celsius: (°C):"))
# fahrenheit = (9 / 5) * celsium + 32
# print(f"Температура в градусах Фаренгейта (°F): {fahrenheit} ")
# --------------------------------------------------------------------------------
# sugar_per_batch = 1.5
# oil_per_batch = 1
# flour_per_batch = 2.75
# total_buns_per_batch = 48
#
# try:
#   desired_buns = int(input("Сколько бутылок вы хотите приготовить?"))
#   if desired_buns <= 0:
#     print("Количество бутылок должно быть положительным")
#   else:
#     scale_factor = desired_buns / total_buns_per_batch
#
#     request_sugar = sugar_per_batch * scale_factor
#     request_oil = oil_per_batch * scale_factor
#     request_flour = flour_per_batch * scale_factor
#
#     print(f'\n Для приготовления {desired_buns} бутылок понадобиться:')
#     print(f'Сахар: {request_sugar:.2f} стакана')
#     print(f'Масло: {request_oil:.2f} стакана')
#     print(f'Мука: {request_flour:.2f} стакана')
#
# except ValueError:
#     print("Пожалуйста, введите целое число.")

# male_count = int(input("Введите количество учащихся мужского пола: "))
# famale_count = int(input("Введите количество учащихся женского пола: "))
# total_count = male_count + famale_count
#
# if total_count == 0:
#     print("В группе нет учащихся!")
# else:
#     male_percent = (male_count / total_count) * 100
#     fmale_percent = (famale_count / total_count) * 100
#
# print(f"Процент учащихся мужского пола: {male_percent:.1f}%")
# print(f"Процент учащихся женского пола {fmale_percent:.1f}%")

# # Константы
# COMMISSION_RATE = 0.03  # 3% комиссии
#
# # Данные о покупке
# quantity_purchased = 2000
# price_per_share_purchase = 40.00
# purchase_price = quantity_purchased * price_per_share_purchase
# commission_purchase = purchase_price * COMMISSION_RATE
#
# # Данные о продаже
# quantity_sold = 2000
# price_per_share_sale = 42.75
# selling_price = quantity_sold * price_per_share_sale
# commission_sale = selling_price * COMMISSION_RATE
#
# # Расчёт остатка денег
# remaining_money = selling_price - purchase_price - commission_purchase - commission_sale
#
# # Вывод результатов
# print(f"Сумма, уплаченная за акции при покупке: {purchase_price} долларов")
# print(f"Комиссия брокеру при покупке: {commission_purchase} долларов")
# print(f"Сумма, за которую Джо продал акции: {selling_price} долларов")
# print(f"Комиссия брокеру при продаже: {commission_sale} долларов")
# print(f"Сумма, которая осталась у Джо после всех операций: {remaining_money} долларов")
#
# # Определение результата
# if remaining_money > 0:
#     print("Джо получил прибыль")
# else:
#     print("Джо понес убытки")

# # Программа для расчёта количества виноградных лоз на гряде
#
# # Ввод данных от пользователя
# R = float(input("Введите длину гряды в метрах:"))
# E = float(input("Введите пространство, занимаемое концевой опорой в метрах:"))
# S = float(input("Введите расстояние между виноградными лозами в метрах:"))
#
# # Расчёт количества лоз по формуле V = (R – 2E) / S
# V = (R - 2 * E) / S
#
# # Вывод результата
# print(f"Количество виноградных лоз, которые поместятся на гряде: {V:.0f}")


# Запрос ввода от пользователя
seconds = int(input("Введите количество секунд:"))

# Инициализация переменных для результата
days = 0
hours = 0
minutes = 0
remaining_seconds = seconds

# Преобразование в дни (86 400 секунд в сутках)
if remaining_seconds >= 86400:
 days = remaining_seconds // 86400
 remaining_seconds%= 86400

# Преобразование в часы (3 600 секунд в часе)
if remaining_seconds >= 3600:
 hours = remaining_seconds // 3600
 remaining_seconds%= 3600

# Преобразование в минуты (60 секунд в минуте)
if remaining_seconds >= 60:
 minutes = remaining_seconds // 60
 remaining_seconds%= 60

# Вывод результата
print(f"{seconds} секунд — это:")
if days > 0:
 print(f"{days} день(я)")
if hours > 0:
 print(f"{hours} час(а)")
if minutes > 0:
 print(f"{minutes} минута(ы)")
if remaining_seconds > 0:
 print(f"{remaining_seconds} секунда(ы)")
