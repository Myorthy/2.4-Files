##Задача 1
def read_book(book):
    new_book = {}
    for dish in book:
        key = dish.strip()
        count = int(book.readline())
        values = list()
        for i in range(count):
            value = book.readline().strip()
            value = value.split(' | ')
            value_dict = {'ingridient_name': value[0], 'quantity': int(value[1]), 'measure': value[2]}
            values.append(value_dict)
        book.readline()
        new_book[key] = values
    return new_book

# with open('dishes.txt', encoding='utf8') as list_dishes:
#      print(read_book(list_dishes))

#Задача 2
def get_shop_list_by_dishes(dishes, person_count, list):
    order_list = {}
    cook_book = read_book(list)
    for dish in dishes:
        if dish in cook_book:
            for book_dish, ingridients  in cook_book.items():
                if book_dish == dish:
                    for ingridient in ingridients:
                        if ingridient['ingridient_name'] not in order_list.keys():
                            key = ingridient['ingridient_name']
                            value = {'measure': ingridient['measure'], 'quantity': ingridient['quantity'] * person_count}
                            order_list.update({key : value})
                        else:
                            key = ingridient['ingridient_name']
                            value['quantity'] += ingridient['quantity'] * person_count
                            order_list.update({key : value})
        else:
            print(f'Выбранное блюдо: {dish} отсутствует в меню')
    return order_list

with open('dishes.txt', encoding='utf8') as list_dishes:
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, list_dishes))
