# 1. Узнай свое имя и возраст:

name = input('Введите Ваше имя: ')
age = int(input('Введите Ваш возраст: '))

print('Вас зовут %s' % name)
print('Вам %d лет' % age)

print(type(age))

# 2. Конвертер: секунды в время по формату hh:mm:ss

secs = int(input('Введите время в секундах: '))

secs = secs % (24 * 3600)
hours = secs // 3600
secs %= 3600
mins = secs // 60
secs %= 60

res = '{:02}:{:02}:{:02}'.format(hours, mins, secs)
print(res)

# 3. Экстравагантый калькулятор

n = input('Введите число: ')

print(int(n) + int(n*2) + int(n*3))

# 4. Максимальная цифра в цисле

num = int(input('Введите целое положительное число: '))
max_num = None

while num > 0:
    max_num = num % 10
    if max_num == 9:
        break
    num //= 10
    if max_num < num % 10:
        max_num = num % 10
print(max_num)

# 5, 6 Микро ОДР

rev = int(input('Введите значение выручки организации: '))
cost = int(input('Введите значение издержек организации: '))
profit = (rev - cost)
profitability = (profit / rev)

if rev > cost:
    print('Поздравляем, у Вас имеется прибыль!')
    print('Ваша рентабельность по выручке составила {:%}' .format(profitability))
    empl = int(input('Введите численность сотрудников Вашей организации: '))
    print('Прибыль организации в расчете на одного сотрудника составила', round((profit / empl), 2))
elif rev == cost:
    print('Неплохо, Вы работаете без убытка, но жаль, что нет прибыли.')
else:
    print('Пора заняться оптимизацией, у Вас убыток!')

# 7. Расчет времени выполнения велосиплана

a = int(input('Введите количество километров в первый день (a): '))
b = int(input('Введите целевое количество километров (b): '))
day = 0

while a < b:
    a *= 1.1
    day += 1
print(day + 1)
