print('Эта программа вычисляет цену товара,учитывая скидку в процентах.Следует вводить проценты как десятичную дробь для корректной работы программы. Спасибо!')
originPrice = float(input('Enter original price: '))
downPay = float(input('Enter down prices: '))

discount = originPrice * downPay

salePrice = originPrice - discount

print('Now price ', salePrice)
