
import random


def drawBoard(board):
#эта функция рисует поле клетки которого заполняются
#'board'список из 10 строк  для прорисовки игрового поля индекс 0 игнорируется

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4]+ '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def inputPlayerLetter():
    #разрешение игроку ввести букву
    #возвращает список в котором буква игрока первый элемент компа второй
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Вы выбираете X или O (латиница)')
        letter = input().upper()
    #первым элементом списка является буква игрока вторым компьютера
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
def whoGoesFirst():
    #случайный выбор игрока ходящего первым
    if random.randint(0, 1) == 0:
        return 'Комп'
    else:
        return 'Человек'
def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    #учитывая заполнение игрового поля и буквы игрока эта функция возвращает True
    #если игрок выиграл
    #мы используем 'bo' и 'le' как синонимы board  и  letter
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or #across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # across centr
            (bo[1] == le and bo[2] == le and bo[3] == le) or # across bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))
def getBoardCopy(board):
    #создает копию игрового поля
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    #возвращает true если сделан ход в свободную клетку
    return board[move] == ' '

def getPlayerMove(board):
    #разрешение игроку сделть ход
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Ваш следующий ход (1 - 9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, moveList):
    #возвращает допустимый ход учитывая список сделанных ходов и список заполненных клеток
    #возвращает значение None усли больше нет допустимых ходов
    possibleMoves= []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
def getComputerMove(board, computerLetter):
    #учитывая заполнение игрового поля и букву компьютера определяет допустимый ход и возвращает его
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    #алгоритм кретиков и ноликов
    #сначана проверяем победим ли мы сделав еще ход
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
    for i in range(1, 10):
        #проверяем победит ли игрок сделав следующий ход и блокируем его
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
    if isSpaceFree(board, 5):
        return 5
    #пробуем занять цунтр если он свободен
    #дальше делаем ход по одной стороне
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    #вернет True если клетка в игровом поле занята в противном случае  False
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Играем в крестики нолики')

while True:
    #перезагрузка игрового поля
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(' ' + turn + ' ходит первым')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'Человек':
            #ход игрока
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Вы выиграли')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья')
                    break
                else:
                    turn = 'Компьютер'
        else:
            #ходкомпьютера
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Комп победил')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья')
                    break
                else:
                    turn = 'Человек'
    print('Сыграем еще разок?(да или нет')
    if not input().lower().startswith('д'):
        break