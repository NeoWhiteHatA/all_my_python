def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print(
            'Error: invalid syntax'
        )
print(spam(2))
print(spam(0))