def collatz () -> int:
    print('Введите число')
    number = input()
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1
    elif number == 0:
        return 'Error! Enter number'
