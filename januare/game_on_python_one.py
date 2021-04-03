#this game for shose unit
import random
#import module random
guesseTaken = 0
#begin mean
#welcome
print('Hello! What is your name?')

myName = input()


number = random.randint(1, 26)

print('Ok, ' + myName + ', i am numbers secret from 1 to 25.')

#exit trying player
for guesseTaken in range(10):
    print('Try number')
    
    guess = input()
    
    #проверяем введеное знвачение путем
#     преобразования его к числу int

    guess = int(guess)
    
    if guess < number:
        print('Ваше число слишком маленькое')
    if guess == number:
        break
if guess == number:
    guesseTaken = str(guesseTaken + 1)
    
    print('Отлично, ' + myName + '! ты справился за ' + guesseTaken + 'попытки!')
    
if guess != number:
    number = str(number)
    print('Увы и ах... Я загадал число  ' + number + '.')
