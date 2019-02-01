with open('dishes.txt', encoding='utf8') as list_dishes:
    cook_book = {}
    for dish in list_dishes:
        key = dish.strip()
        count = int(list_dishes.readline())
        values = list()
        for i in range(count):
            value = list_dishes.readline().strip()
            value = value.split(' | ')
            value_dict = {'ingridient_name': value[0], 'quantity': int(value[1]), 'measure': value[2]}
            values.append(value_dict)
        list_dishes.readline()
        cook_book.update({ key : values})
    print(cook_book)

