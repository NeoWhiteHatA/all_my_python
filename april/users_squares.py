#та программа использует цикл для вывода таблицы числе  и их квадратов
#получить конечный предел от пользовтеля
print('Эта программа выводит список числе')
print('(начиная с 1) и их квадраты')

end = int(input('Насколько далеко мне заходить в вычислениях?: '))

#печать заголовков таблицы
print()
print('Число\tКвадрат числа')
print('===================')
#напечатать числа и их квадраты
for number in range(1, end + 1):
    square = number ** 2
    print('==================')
    print('   ', number,'\t', '   ', square)