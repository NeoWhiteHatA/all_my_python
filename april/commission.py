#эта программа вычисляет торговые комиссионые
#создаем переменную для управления циклом
keep_going = 'д'

#вычислить серию комиссионых вознаграждений
while keep_going == 'д':
#получить продажи продавца и его ставку комиссионных
    sales = float(input('Введите обем продаж '))
    comm_rate = float(input('Введите размер комиссионных: '))
    
    #рассчитать размер комиссионного вознаграждения
    commission = sales * comm_rate
    #показать комиссионное вознаграждение
    print('Комиссионное вознаграждение составляет $', 
          format(commission, '.2f'), sep = '')
    #убеждаемся, что пользователь хочет выполнить еще одно
    keep_going = input('Хотите вычислить еще одно' + '(Введите д если да): ')
