#Задача 1
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
        cook_book.update({key : values})
    print(cook_book)

#Задача 2
# dishes = input('Введите названия блюд : ').split()
# person_count = int(input('Введите количество персон : '))

def get_shop_list_by_dishes(dishes, person_count):
    order_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for book_dish, ingridients  in cook_book.items():
                if book_dish == dish:
                    for ingridient in ingridients:
                        if ingridient['ingridient_name'] not in order_list.keys():
                            key = ingridient['ingridient_name']
                            value = {'measure': ingridient['measure'], 'quantity': ingridient['quantity'] * person_count}
                            order_list.update({key : value})
                        else:
                            value['quantity'] += ingridient['quantity'] * person_count
        else:
            print(f'Выбранное блюдо: {dish} отсутствует в меню')
    return order_list
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
