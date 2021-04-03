Monday = 1
Truseday = 2
Wednessday = 3
Tuseday = 4
Friday = 5
Saturday = 6
Sunday = 7

number_of_week_day = int(input('введите номер дня недели - 1-7'))

if number_of_week_day == 1:
    print('Понедельник')
elif number_of_week_day == 2:
    print('Вторник')
elif number_of_week_day == 3:
    print('Среда')
elif number_of_week_day == 4:
    print('Четверг')
elif number_of_week_day == 5:
    print('Пятница')
elif number_of_week_day == 6:
    print('Суббота')
elif number_of_week_day == 7:
    print('Воскресенье')
else:
    print('Ошибка! Число не может быть больше 8 и мньше 1')