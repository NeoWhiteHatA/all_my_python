def total( *numbers, extra_number, number=5):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)
