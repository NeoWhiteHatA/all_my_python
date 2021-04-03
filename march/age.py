age = int(input(' ё  Введите ваш возраст: '))

if age <= 1:
    print('Вы младенец')
elif age > 1 and age < 13:
    print('рeбенок')
elif age > 13 and age < 20:
    print('Подросток')
else:
    print('Взрослый')