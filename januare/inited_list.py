def united_list():
    list_one = [
        'one', 'two', 'three',
        'footh', 'fivth', 'sixth',
        'zero'
        ]
    list_two = [
        'a', 'b', 'c', 
        'd', 'e', 'f',
        'g'
    ]
    united_lists = []
    
    for numbers in list_one:
        numbers = numbers.upper()
        united_lists.append(numbers)
    for letters in list_two:
        letters = letters.upper()
        united_lists.append(letters)

    print(united_lists)