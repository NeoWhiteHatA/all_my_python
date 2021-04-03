summa = float(input('Введите полную сумму вашей покупки без учета налогов: '))
federal = float(input('Введите полный федеральный узаконенный налог: '))
region = float(input('Введите ваш региональный налог: '))

print('Первоначальная сумма вашей покупки без учета налогов - ', summa)

federal_tax = summa * federal

print('Сумма федерального налога в абсолютной величине - ', federal_tax)

region_tax = summa * region

print('Cумма регионального налога в абсолютной величине - ', region_tax)

unit_tax = federal_tax + region_tax
print('Общий налог с продаж - ',unit_tax)

full_summ = summa + unit_tax

print('Полная стоимость товаров с учетом всех налогов - ', full_summ)