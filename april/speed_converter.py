#эта прога преобразует скорости от 60 км в час до 130 км в час с приращение 10 км
#  в американские мили
START_SPEED = 60        #начальная скорость
END_SPEED = 131         #конечная скорость

INCREMENT = 10          #приращение скорости 10 км

CONVERSION_FACTOR = 0.6214 #коэффициент пересчета

#печатаем заголовки таьлицы
print('KPH\tMPH') #kilometer per hour and miles per hour
print('----------------------------')

#выводим скорости
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print('     ',kph, '\t', format(mph, '.1f'))