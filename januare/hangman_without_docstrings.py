import random
HANGMAN_PICS = [
    '''
    +-----+
              |
              |
              |
              |
        =====
    '''
    ,
    '''
    +-----+
    0        |
              |
              |
              |
              |
        =====
    '''
    ,
    '''
    +-----+
    0       |
    |       |
             |
             |
        =====
    ''',
    '''
    +-----+
    0        |
  /|\       |
              |
              |
              |
        =====
        ''',
    '''
    +-----+
    0        |
   /|\       |
             |
    /\       |
        =====
        '''
    ]

words ='''аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея
индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось ля-
гушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон
попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица''' .split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
          
    print('wrong letters: ', end = '')
    for letter in missedLetters:
          print(letter, end = '')
          
          
    blanks = '_' * len(secretWord)
    
    
    for i in range(len(secretWord)):
          if secretWord[i] in correctLetters:
              blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
    
    
    for  letter in blanks:
          print(letter, end = '')
          
          
def getGuess(alreadyGuessed):
          while True:
                  print('enter letter')
          guess = input()
          guess = guess.lower()
          if len(guess) != 1:
              print('enter letter')
          elif guess in alreadyGuessed:
              print('shose another')
          elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
              print('enter letter')
          else:
              return guess
          
def playAgain():
          print('wonna play nexttime?(да или нет)')
          return input().lower().startswith('д')
          
print('В И С Е Л И Ц А')


missedLetters = ' '
correctLetters = ' '
secretWord = getRandomWord(words)
gameIsDone = False
          
          
while True:
          displayBoard(missedLetters, correctLetters, secretWord)
          guess= getGuess(missedLetters + correctLetters)
          if guess in secretWord:
              correctLetters = correctLetters + guess
          
              foundLetters = True
              for i in range(len(secretWord)):
                      if secretWord[i] not in correctLetters:
                              foundAllLetters = False
                              break
          if foundAllLetters:
                  print('Yes Secret word = " ' + secretWord+ ' "! You are winner!')
                  gameIsDone = True
          else:
              missedLetters =missedLetters + guess
          
          if len(missedLetters)== len(HANGMAN_PICS) - 1:
                  displayBoard(missedLetters, correctLetters, secretWord)
                  gameIsDone= True
                  if gameIsDone:
                      if playAgain():
                          missedLetters = ''
                          correctLetters = ''
                          gameIsDone= False
                          secretWord = getRandomWord(words)
                        else:
                            break

          
          
          
  