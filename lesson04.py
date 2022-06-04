# 1. Скрипт расчета ЗП сотрудников

from sys import argv

if len(argv) == 4:
    path, worktime, hourrate, bonus = argv
    salary = int(worktime) * int(hourrate) + int(bonus)
    print(f'Заработная плата работника = {salary}.')
else:
    print('Введено неверное число аргументов (должно быть 3)!')

# 2. Генератор списков: отбор наибольших в паре элементов

old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([old_list[i + 1] for i in range(0, len(old_list)-1) if old_list[i + 1] > old_list[i]])

# 3. Генератор кратных чисел

print([el for el in range(20, 241) if el % 21 == 0 or el % 20 == 0])

# 4. Список без повторений

old_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([el for el in old_list if old_list.count(el) == 1])

# 5. Генератор списков: перемножение всех четных элементов

from functools import reduce


def multi(a, b):
    return a * b


print(reduce(multi, [num for num in range(100, 1001, 2)]))

# 6. "Бесконечные" генераторы

from itertools import count, cycle

num = int(input('Введите число начиная с которого генерировать список: '))

for i in count(num):
        print(i)
        if i >= 100:
            break

for i, char in enumerate(cycle('lol')):
    print(i, char)
    if i >= 100:
        break

# 7. Тренировка yield

from functools import reduce


def multi(a, b):
    return a * b


def fact():
    while True:
        arg = int(input('Введите целое положительное число: '))

        if str(arg).isnumeric():
            for num in range(1, int(arg) + 1):
                yield reduce(multi, range(1, num + 1))
            return
        else:
            print('Неверный тип аргумента, нужно число!')


for num in fact():
    print(num)
