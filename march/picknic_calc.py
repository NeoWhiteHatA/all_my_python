on_pack_fin = 10
on_pac_bakery = 8


count_people_for_picnic = int(input('  Введите количество участников пикника: '))
count_hot_dogs = int(input('   Введите количество хотдогов на одного участника: '))


unit_count_hot_dogs = count_hot_dogs * count_people_for_picnic

count_fin = unit_count_hot_dogs // on_pack_fin
count_bekkery = unit_count_hot_dogs // on_pac_bakery

print('Минимально необходимое количество упаковок сосисек на ', count_people_for_picnic, 'человек', count_fin)

print('Минимальное количество упаковок булочек на', count_people_for_picnic,'людей', count_bekkery)


count_fin_unit = unit_count_hot_dogs % on_pack_fin
count_bekkery_unit = unit_count_hot_dogs % on_pac_bakery

print('Остаток сосисек', count_fin_unit)
print('Остаток булочек', count_bekkery_unit)