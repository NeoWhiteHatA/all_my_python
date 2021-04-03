12
32#запрашиваем у пользователя количество учащихся обоего пола
man = int(input('Введите количество учащихся женского пола: '))
woman = int(input('Введите число учащихся женского пола: '))
# полное количесвто учеников обоих полов
united = man + woman

# процент мужского пола
procent_man = format(man / united, '.2f')

#процент женского пола
procent_woman = format(woman / united, '.2f')


print('В вашей группе мужчин: ', procent_man)
print('В вашей группе женщин: ', procent_woman)
