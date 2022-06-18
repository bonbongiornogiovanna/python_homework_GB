# 1. матрицы


class Matrix:

    """матрица любой размерности"""

    def __init__(self, mtrx: list):
        self.mtrx = mtrx

    def __str__(self) -> str:
        return '\n'.join([' '.join([str(i) for i in j]) for j in self.mtrx])

    def __add__(self, other) -> object:

        """сложение матриц с проверкой на размерность"""

        if len(self.mtrx) == len(other.mtrx) and len(self.mtrx[0]) == len(other.mtrx[1]):  # без проверки каждой строки на размерность (не удалось)
            return Matrix([[self.mtrx[i][j] + other.mtrx[i][j] for j in range(len(self.mtrx[0]))] for i in range(len(self.mtrx))])
        else:
            return 'Складывать можно лишь матрицы одинаковой размерности!'


mtrx0 = [[2, 3, 4],
         [3, 2, 1]]

mtrx1 = [[1, 3, 9],
         [2, 2, 3]]

mtrx2 = [[1, 3],
         [2, 2],
         [3, 2]]

m0 = Matrix(mtrx0)
m1 = Matrix(mtrx1)
m2 = Matrix(mtrx2)

print(m0)
print(' ')  # есть ли способ более кратко записасть пропустить строку при выводе в консоль?
print(m1)
print(' ')
print(m2)
print(' ')
print(m0 + m1)
print(' ')
print(m1 + m2)

# 2. расчет расхода ткани
from abc import ABC, abstractmethod


class Clothing(ABC):
    name = None

    @abstractmethod
    def cloth_calc(self):
        pass


class Coat(Clothing):
    size = None

    def __init__(self, size: float) -> None:
        self.size = size

    @property
    def cloth_calc(self) -> str:
        res = self.size / 6.5 + 0.5
        return f'Расход ткани для вещи составляет {res:0.2f}'


class Suit(Clothing):
    height = None

    def __init__(self, height: float) -> None:
        self.height = height

    @property
    def cloth_calc(self) -> str:
        res = self.height * 2 + 0.3
        return f'Расход ткани для вещи составляет {res:0.2f}'


ct = Coat(100.05)
st = Suit(70.5)
print(ct.cloth_calc)
print(st.cloth_calc)

# 3. работа с органическими клетками


class Cell:
    def __init__(self, cell_num: int) -> None:
        self.cell_num = cell_num

    def __str__(self):
        return str(self.cell_num)

    def __add__(self, other) -> str:
        return f'Количество ячеек клеток при слиянии: {Cell(self.cell_num + other.cell_num)}'

    def __sub__(self, other) -> str:
        if self.cell_num - other.cell_num > 0:
            return f'Количество ячеек клеток при вычитании: {Cell(self.cell_num - other.cell_num)}'
        else:
            return f'Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля!'

    def __mul__(self, other) -> object:
        return Cell(self.cell_num * other.cell_num)

    def __truediv__(self, other) -> object:
        return Cell(self.cell_num // other.cell_num)

    @staticmethod
    def make_order(num: int, char='*') -> str:
        rows = num // 5
        surplus = num - (rows * 5)
        return f'{char * 5}\n' * rows + f'{char * surplus}'


c0 = Cell(30)
c1 = Cell(22)

print(c0 + c1)
print(c0 - c1)
print(c1 / c0)
print(c1 * c0)
print(Cell.make_order(29))
