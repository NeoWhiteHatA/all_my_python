#желаемое будущее значение
future_value = int(input('Введите желаемое значение будущей суммы на вашем сберегательном счету: '))
rate = float(input('Введите годовую процентную ставку, предложенную в банке: '))
years = int(input('Введите предложенное банком количество лет сберегательного вклада: '))

present_value = future_value / (1.0 + rate) ** years
format_present_value = format(present_value, '.2f')
print('Результат расчетов нашего алгоритма ', format_present_value, 'именно такую сумму вам потребуется внести на ваш банковский счет')