# Tic Tac Toe       
   
   import random       
          
  def drawBoard(board):       
     # This function prints out the board that it was passed.        
           
       # "board" is a list of 10 strings representing the board (ignore index 0)       
      print(board[7] + '|' + board[8] + '|' + board[9])       
10      print('-+-+-')      
11      print(board[4] + '|' + board[5] + '|' + board[6])       
12      print('-+-+-')      
13      print(board[1] + '|' + board[2] + '|' + board[3])       
14          
15  def inputPlayerLetter():        
16      # Lets the player type which letter they want to be.        
17      # Returns a list with the player's letter as the first item, and the computer's letter as the second.       
18      letter = ''     
19      while not (letter == 'X' or letter == 'O'):     
20          print('Do you want to be X or O?')      
21          letter = input().upper()        
22          
23      # the first element in the list is the player's letter, the second is the computer's letter.        
24      if letter == 'X':       
25          return ['X', 'O']       
26      else:       
27          return ['O', 'X']       
28          
29  def whoGoesFirst():     
30      # Randomly choose the player who goes first.        
31      if random.randint(0, 1) == 0:       
32          return 'computer'       
33      else:       
34          return 'player'     
35          
36  def makeMove(board, letter, move):      
37      board[move] = letter        
38          
39  def isWinner(bo, le):       
40      # Given a board and a player's letter, this function returns True if that player has won.       
41      # We use bo instead of board and le instead of letter so we don't have to type as much.     
42      return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top       
43      (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle        
44      (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom        
45      (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side       
46      (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle      
47      (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side      
48      (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal     
49      (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal       
50          
51  def getBoardCopy(board):        
52      # Make a copy of the board list and return it.      
53      boardCopy = []      
54      for i in board:     
55          boardCopy.append(i)     
56      return boardCopy        
57          
58  def isSpaceFree(board, move):       
59      # Return true if the passed move is free on the passed board.       
60      return board[move] == ' '       
61          
62  def getPlayerMove(board):       
63      # Let the player type in their move.        
64      move = ' '      
65      while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):     
66          print('What is your next move? (1-9)')      
67          move = input()      
68      return int(move)        
69          
70  def chooseRandomMoveFromList(board, movesList):     
71      # Returns a valid move from the passed list on the passed board.        
72      # Returns None if there is no valid move.       
73      possibleMoves = []      
74      for i in movesList:     
75          if isSpaceFree(board, i):       
76              possibleMoves.append(i)     
77          
78      if len(possibleMoves) != 0:     
79          return random.choice(possibleMoves)     
80      else:       
81          return None     
82          
83  def getComputerMove(board, computerLetter):     
84      # Given a board and the computer's letter, determine where to move and return that move.        
85      if computerLetter == 'X':       
86          playerLetter = 'O'      
87      else:       
88          playerLetter = 'X'      
89          
90      # Here is our algorithm for our Tic Tac Toe AI:     
91      # First, check if we can win in the next move       
92      for i in range(1, 10):      
93          boardCopy = getBoardCopy(board)     
94          if isSpaceFree(boardCopy, i):       
95              makeMove(boardCopy, computerLetter, i)      
96              if isWinner(boardCopy, computerLetter):     
97                  return i        
98          
99      # Check if the player could win on his next move, and block them.       
100     for i in range(1, 10):      
101         boardCopy = getBoardCopy(board)     
102         if isSpaceFree(boardCopy, i):       
103             makeMove(boardCopy, playerLetter, i)        
104             if isWinner(boardCopy, playerLetter):       
105                 return i        
106         
107     # Try to take one of the corners, if they are free.     
108     move = chooseRandomMoveFromList(board, [1, 3, 7, 9])        
109     if move != None:        
110         return move     
111         
112     # Try to take the center, if it is free.        
113     if isSpaceFree(board, 5):       
114         return 5        
115         
116     # Move on one of the sides.     
117     return chooseRandomMoveFromList(board, [2, 4, 6, 8])        
118         
119 def isBoardFull(board):     
120     # Return True if every space on the board has been taken. Otherwise return False.       
121     for i in range(1, 10):      
122         if isSpaceFree(board, i):       
123             return False        
124     return True     
125         
126         
127 print('Welcome to Tic Tac Toe!')        
128         
129 while True:     
130     # Reset the board       
131     theBoard = [' '] * 10       
132     playerLetter, computerLetter = inputPlayerLetter()      
133     turn = whoGoesFirst()       
134     print('The ' + turn + ' will go first.')        
135     gameIsPlaying = True        
136         
137     while gameIsPlaying:        
138         if turn == 'player':        
139             # Player's turn.        
140             drawBoard(theBoard)     
141             move = getPlayerMove(theBoard)      
142             makeMove(theBoard, playerLetter, move)      
143         
144             if isWinner(theBoard, playerLetter):        
145                 drawBoard(theBoard)     
146                 print('Hooray! You have won the game!')     
147                 gameIsPlaying = False       
148             else:       
149                 if isBoardFull(theBoard):       
150                     drawBoard(theBoard)     
151                     print('The game is a tie!')     
152                     break       
153                 else:       
154                     turn = 'computer'       
155         
156         else:       
157             # Computer's turn.      
158             move = getComputerMove(theBoard, computerLetter)        
159             makeMove(theBoard, computerLetter, move)        
160         
161             if isWinner(theBoard, computerLetter):      
162                 drawBoard(theBoard)     
163                 print('The computer has beaten you! You lose.')     
164                 gameIsPlaying = False       
165             else:       
166                 if isBoardFull(theBoard):       
167                     drawBoard(theBoard)     
168                     print('The game is a tie!')     
169                     break       
170                 else:       
171                     turn = 'player'     
172         
173     print('Do you want to play again? (yes or no)')     
174     if not input().lower().startswith('y'):     
175         break       
176 