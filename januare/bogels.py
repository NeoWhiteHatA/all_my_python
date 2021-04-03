import random

NUM_DIGITS = 3
MAX_GUESS = 10


def getSecretNum():
    #возвращает строку уникальных случайныч цифр, длина которой состовляет NUM_DIGITS.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ' '
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    #возвращает строку с подсказками пользователю 'Тепло', 'горячо', 'холодно'.
    if guess == secretNum:
        return 'Вы угадали'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Горячо')
        elif guess[i] in secretNum:
            clues.append('Тeпло')
    if len(clues) == 0:
        return 'Холодно'
    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):
    #возвращает значение True, если num строка , состоящая только из цифр
    #в противном случае вернет False
    if num == ' ':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True
print('я загадаю %s-х число,которое вы должны отгадать.' % (NUM_DIGITS))
print('Я дам несколько подсказок')
print('Когда я вам напишу:   Это будет означать:')
print('Холодно - ни одна цифра не угадана')
print('Тепло - одна цифра угадана, но не отгадана ее позиция.')
print('Горячо - одна цифра угадана и ее позиция тоже.')

while True:
    secretNum = getSecretNum()
    print('Итак, я загадал число. У вас есть %s попыток, чтобы отгадать его.' % (MAX_GUESS))
    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ' '
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Попытка № %s: ' % (guessesTaken))
            guess = input()
            print(getClues(guess, secretNum))
            guessesTaken += 1
            if guess == secretNum:
                break
            if guessesTaken > MAX_GUESS:
                print('Попыток больше не осталось. я загадал число %s.' % (secretNum))
                print('Хотите сыграть еще разок?(да или нет)')
                if not input().lower().startswith('д'):
                    break