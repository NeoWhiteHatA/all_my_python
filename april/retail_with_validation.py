#эта программа вычисляет розничные цены товаров и услуг.


MARK_UP = 2.5 #процент надбавки
another = 'д' #переменная управления циклом


#обрабатывать один или несколько товаров.
while another == 'д' or another == 'Д':
    #получить оптовую стоимость товара.
    wholesale = float(input('Введите оптовую стоимость товара: '))
    
    
    #проверить допустимость оптовой стоимости.
    while wholesale < 0:
        print('ОШИБКА!Стоимость товара не может быть меньше нуля')
        wholesale = float(input('введите правильную стоимость: '))
    #вычисление розничной цены
    retail = wholesale * MARK_UP
    
    # показать розничную цену.
    print('озничная цена: $', format(retail, '.2f'), sep='')
    
    #повторить?
    another = input('сть еще товар или товары? ' + '(введите д, если есть): ')