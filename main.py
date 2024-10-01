# Запрашиваем у пользователя ввод дня и месяца
d = int(input('Введите день '))
m = int(input('Введите месяц '))
# Проверяем, к какому времени года относится введенная дата
if (m == 9 and  d < 31 and d >= 1 ) or (m == 10  and d <= 31 and d >= 1 ) or (m == 11 and d <= 30 and d >= 1):
    s = 'Осень'
elif (m == 3 and d <= 31 and d >= 1) or (m == 4 and d <= 30 and d >= 1) or (m == 5 and d <= 31 and d >= 1):
    s = 'Весна'
elif (m == 12 and d >= 1 and d <= 31) or (m == 1 and d <= 31 and d >= 1) or (m == 2 and d <= 29 and d >= 1):
    s = 'Зима'
else:
    s = 'Лето'
# Выводим название сезона
print(f"Сезон {s}")
