# 1. создание файла и запись
import json

f_obj = open('first.txt', 'w', encoding='utf-8')
txt = []


def loop_listing():
    while True:
        line = input('Введите текст для добавления в файл (чтобы закончить - введите пустое значение): ')
        if line != '':
            txt.append(line)
        else:
            return


loop_listing()
txt = '\n'.join(txt)
f_obj.write(txt)
f_obj.close()

# 2. подсчет строк и слов в файле

with open('second.txt', 'r', encoding='utf-8') as f_obj:
    lines = f_obj.readlines()
    rows = len(lines)
    words = [str(len(el.split())) for i, el in enumerate(lines)]
print(f'В файле {rows} строки')
for i, val in enumerate(words):
    print(f'В {i + 1} строке: {val} слов')

# 3. учет окладов

with open('third.txt', 'r', encoding='utf-8') as f_obj:
    lines = f_obj.readlines()
    headcount = len(lines)
    wage_list = [tuple(line.split()) for line in lines]
    underwage_list = [tuple(line.split()) for line in lines if float(tuple(line.split())[1]) < 20000.00]
    surname_list = [el[0] for el in underwage_list]
    avg_wage = sum([float(el[1]) for el in wage_list]) / headcount

print('Сотрудники с окладом ниже 20 000 руб.')
for sur in surname_list:
    print(sur)
print(f'Средний оклад составляет {round(avg_wage, 2)} руб.')

# 4. перевод

with open('fourth_eng.txt', 'r', encoding='utf-8') as f_obj:
    trans_dict = {'One': 'Один',
                  'Two': 'Два',
                  'Three': 'Три',
                  'Four': 'Четыре'
                  }
    res = []

    lines = [list(el.replace('\n', '').split(' — ')) for el in f_obj.readlines()]
    for el in lines:
        el[0] = trans_dict.get(el[0])
        res.append(' — '.join(el))

with open('fourth_rus.txt', 'w', encoding='utf-8') as f_obj:
    f_obj.write('\n'.join(res))

# 5. суммирование чисел

with open('fifth.txt', 'w', encoding='utf-8') as f_obj:
    def inp():
        while True:
            line = input('Введите числа через пробел: ')
            if line != '':
                f_obj.write(line)
                return
            else:
                print('Пустой ввод')
    inp()

with open('fifth.txt', 'r', encoding='utf-8') as f_obj:   # не могу понять в чем тут смысл предупреждения, я же
    # использовал объект в строке 71?
    print(sum([int(el) for el in f_obj.readline().split()]))

# 6. суммирование по предметам, немного замудрил, был уставший)
import re

f_obj = open('sixth.txt', 'r', encoding='utf-8')
lines = f_obj.readlines()
res = None
res_list = []
calc_list = []
linesum = None
trans_dict = {0: 'Информатика',
              1: 'Физика',
              2: 'Физкультура',
              3: 'Математика'
              }
res_dict = {}

for i, line in enumerate(lines):
    num_list = []
    for word in line.split():
        num = re.findall('\d+', word)
        if len(num) != 0:
            num_list.append(int(num[0]))
        else:
            pass
    linesum = sum(num_list)
    res = i, linesum
    res_list.append(list(res))

for el in res_list:
    el[0] = trans_dict.get(el[0])

res_dict = {el[0]: el[1] for el in res_list}
print(res_dict)

f_obj.close()

# 7. подсчет прибыли в JSON
import json

f_obj0 = open('seventh.txt', 'r', encoding='utf-8')
lines = f_obj0.readlines()
res = None
prof_list = []
prof_dict = {}
avg_prof = []
avg_dict = {}
result = []

for i, line in enumerate(lines):
    num_list = []
    for word in line.split():
        num = re.findall('\d+', word)
        if len(num) != 0:
            num_list.append(int(num[0]))
        else:
            pass
    if int(num_list[0]) > int(num_list[1]):
        prof = num_list[0] - num_list[1]
        res = i, prof
        prof_list.append(list(res))

firm_num = len(prof_list)
avg_prof = sum([el[1] for el in prof_list]) / firm_num
avg_dict = {'avg_profit': avg_prof}
prof_dict = {f'firm {i + 1}': el[1] for i, el in enumerate(prof_list)}
result.append(prof_dict)
result.append(avg_dict)
print(result)

f_obj1 = open('seventh_fin.json', 'w', encoding='utf-8')
json.dump(result, f_obj1)
f_obj1.close()

f_obj0.close()
