def count_characters(string):
    count_dict = {}
    for i in string:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    print(count_dict)