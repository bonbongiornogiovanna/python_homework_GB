# 1. Функция: деление


def division(arg1, arg2):
    try:
        return arg1 / arg2
    except ZeroDivisionError:
        return 'Данный калькулятор не поддерживает деление на ноль'


a = float(input('Введите делимое число: '))
b = float(input('Введите число-делитель: '))

res = division(a, b)
print(res)


# 2. Вывод данных о пользователе


def user_data(arg0, arg1, arg2, arg3, arg4, arg5):
    return f'Пользователя зовут {arg0} {arg1}, родил(ся/ась) {arg2}, проживает в {arg3}. Email: {arg4}, телефонный ' \
           f'номер: {arg5} '


name = input('Введите имя пользователя: ')
surname = input('Введите фамилию пользователя: ')
date_of_birth = input('Введите дату рождения: ')
city = input('Введите город проживания: ')
email = input('Введите Email: ')
tel = input('Введите телефон: ')

print(user_data(arg0=name, arg1=surname, arg2=date_of_birth, arg3=city, arg4=email, arg5=tel))


# 3. Сумма наибольших двух аргументов


def my_func(arg0, arg1, arg2):
    func_list = [arg0, arg1, arg2]

    try:
        func_list.remove(min(func_list))
        return sum(func_list)
    except TypeError:
        return 'Введенный тип данных не поддерживается'


num1 = float(input('Введите первое число '))
num2 = float(input('Введите второе число '))
num3 = float(input('Введите третье число '))

print(my_func(num1, num2, num3))


# 4.1. Возведение в отриц. степень: x ** y


def my_func():
    while True:
        try:
            x = float(input('Введите первое число (положительное): '))
            y = float(input('Введите второе число (отрицательное): '))

            if x > 0 and y < 0:
                return x ** y
            else:
                print('Первое число должно быть больше нуля, а второе - меньше нуля')
        except ValueError:
            print('Введенный тип данных не поддерживается')


print(my_func())

# 4.2. Возведение в отриц. степень: цикл


def my_func():
    while True:
        try:
            x = float(input('Введите первое число (положительное): '))
            y = float(input('Введите второе число (отрицательное): '))
            i = 0
            new_x = 1

            if x > 0 and y < 0:  # x = 2 y = 2
                while i <= abs(y) - 1:
                    if abs(y) == 1:
                        return 1 / x
                    else:
                        new_x *= x
                        i += 1
                return 1 / new_x
            else:
                print('Первое число должно быть больше нуля, а второе - меньше нуля')
        except ValueError:
            print('Введенный тип данных не поддерживается')


print(my_func())


# 5. Продолжительное суммирование со стоп-словом


def cont_sum():
    sum_list = []

    while True:
        try:
            stop_word = 'stop'
            nums = input(f'Введите числа через пробел, когда решите закончить напишите: {stop_word}: ').split()
            for el in nums:
                if el.isnumeric():
                    sum_list.append(float(el))
                else:
                    if el.lower() == stop_word:
                        return
            print(sum(sum_list))
        except TypeError:
            print('Введенный тип данных не поддерживается')


cont_sum()


# 6, 7 Выведение текстовых строк


def int_func(arg):
    return arg.title()


text = input('Введите слова состоящие из строчных латинских букв, разделяя их пробелом: ')
print(int_func(arg=text))
