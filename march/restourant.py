price_foode = float(input('введите стоимость заказанного меню в ресторане: '))
tea_tax = 0.18
tax_for_sales = 0.07
full_tax = tea_tax + tax_for_sales

price_with_tea_tax = price_foode + (price_foode * tea_tax)

price_with_tax_sales = price_foode + (price_foode * tax_for_sales)

full_price = price_foode + (price_foode * full_tax)

print('Стоимость еды до налогов: ', price_foode)
print('Стоимость еды с чаевыми: ', price_with_tea_tax)
print('Стоимость еды с налогом на продажы: ', price_with_tax_sales)
print('Полная стоимость еды вместе с налогами и сборами: ', full_price)