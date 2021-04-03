
count_bekery = int(input('Сколько вам требуется приготовить булочек? '))

users_glasses_sugar = format(count_bekery * 0.031, '.3f')
users_glasses_oil =  format(count_bekery * 0.020, '.3f')
users_glasses_gross = format(count_bekery * 0.057, '.3f')

print('Вам потребуется следующий перечень ингредиентов')
print(users_glasses_sugar, ' стаканов сахара')
print(users_glasses_oil, ' стаканов масла')
print(users_glasses_gross, ' стаканов муки')



