def from_user():
    qs = ['I have htree question for you', 'First - What is your name',
         'Second - What are you like color', 
         'threeth - What do you do',
         ]
    n = 0
    while True:
        print('Enter X for enter')
        a = input(qs[n])
        if a == 'X':
            break
        n = (n + 1) % 3