import pandas as pd

# Создаём простой DataFrame
# data = {'Имя': ['Анна', 'Борис', 'Виктор'], 'Возраст': [25, 30, 35]}
# df = pd.DataFrame(data)
# print(df)

# test1 = float(input("Ведите первую оценку "))
# test2 = float(input("Ведите вторую оценку "))
# test3 = float(input("Ведите третью оценку "))
#
# average = (test1 + test2 + test3) / 3
# print("Средний бал составляет", average)

# totalSeconds = float(input("Ведите количество секунд "))
# hours = totalSeconds // 3600
# minutes = (totalSeconds // 60) % 60
# seconds = totalSeconds % 60
#
# print("Вот время в часах, минутах, секундах")
# print(hours)
# print(minutes)
# print(seconds)

# future_value = float(input("Введите требуемую будущее значение: "))
# rate = float(input("Введите годовую процентную ставку: "))
# years = int(input("Введите количество лет хранения денег на счете: "))
#
# present_value = future_value / (1.0 + rate)**years
# print("Вам потребуется внести сумму:", present_value)

# print('Один', end=' ')
# print('Два', end=' ')
# print('Три')
#
# print ('Один', 'Два', 'Три')
#
# print('Один\nДва\nТри')

name = 'Карли'
print('Привет, {name}')

name = 'Карли'
print(f'Привет, {name}')

value = 99
print( f'Значение равно {value + 1}')

value = 65.4321
print(f'Значение равно {value:.2f}')

value = 987654.129
print(f'Значение равно {value:,.2f}')

value = 9876543210
print(f'Значение равно {value:,d}')

print(f'{name:10}')

print(f'{number:<12d}')




