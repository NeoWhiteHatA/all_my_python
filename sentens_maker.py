def sentens_maker() -> str:
    n = input('Введите существительное: ')
    v = input('Введите глагол ')
    a = input('ведите прилагательное: ')
    o = input('Введите обстоятельство: ')
    senten = 'Вот ваше предложение, {} {} {} {}'.format(n, v, a, o)
    print(senten)