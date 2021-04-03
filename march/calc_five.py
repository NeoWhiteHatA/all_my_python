summa = int(input('Введите цену товара: '))
DISCOUNT = 0.15

summa_present_day = summa - (summa * DISCOUNT)
print('Ваша новая цена с учетом постоянной скидки: ', format(summa_present_day, '.2f'))