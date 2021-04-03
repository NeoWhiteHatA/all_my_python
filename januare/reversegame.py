#рувурси  клон игры Отелло
import random
import sys

WIDTH = 8#игровое поле содержит 8 клеток по ширине
HEIGHT = 8#игровое поле содкержит 8 клеток по высоте

def drawBoard(board):#вывести игровое поле, переданное этой функции. Ничего не возвращать
    print('  12345678')
    print('  +-------+')
    for y in range(HEIGHT):
        print('%s|' % (y + 1), end = '')
        for x in range(WIDTH):
            print(board[x][y], end = '')
        print('|%s' % (y + 1))
    print('  12345678')

def getNewBoard():#создаем структуру данных нового чистого игрового поля.
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',])
    return board

def isValidMove(board, tile, xstart, ystart):#вернуть False если ход игрока в клетку с координатами xstart?
#ystart-недопустимый.усли допустимый ход, вернуть список клеток
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False
    if tile == 'X':
        otherTile == '0'
    else:
        otherTile == 'X'
    tilesToFlip = []
for xdirection, ydirection in[[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
    x, y = xstart, ystart
    x += xdirection#пурвый шаг в направлении x
    y += ydirection#первый шаг в направлении y
    while isInBoard(x, y) and board[x][y] == otherTile:#продолжать двигаться в этом направлении
        x += xdirection
        y += ydirection
        if isOnBoard(x, y) and board[x][y] == tile:#есть фишки которые можно перевернуть
            while True:
                x -= xdirection
                y -= ydirection
                if x == xstart and y == ystart:
                    break
                tilesToFlip.append([x, y])
if len(tilesToFlip) == 0:#если ни одна из фишек не перевернулсь это недопустимый ход
    return False
