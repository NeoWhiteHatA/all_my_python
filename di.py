def question() -> str:
    #добавление в словарь и вывод из него
    dict_question = {}
    dict_question['age'] = input('enter age: ')
    dict_question['color'] = input('enter color: ')
    dict_question['actor'] = input('enter actor: ')
    for d, t in dict_question.items():
        print(d, t)