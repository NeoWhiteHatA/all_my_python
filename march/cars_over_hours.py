from typing import Pattern


BASE_HOURS = 40
MULTIP = 1.5
#именнованные константы представляют базовые часы и 
#коэффициент умножения сверхурочной ставки соответственно

#получаем отработанные часы
hours = float(input('Введите количество отработанных вами часов: '))
pay_rate = float(input('Введите вашу почасовую ставку оплаты труда: '))


#расчет заработной платы до удержаний
if hours > BASE_HOURS:
    #расчитать зарплату без сверхурочных
    #получаем количество отработанных сверхурочныхз часов
    overtime_hours = hours - BASE_HOURS
    #далее расчитываем оплату во сверхурочное время
    overtime_pay = overtime_hours * pay_rate * MULTIP
    #расчет зарплаты до удержаний
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    #расчитать зарплату до удержаний без сверхурочных
    gross_pay = hours * pay_rate
    
#вывести на экран результаты
print('Зарплата до удержаний составляет : $', format(gross_pay, ',.2f'), sep='')