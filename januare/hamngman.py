def hangman():
    import math
    w = math.randint
    words = ['cat', 'dog',
             'bird']
    wrong = 0
    word = 
    stages = ["",
              "__________        ",
              "|                 ",
              "|        |        ",
              "|        0        ",
              "|       /|\       ",
              
              "|       / \       ",
              "|                 "
              ]
    rletters = list(word)
    board = ["______"] * len(word)
    
    win = False
    print('Добро пожаловать на вашу казнь!')
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Enter letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
            print(("".join(board)))
            e = wrong + 1
            print("\n".join(stages[0: e]))
            if "__" not in board:
                print("You are winner")
                print(" ".join(board))
                win = True
                break
            if not win:
                print("\n".join(stages[0: wrong]))
                print("You not winner: {}".format(word))
                
hangman('cat')