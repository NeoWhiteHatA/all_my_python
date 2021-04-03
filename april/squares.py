#эта программа использует цикл для вывода
#таблицы с числами от 1 до 10
#и их квадратами

#Напечатать заголовки таблицы
print('Number\t Square number')
print('----------------------------------------')
#напечатать числа от 1 до 10 и их квадраты
for number in range(1, 11):
    square = number ** 2
    qub = number ** 3
    quatro = number ** 4
    print('      ', number,'\t', square, '\t', qub, '\t', quatro)