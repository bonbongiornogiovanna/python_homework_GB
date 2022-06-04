# 1. Вывод типа данных списка


li = ['something', 12, 23.5, False, None]
for i in li:
    print(type(i))

# 2. Обмен значений элементов списка

li = input('Введите элементы через пробел: ').split()
i = 0

while i < len(li) - 1:
    li[i], li[i + 1] = li[i + 1], li[i]
    i += 2
print(li)

# 3.1 Вывод времени года (dictionary)

mon_dict = {'Зима': [12, 1, 2],
            'Весна': [3, 4, 5],
            'Лето': [6, 7, 8],
            'Осень': [9, 10, 11]}

mon = int(input('Введите число месяца: '))
for i, el in enumerate(list(mon_dict.values())):
    if mon in el:
        ind = i
        print(list(mon_dict.keys())[ind])

# 3.2 Вывод времени года (list)

mon_list = [('Зима', '12, 1, 2'), ('Весна', '3, 4, 5'), ('Лето', '6, 7, 8'), ('Осень', '9, 10, 11')]

mon = input('Введите число месяца: ')

for el in mon_list:
    if mon in el[1]:
        print(el[0])

# 4. Вывод слов с нумерацией. Сделал нумерацию с единицы

str_list = input('Введите слова через пробел: ').split()

for i, val in enumerate(str_list):
    print(f'{i +1}. {val[:10]}')

# 5. Заполнение "Рейтинга"

my_list = [7, 5, 3, 3, 2]

new_num = int(input('Введите новый элемент рейтинга (число): '))

if new_num in my_list:
    i = my_list.index(new_num)
    cou = my_list.count(new_num)
    my_list.insert(i + cou, new_num)
else:
    my_list.insert(0, new_num)
    my_list.sort(reverse=True)
print(my_list)

# 6. Структура данных "Товары"

cou = int(input('Введите число добавляемых позиций для товара: '))
arr = range(0, cou)
data_list = []
param = ['название', 'цена', 'количество', 'единица измерения']  # названия полей (параметры) структуры данных
attr_list = []

if cou != 0:
    for arr_ind in arr:
        name = input(f'Введите {param[0]} товара: ')
        pr = int(input(f'Указанная {param[1]} товара: '))
        qt = int(input(f'Введите {param[2]} товара: '))
        unit = input(f'Указанная {param[3]} товара: ')

        attr_list = [name, pr, qt, unit]

        di = dict.fromkeys(param)

        for ind in range(0, 4):
            di.update({param[ind]: attr_list[ind]})

        tup = tuple((arr_ind + 1, di))
        data_list.append(tup)

    di = dict.fromkeys(param)
    temp_list = []

    for ind in range(0, 4):
        for cou_ind in range(0, cou):
            temp_list.append((data_list[cou_ind][1]).get(param[ind]))

        di.update({param[ind]: temp_list})
        temp_list = []

    print(di)

else:
    print('Отмена ввода')
