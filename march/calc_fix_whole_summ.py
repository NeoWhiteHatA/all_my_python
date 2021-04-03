first = float(input('введите стоимость первого товара: '))
second = float(input('Введите стоимость второго товара: '))
three = float(input('введите стоимость третьего товара: '))
foo = float(input('Введите стоимость четвертого товара: '))
five = float(input('Введите стоимость пятого товара '))

fix_from_sales = float(input('ведите процентную ставку налога на товары: '))

full_summ = first + second + three + foo + five 

fix_from_full_summ = full_summ * fix_from_sales

full_summ_with_fix = full_summ + fix_from_full_summ

print('Полная сумма вашей покупки с учетом всех налогов: ', full_summ_with_fix)