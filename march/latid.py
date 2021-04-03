#запрашиваем длину и ширину первого прямоугольника
side_one_first = float(input('    Введите длину стороны первого прямоугольника: '))
side_one_second = float(input('    Введите длину второй стороны прямоугольника: '))

#запрашиваем длину и ширину второго прямоугольник
side_two_first = float(input('    Введите длину стороны второго прямоугольника: '))
side_two_second = float(input('    Введите длину второй стороны прямоугольника: '))


s_first = side_one_first * side_one_second

s_second = side_two_first * side_two_second

if s_first > s_second:
    print('Площадь первого прямоугольника больше площади второго прямоугольника')
elif s_first < s_second:
    print('Площадь первого прямоугольника меньше площади второго')
else:
    print('Площади прямоугольников равны')
    