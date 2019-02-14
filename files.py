#Задача 1
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
            for recipe  in cook_book[dish]:
                key = recipe['ingridient_name']
                if recipe['ingridient_name'] not in order_list:
                    key = recipe['ingridient_name']
                    value = {'measure': recipe['measure'], 'quantity': recipe['quantity'] * person_count}
                    order_list.update({key : value})
                else:
                    count = order_list[recipe['ingridient_name']]['quantity'] + recipe['quantity']
                    value = {'measure': recipe['measure'], 'quantity': count * person_count}
                    order_list.update({key : value})
        else:
            print(f'Выбранное блюдо: {dish} отсутствует в меню')
    return order_list

with open('dishes.txt', encoding='utf8') as list_dishes:
    print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 1, list_dishes))
