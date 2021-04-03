sota = int(input('Введите цифру или число от 0 до 36:'))

if sota == 0:
    print('green')
elif sota >= 1 and sota <= 10 and sota // 2 == 0:
    print('red')
elif sota >= 1 and sota <= 10 and sota // 2 != 0:
    print('black')
elif sota >= 11 and sota <= 18 and sota // 2 == 0:
    print('black')
elif sota >= 11 and sota <= 18 and sota // 2 != 0:
    print('red')
elif sota >= 19 and sota <= 28 and sota // 2 == 0:
    print('red')
elif sota >= 19 and sota <= 28 and sota // 2 != 0:
    print('black')
elif sota >= 29 and sota <= 36 and sota // 2 ==0:
    print('black')
elif sota >= 29 and sota <= 36 and sota // 2 != 0:
    print('red')
else:
    print('error')
