rock = []
country = []

def collection_songs() -> str:
    song = 'Enter song: '
    ask = 'Enter r (rock) or c Country). Enter X for exit'
    while True:
        genre = input(ask)
        if genre == 'X':
            break
            
        if genre == 'r':
            rk = input(song)
            rock.append(rk)
                
        elif genre == ('c'):
            cy = input(song)
            country.append(cy)
            
        else:
            print('Wrong')
    print(rock)
    print(country)
        
        