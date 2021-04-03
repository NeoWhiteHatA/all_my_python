dev_prod = 99

dev_prod_sales = int(input('Сколько штук нашего продукта вы приобрели? 0 > 100: '))
if dev_prod_sales >= 10 and dev_prod_sales <= 19:
    print('ваша скидка: ', dev_prod_sales * 0.1)
elif dev_prod_sales >= 20 and dev_prod_sales <= 49:
    print('Ваша скидка ', dev_prod_sales * 0.2)
elif dev_prod_sales >= 50 and dev_prod_sales <= 99:
    print('Ваша скидка: ', dev_prod_sales * 0.3)
elif dev_prod_sales >= 100:
    print('Ваша скидка: ', dev_prod_sales * 0.4)
else:
    print('За вашу покупку не предусмотрено скидки')
