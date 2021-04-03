#стартуем
#показываем вступление
# игрок выбирает пещеру
#дальше проверяем добр дракон или зол
#если добр побеждаем
#если зол проигрываем
#спрашиваем игрока хотел бы он еще сыграть
import random
import time
cave = input()
def displayIntro():
    print("""
Вы находитесль в землях, населенных дораконами.
Перед собой вы видите две пещеры. В одной из них -
дружелюбный дракон. котоорый готов поделиться с вами
своими сокровищами. Во второй - жадный и голодный
драконб который мигом вас съест.""")
    print()
    
def chooseCave():
    cave = ' '
    while cave != '1' and cave != '2':
            print("""В какую пещеру вы рискнете войти(
            нажмите клавишу 1 или 2)""")
        cave = input()
    return cave

def checkCave(chosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(3)
    print('Ее темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print("""Большой дракон выпрыгивает перед вами!
    Он раскрывает свою пасть и ...""")
    print()
    time.sleep(2)
    
    friendlyCave = random.randint(1, 2)
    
    if chosenCave == str(friendlyCave):
        print('...делится с вами сокровищами')
    else:
        print('...моментально съедает вас')
        
playAgain = 'да'
while playAgain == 'да' or playAgain == 'д':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    
    print('попытаете удачу еще разок?(да или нет)')
    playAgain = input()
    
    
    