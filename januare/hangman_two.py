#статртуем
#задумываем секретное слово
#показываем игроку виселицу и пропуски
#если буква присутствует
#игрок угадывает все буквы и побеждает
#спрашиваем игрока хочет ли он сыграть еще
#в противном случает
#буквы нет в загаданном слове
#игрок не угадывает и проигрывает
import random
HANGMAN_PICS = [
         '''    +-----+
                      |
                      |
                      |
                      |
                      |
                    ===== ''', 
                '''+-----+
                      |
                      |
                      |
                      |
                      |
                    =====''', 
                '''   +-----+
                    0     |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                        =====''', 
                 ''' +-----+
                    0
                    |
                          |
                          |
                          |
                          |
                        =====''',
                 '''+-----+
                    0     |
                   /|\    |
                          |
                          |
                          |
                        =====''',
        '''       +-----+
                    0     |
                   /|\    |
                   ( )    |
                   /      |
                        =====''',
               '''    +-----+
                    0     |
                   /|\    |
                   ( )    |
                   / \    |
                          |
                        =====''',
            ''' +-----+
            [0       |
              |       |
            /|\     |
            /  \      
                =====''',
         '''+-----+
           [0]      |
           /| \     |
            /\       |
                      |
               =====''',
]

#ввoдим необходимые слова для рэндомного выбора
wordDict= {
'Цвета': 'красный оранжевый желтый зеленый синий голубой фиолетовый белый черный коричневый'.split(),
'Фигуры': 'квадрат треугольник прямоугольник круг эллипс ромб трапеция параллелограмм пятиугольник шестиугольник восьмиугольник'.split(),
'Фрукты': 'яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик банан абрикос манго банан нектарин'.split(),
'Животные': 'аист бабуин баран барсук бык волк зебра кит коза корова кошка кролик крыса лев лиса лось медведь мул мышь норка носорог обезьяна овца олень осел панда пума скунс собака сова тигр тюлень хорек ящерица'.split()
}




#создаем функцию для рэндомного выбора слова
def getRandomWord(wordDict):
    #эта функция возвращает случайную строку из словаря спрашиваем
    #строк а также ключ.
    #для начала выбераем случайно ключ из словаря:
    wordKey = random.choice(list(wordDict.keys()))
    #во вторых случайным образом выбираем слово из
    #списка ключей в словаре
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return wordDict[wordKey, wordIndex]
def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы: ', end = '')
    for letter in missedLetters:
        print(letter, end = '')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): #заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:#показывает секретное слово
        print(letter, end = '')
    print()

def getGuess(alreadyGuessed):
    #возвращает букву введеную игроком
    #эта функция проверяет что игрок ввел одну букву
    while True:
        print('Введите букву')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву.')
        elif guess not in 'абвгдежзийклмнопрстуфхчшщъьэюя':
            print('Пожалуйста введите букву')
        else:
            return guess

def playAgain():
    #Эта функция возвращает TrueБ если игрок хочет сыграть еще раз
    print('Не желаете ли пройти этот  путь еще раз?(да или нет)')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')


difficulty = ''
while difficulty not in 'ЛСТ':
    print('Выберите уровень сложности:')
    print('Л-легкий, С - средний, Т - тяжелый')
    difficulty = input().upper()
if difficulty == 'С':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'Т':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]
missedLetters = ''
correctLetters = ''

secretWord, secretSet = getRandomWord(wordDict)
gameIsDone = False

while True:
    print('Секретное слово из набора: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    #позволяет игроку ввести букву
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #проверяет выиграл ли игрок
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('Да! секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

                #проверяет превысил ли игрок колличество попыток
    if len(missedLetters) == len(HANGMAN_PICS) - 1:
                    displayBoard(missedLetters, correctLetters, secretWord)

print('Вы исчерпали все попытки!\nНе угадано буквЖ '+ str(len(missedLetters)) + 'и угадано букв :' + str(len(correctLetters)) + 'было загадано слово' + secretWord + '.')
gameIsDone= True
                #запрашиваем у игрока, хочет ли он сыграть еще
if gameIsDone:
    if playAgain():
        missedLetters = ''
        correctLetters = ''
        gameIsDone = False
        secretWord, secretSet = getRandomWord(words)
    