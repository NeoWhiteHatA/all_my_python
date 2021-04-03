#охотник за сокровищами

import random
import sys
import math


def getNewBoard():#создать структуру данных нового игрового поля размером 60 на 15
    board = []
    for x in range(60):#главный список из 60 списков
        board.append([])
    for y in range(15):#каждый список в главном окне содержит 15 односимвольных строк
        #я создания океана используем разные символы, чтобы сделать егог реалистичнее
        if random.randint(0, 1) == 0:
            board[x].append('~')
        else:
            board[x].append('~')
    return board
def drawBoard(board):#изобразить структуру данных игрового поля
    tensDigitsLine = ' '  # создать место для чисел вниз по левой стороне поля
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)
    #вывести числа в верхней части поля
    print(tensDigitsLine)
    print(' ' + ('0123456789' * 6))
    print()
    #вывести каждый из 15 рядов
    for row in range(15):
        #к однозначным числам прибавляем пробел
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace =''
        #оздать строку для этого ряда на игровом поле
        boardRow =''
        for column in range(60):
            boardRow += board[column][row]
            print('%s%s %s %s' %(extraSpace, row, boardRow, row))#вести числа в нижней части поля
            print(' ' + ('0123456789' *6))
            print(tensDigitsLine)
    
def getRandomChests(numChests):
    #создать список структур данных сундука(двухэлементные списки целочисленных координат  y)
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 59), random.randint(0, 14)]
    if newChest not in chests:#убедиться что сундука здесь еще нет
            chests.append(newChest)
    return chests
def isOnBoard(x, y):
    #вернет eесли координаты есть на поле в противном случае возвращает alse
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    #изменить структуру данных поля, используя символ гидролокатора
    #удалить сундуки с сокровищами из списка с сундуками,как только нашли их
    #Вернуть False если это недопустимый ход в противном случае вернуть строку с результатом 
    #этого хода
    smallestDistance = 100
    #все сундуки будут расположены ближе чем на рассторянии 100
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))
        if distance < smallestDistance:
            #нам нужен ближайший сундук
            smallestDistance = distance
            smallestDistance = round(smallestDistance)
            if smallestDistance == 0:
                #координаты xy попали прямо в сундук с сокровищами
                chests.remove([x, y])
        return ' нашли сундук с сокровищами'
    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
    return 'Сундук с сокровищами обнаружен на расстоянии %s от гидролокатора' % (smallestDistance)
    return board[x][y] == 'X'
print('Гидролокатор ничего не обнаружил.')

def enterPlayerMove(previosMoves):# позволить игроку сделать ход вернуть двухэлементный список с целыми координатами  x y
    print('Гдe следует опустить гидролокатор?(координаты 0-59 и 0-14)(или введите слово "выход")')
    while True:
        move = input()
        if move.lower() == 'выход':
            print('Всего доброго')
            sys.exit()
        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
                if [int(move[0]), int(move[1])] in previousMoves:
                    print('Здесь вы уже опускали локатор')
                    continue
                return [int(move[0]), int(move[1])]
                print('введите число от 0 до 59 потом пробел а затем число от 0 до 14')

def showInstructions():
    print("""
    Инструктаж
    вы капитан корабля плывущего за сокровищами.ваша задача с помощью локатора найти три сунудука с сокровищами.
    локаторы определяют только расстояние но не направление.
    введите координаты, чтобы опустить локатор в воду.
    на карте будет показано число, обозначающее, на каком расстоянии находится ближайший 
    сундук с золотом.
    или же будет показана буква Х, обозначающая, что сунудук в области дейстивия прибора
    не обнаружен 
    цифра 3 означает, что ближайший сундук находится на отдалении в 3 единицы.""")
    print('Нажмите клавишу enter чтобы получить подробные сведения')

    print("""
    усли гидролокатор опущен прямо в сундук, вы можете поднять сундук.
    другие локаторы обновят данные о расположении ближайшего сунудука
    сунудуки с сокровищами не перемещаются. Гидролокаторы определяют сунудуки на расстоянии до 3 единиц. 
    попробуйте поднять все 3 сундука до того как
    все гидролокаторы будут опущены на дно.Удачи!""")
    print('Нажмите Enter чтобы продолжить')
    print('Охотник за сокровищами')
    print()
    print('Показать инструктаж?(да/нет)')
    if input().lower().startswith('д'):
        showInstructions()


while True:#настройка игры
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []
    while sonarDevices > 0:
        print('Осталось гидролокаторов %s, осталось сундуков %s' % (sonarDevices, len(theChests)))
        x, y = enterPlayerMove(previousMoves)
previousMoves.append([x, y])#отслеживание всех ходов для обновления локаторов
moveResult = makeMove(theBoard, theChests, x, y)
if moveResult == False:
    print('hi')
else:
    if moveResult == 'Вы нашли сундук с сокровищами на затонувшем судне':
        for x, y in previoseMoves:
            makeMove(theBoard, theChests, x, y)
            drawBoard(theBoard)
            print(moveResult)
        if len(theChests) == 0:
            print('Вы нашли сундуки с сокровищами')
            sonarDevices -= 1
            if sonarDevices == 0:
                print('все гидролокаторы опущены на дно')
                print('Вы не нашли сундуки в следующих местах:')
                for x, y in theChests:
                    print('%s, %s,' % (x, y))
                    print('Хотите попробовать еще разок?(да или нет)')
                    if not input().lower().startswith('д'):
                            sys.exit()
    
