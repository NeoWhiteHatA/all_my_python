#игра угадай число
import  random

secretNumber = random.randint(1, 30)
print('Мною задумано число в интервале от 1 до 30. рискни ушадать')

#предоставить игроку 6 попфток для угадывания
for guessesTaken in range(1, 7):
    print('Ваш вариант:')
    guess = int(input())

    if guess < secretNumber:
        print('Предложенное читсло меньше задуманного')
    elif guess > secretNumber:
        print('Предложенное число больше задуманного')
    else:
        break#правильный ответ
if guess == secretNumber:
    print('Вы угадали число с первой попытки')

