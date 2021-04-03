plan_summ = int(input('Введите плановую сумму общего обьема продаж: '))
plan_procent = float(input('Введите плановую процентную ставку: '))

clean_profit = plan_summ * plan_procent

print('Прибыль от первоначальной суммы, с учетом ставки: ' , clean_profit)