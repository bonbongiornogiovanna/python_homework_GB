# 1. работа с датой


class Date:
    def __init__(self, dd: int, mm: int, yyy: int) -> None:
        self.dd = dd
        self.mm = mm
        self.yyy = yyy

    def __str__(self):
        return f'{self.dd:02}.{self.mm:02}.{self.yyy:04}'

    @classmethod
    def date_convert(cls, date):
        dd, mm, yyy = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        return cls(int(dd), int(mm), int(yyy))

    @staticmethod
    def date_validation():
        if 1 <= Date.date_convert(date).dd <= 31 and 1 <= Date.date_convert(date).mm <= 12 and 1900 <= Date.date_convert(date).yyy <= 2022:
            return 'Введена корректная дата'
        else:
            return 'Введена некорректная дата'


date = '03-03-1996'
d0 = Date.date_convert(date)
print(d0)
print(Date.date_validation())

# 2. собственные исключения 1


class AltZeroDivisionException(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    numerator = int(input('Введите делимое число: '))
    denominator = int(input('Введите число - делитель: '))
    if denominator == 0:
        raise AltZeroDivisionException('Запрещено деление на ноль!')
except (ValueError, AltZeroDivisionException) as err:
    print(err)
else:
    print(numerator / denominator)


# 3. собственные исключения 2


class IsNum(Exception):
    def __init__(self, txt):
        self.txt = txt


li = []  # заполняемый значениями список


def listing():
    while True:
        try:
            elem = input('Введите число для добавления в список, для завершения введите "stop"')
            if elem.isalpha():
                if elem.lower() == 'stop':
                    return li
                else:
                    raise IsNum('Разрешены только числа!')
            else:
                li.append(elem)
        except IsNum as err:
            print(err)


print(listing())

# 4, 5, 6 учет музыкального инвентаря


class MusInst:
    def __init__(self, name: str, materials: list) -> None:
        self.name = name.title()
        self.materials = materials

    def __str__(self) -> str:
        return self.info()

    def info(self) -> str:
        return f'Instrument name is {self.name}.\nIt\'s made of {", ".join(self.materials)}.'

    @staticmethod
    def tuning() -> str:
        return 'Tuning the instrument'

    def play(self, song_name: str) -> str:
        return f'{self.name} plays a "{song_name}" tune!'


class Brass(MusInst):

    genres = ['Classic', 'Cinematic', 'Roots', 'Jazz', 'Blues']

    def __init__(self, name: str, materials: list, key: str) -> None:
        super().__init__(name, materials)
        self.key = key

    def __str__(self) -> str:
        return f'It\'s a {self.name} in key of {self.key}!'

    def info(self) -> str:
        return f'Brass instrument name is {self.name}.\nIt\'s made of {", ".join(self.materials)}.\nBest known for {", ".join(self.genres)} genres.'

    def play(self, song_name: str) -> str:
        return f'Brass {self.name}({self.key}) is playing a "{song_name}"!'


class Stringed(MusInst):

    genres = ['Classic', 'Cinematic', 'Roots', 'Jazz', 'Blues', 'Rock']

    def __init__(self, name: str, materials: list, strings_num: int) -> None:
        super().__init__(name, materials)
        self.strings_num = strings_num

    def __str__(self) -> str:
        return f'It\'s a {self.name} with {self.strings_num} strings!'

    def info(self) -> str:
        return f'{self.name} is a {self.strings_num} stringed instrument.\nIt\'s made of {", ".join(self.materials)}.\nBest known for {", ".join(self.genres)} genres.'

    def play_in_bmp(self, song_name: str, tempo: int) -> str:
        return f'{self.name}({self.strings_num}-stringed) is playing a "{song_name}" in {tempo} bmp.'


class IsStoraged:

    """Создание хранящегося на складе объекта"""

    city = 'New York'
    location = 'West-side storehouse'
    store_counter = 0
    item_list = []
    capacity = 10

    def __init__(self, mus_item: object, quantity: int):
        self.mus_item = mus_item
        self.quantity = quantity

    def store(self, store_time_dd: float) -> None:
        item = (str(self.mus_item), store_time_dd)
        IsStoraged.store_counter += 1
        return IsStoraged.item_list.append(list(item))

    @staticmethod
    def store_validation():
        for i, el in enumerate(IsStoraged.item_list):
            if 0 < el[1] < 10000:
                print(f'Data is valid for {i + 1} item.')
            else:
                print(f'Not valid data for {i + 1} item!')

# tests #


cl = Brass('Clarinet', ['Ebony', 'Plastic', 'Crystal'], 'A')
vn = Stringed('Violin', ['Ebony', 'Maple', 'Steel'], 4)
gt = Stringed('Guitar', ['Rosewood', 'Mahogany', 'Steel'], 6)

print(cl)
print(cl.info(), cl.play('Tocata in A'))
print(vn)
print(vn.info(), vn.play_in_bmp('Contradanza', 130))
print(gt)
print(gt.info(), gt.play_in_bmp('Master of Puppets', 220))

cl_storaged = IsStoraged(cl, 2)
gt_storaged = IsStoraged(gt, 3)

cl_storaged.store(160.12)
cl_storaged.store_validation()

# adding second item in the storage #

gt_storaged.store(30)
gt_storaged.store_validation()

print(IsStoraged.item_list)

# 7. сложение и умножение комплексных чисел


class ComplexNumber:
    def __init__(self, real_num: float, img_num: float):
        self.real_num = real_num
        self.img_num = img_num
        self.comp_num = complex(real_num, img_num)  # нужно ли?

    def __str__(self):
        return self.comp_num

    def __add__(self, other):
        return f'{self.comp_num} + {other.comp_num} = {self.comp_num + other.comp_num}'

    def __mul__(self, other):
        return f'{self.comp_num} * {other.comp_num} = {self.comp_num * other.comp_num}'


c0 = ComplexNumber(2, 3)
c1 = ComplexNumber(-5, 4)
c2 = ComplexNumber(7, -4)

print(c0 + c1)
print(c1 * c2)
