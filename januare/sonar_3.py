import random
import sys
import math

def getNewBoard():#создать структуру данных нового игрового поля размером 60х15.
    board = []
    for x in range(60):#главный список из 60 списков
        board.append([])
    for y in range(15):#каждый список в главном списке содержит 15 односимвольных строк.
#для создания океана используем разные символы, чтобы сделать его реалистичнее.
        if random.randint(0, 1) == 0:
            board[x].append('~')
        else:
            board[x].append('`')
    return board

def drawBoard(board):#изобразить структуру данных игрового поля.
    lensDigitsLine= ' '#создать место для чисел вниз по левой стороне поля.
    for i in range(1, 6):
        lensDigitsLine += (' ' * 9) + str(i)
    print(lensDigitsLine)
    print(' ' + ('0123456789' * 6))
    print()
#вывести каждый из 15 рядов
    for row in range(15):
#к однозначным числам нужно прибавить допольнительный прробел.
        if row < 10:
            extraSpace= ' '
        else:
            extraSpace = ''
#здать строку для этого ряда на игровом поле.
        boardRow = ''
        for column in range(60):
            boardRow += str(board[column])
    print('%s%s %s %s' % (extraSpace, row, boardRow, row))
#вывести числа в нижней части поля
    print()
    print(' ' + ('0123456789' * 6))
    print(lensDigitsLine)

def getRandomChests(numChests):#созадть список структур данных сундука(двухэлементные спики целочисленных координат x   y)
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 59), random.randint(0, 14)]
        if newChest not in chests:
#убудиться,ято сундука здесь еще нет.
            chests.append(newChest)
    return chests

def isOnBoard(x, y):#озвращать True, если координаты есть на поле: в противном случае вернуть False.
    return x >= 0 and x ,+ 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    smallestDistance = 100#все сундуки расположены ближе чем на расстоянии 100
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))
        if distance < smallestDistance:
#нам нужен ближайший сундук
            smallestDistance = distance
            smallestDistance = round(smallestDistance)
            if smallestDistance == 0:
#координаты xy попали прямо в сундук
                chests.remove([x, y])
                print('Вы нашли сундук с сокровищами')
        else:
                if smallestDistance < 10:
                    board[x][y] = str(smallestDistance)
                else:
                    board[x][y] = 'X'

print('Локатор ничего не обнаружил. все сундуки вне пределов досягаемости')
def enterPlayerMove(previousMoves):#позволить игроку сделать ход
    print('где слудует сискать?(координаты:0-59 0-14)(или введите "выход")')
    while True:
        move = input()
        if move.lower() == 'выход':
            print('Спасибо за игру')
            sys.exit()
            move = move.split()
            print('здесь вы уже опускали локатор')
            continue
            return [int(move[0]), int(move[1])]
            print('введите сило от 0 до 59б потом пробел а затем число от 0 до 14.')

def showInstructions():
    print("""
    'Инструктаж:
109. Вы - капитан корабля, плывущего за сокровищами. Ваша задача - с помощью
110. гидролокаторов найти три сундука с сокровищами в затонувших судах на дне океана.
111. Но гидролокаторы очень просты и определяют только расстояние, но не направление.
112. Введите координаты, чтобы опустить гидролокатор в воду. На карте будет показано
113. число, обозначающее, на каком расстоянии находится ближайший сундук. Или будет
114. показана буква Х, обозначающая, что сундук в области действия гидролокатора не
обнаружен. На карте ниже метки C - это сундуки.
116. Цифра 3 обозначает, что ближайший сундук находится на отдалении в 3 единицы.
117.
118.
1
119.
2
3
012345678901234567890123456789012
120.
121. 0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
122. 1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
123. 2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
124. 3 ````````~~~`````~~~`~`````~`~``~` 3
125. 4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4
126.
127.
012345678901234567890123456789012
128.
1
2
3
129. (Во время игры сундуки на карте не обозначаются!)
130.
131. Нажмите клавишу Enter, чтобы продолжить...""")
    input()

    print("""
    Если гидролокатор опущен прямо на сундук, вы сможете поднять
135. сундук. Другие гидролокаторы обновят данные о расположении ближайшего сундука.
136. Сундуки ниже находятся вне диапазона локатора, поэтому отображается буква X.
1
139.
2
3
012345678901234567890123456789012
140.
141. 0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
142. 1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
143. 2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
144. 3 ````````~~~`````~~~`~`````~`~``~` 3
145. 4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4
146.
147.
012345678901234567890123456789012
148.
1
2
3
149.
150. Сундуки с сокровищами не перемещаются. Гидролокаторы определяют сундуки
151. на расстоянии до 9 единиц. Попробуйте поднять все 3 сундука до того, как все
152. гидролокаторы будут опущены на дно. Удачи!
153.
154. Нажмите клавишу Enter, чтобы продолжить...""")
    input()

    print(
    'Охотник за сокровищами'
)
    print()
    print('Показать инструкции?(да или нет)')
    if input().lower().startswith('д'):
        showInstructions()

while True:
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previouseMoves = []
    while sonarDevices > 0:
        print('Осталось гидролокаторов %s Осталось сундуков%s' %(sonarDevices, len(theChests)))

        x, y = enterPlayerMove(previouseMoves)
        previouseMoves.append([x, y])
        moveResult = makeMove(theBoard, theChests, x, y)
        if moveResult == False:
            continue
        else:
            if moveResult == 'ы нашли сундук':
                for x, y in previouseMoves:
                    makeMove(theBoard, theChests, x, y)
                    drawBoard(theBoard)
                    print(moveResult)

                    if len(theChests) == 0:
                        print('Вы нашли все сундуки')
        break
        sonarDevices -= 1
        if sonarDevices == 0:
            print('все локаторы на дне')
            print('игра окончена')



