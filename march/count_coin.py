print('Вам необходимо ввести небольшое количество монет')
print('Цель - получить в титоге один рубль')
print('имеются монеты достоинством в 5 копеекб 10 копеек и 50 копеек')


nominal_one_coin = 5
nominal_two_coin = 10
nominal_three_coin = 50

coin_one = int(input('Введите количество монет достоинством 5 копеек:'))
coin_two = int(input('Введите количество монет, достоинством в 10 копеек '))
coin_three = int(input('Введите количество монет, достоинством в 50 копеек '))

if nominal_one_coin * coin_one == 100:
    print('Вы выиграли рубль')
elif nominal_one_coin * coin_two == 100:
    print('Вы выиграли рубль')
elif nominal_three_coin * coin_three == 100:
    print('Вы выиграли рубль')
elif (nominal_one_coin * coin_one) + (nominal_two_coin * coin_two) == 100:
    print('Вы выиграли рубль')
elif (nominal_one_coin * coin_one) + (nominal_two_coin * coin_two) + (nominal_three_coin * coin_three) == 100:
    print('Вы выграли рубль')
else:
    print('ваших монет или слишком много или слишком мало')