#крестики нолики
import random

def drawBoard(board):
    #эта функция рисует на экране игровое поле,
    #клетки которого будут заполнятся.
    #'board' это списко из 10 строк
    # для прорисоки игрового поля(индекс 0 игнорируеьтся)
    
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
    
    
def inputPlayerLetter():
        #разрешение игроку ввести буквуБ которую он выбирает
        #возвращает список, где буква игрока первый элемент
        #а буква компьютера второй
        
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Вы выбираете X или O(если что буквы латинские)')
            letter = input().upper()
        
        #первым элементом списка является буква игрока
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']
        
        
def whoGoesFirst():
    #случайный выбор первого игрока
    if random.randint(0, 1) == 0:
        return 'Компьютер ходит первым'
    else: 
        return 'Человек ходит первым'
    
def makeMove(board, letter, move):
    board[move] = letter
    
    
def isWinner(bo, le):
    #учитывая заполнение игрового поля и буквы игрока, 
    #эта функция возвращает True, усли игрок выиграл
    #будт использоваться 'bo'вместо 'board' это
    # и 'le'вместо letter ля сокращения кода
    return ((bo[7] == le and bo[8] == le and b0[9] == le) or #top
            (bo[1] == le and bo[2] == le and bo[3] == le) or #bottom 
            (bo[7] == le and bo[4] == le and bo [1] == le) or #left 
            (bo[8] == le and bo[5] == le and bo[2] == le) or #centr 
            (bo[9] == le and bo[6] == le and bo[3] == le) or #right 
            (bo[7] == le and bo[5] == le and bo[3] == le) or #diagonal 
            (bo[9] == le and bo[5] == le and bo[1] == le)) #diagonal
    
def getBoardCopy(board):
    #создает копию игрового поля и возвращает его 
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy 

def isSpaceFree(board, move):
    #dвозвращает True , если сделан ход в свободную клетку.
    return board[move] == ' '


def getPlayerMove(board):
    #разрешение игроку сделать ход
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Ваш следующий ход?(1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, moveList):
    #возвращает допустимый ход, учтитывая список сделанных ходов
    #и заполненных клеток на поле
    #возвращает значение NONE если больше нет допустимых ходов
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
            
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
    
    
def getComputerMove(board, computerLetter):
        #учитывая заполнение игрового поля и букву компьютера определяет
        #допустимый ход  и возвращает его
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'
            
            
            #алгоритм для имскустенного интеллект
            #сначала определим - победим ли мы почле слкедующего хода
for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
    return i
            #теперь проверяем победит ли игрок сделав следующий ход
             for i in range(1, 10):
                 boardCopy = getBoardCopy(board)
                if isSpaceFree(boardCopy, i):
                    makeMove(boardCopy, playerLetter, i)
                    if isWinner(boardCopy, playerLetter):
                            return i
            #пробуем занять один из углов, если есть свободные
            move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
            if move != None:
                return move
            #пробуем занять центр если там свободно
            if isSpaceFree(board, 5):
                return 5
            
            #делаем ход по одной стороне
            return chooseRandomMoveFromList((board, [2, 4, 6, 8]))
                                            
                                            
def isBoardFull(board):
    #возвращает True если клетка на игровом поле занята. иначе вернетFalse
        for i in range(1, 10):
            if isSpaceFree(board, i):
                return False 
        return True 
    
print('Игра в крестики- нолики')
while True:#перезагрузка игрового окна
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print(turn)
        print('Ходит первым')
        gameIsPlaying = True
while gameIsPlaying:
         if turn == 'Человек':
            #ход игрока
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            
            
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Вы победили')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья')
                    break 
                else:
                    turn = 'Компьютер'
                    else:
                #ход компа
                    move = getComputerMove(theBoard, computerLetter)
                     makeMove(theBoard, playerLetter, move)
            
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Компьютер победил')
                gameIsPlaying = False 
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья')
                    break
                else:
                    turn = 'Человек'
        print('Сыграем еще раз?(дф или нет)')
        if not input().lower().startswith('д'):
            break
            
                

