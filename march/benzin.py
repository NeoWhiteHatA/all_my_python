200#программа для расчета полного расхода бензина на заданное расстояние
distance = float(input('ведите дистанцию, преодоленную авто в км: '))
benzin_on_km = float(input('Введите сход авто бензина в литрах на км: '))

full_benzine_of_distance = format(distance / benzin_on_km, '.2f')

print('Расход топлива на расстояние ', distance, 'сoставляет', full_benzine_of_distance)