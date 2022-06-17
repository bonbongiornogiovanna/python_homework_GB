# 1. светофор цикл как и требует задание "красный" -> "желтый" -> "зеленый".
# При начале следующего цикла, "желтый" между цикалми не выводится
import time as t


class TrafficLight:
    # атрибут класса:
    __color = None

    # метод класса:
    def running(self):
        runs = int(input('Type the number of cycles: '))
        try:
            for cycle in range(0, runs):
                __color = 'red'
                print(__color)
                t.sleep(7)
                __color = 'yellow'
                print(__color)
                t.sleep(2)
                __color = 'green'
                print(__color)
                t.sleep(10)
        except TypeError:
            print('Wrong input type, expected: integer number!')


traff = TrafficLight()
traff.running()


# 2. расчет массы асфальта


class Road:
    _length = None
    _width = None

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def formula(self, wei1, th):
        self.weight1 = wei1
        self.thickness = th
        print(self._length * self._width * self.weight1 * self.thickness)


my_road = Road(20000, 6)
my_road.formula(12, 5)

# 3. наследование классов


class Worker:

    name = None
    surname = None
    position = None
    wage = None
    bonus = None
    _income = {'wage': wage,
               'bonus': bonus}

    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self.wage = w
        self.bonus = b


class Position(Worker):

    def get_full_name(self):
        print(f'Full name is {self.name} {self.surname}, who works as {self.position} in company')

    def get_total_income(self):
        total_income = self.wage + self.bonus
        print(f'Total income of worker (incl. bonus): {total_income}')


js = Position('Jack', 'Sommerfeld', 'Site supervisor', 65000, 20000)
js.get_full_name()
js.get_total_income()

# 4. игра в машинки


class Car:
    speed = None
    color = None
    name = None

    def __init__(self, speed: float, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('rollin')

    def stop(self):
        print('stopped')

    def turn(self, direction):
        if direction == 'left':
            print('turning left!')
        else:
            print('turning right!')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('exceeding speed limit of 60, slow down!')
        else:
            print(self.speed)


class SportCar(Car):
    def show_speed(self):
        if self.speed < 120:
            print('fasten your seatbelt, turtles, and push it to the limit!!!')
        else:
            print(self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('exceeding speed limit of 40, slow down!')
        else:
            print(self.speed)


class PoliceCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name)
        self.is_police = True


pr = TownCar(60.2, 'silver', 'Toyota Prius')
pr.show_speed()
print(pr.is_police)

fr = SportCar(110, 'white', 'Ferrari')
fr.show_speed()
print(fr.is_police, fr.color)

iz = WorkCar(40, 'red', 'Isuzu')
iz.show_speed()
print(iz.is_police, iz.name)

lg = PoliceCar(140, 'green-white-red', 'Lamborghini Gallardo')
lg.show_speed()
print(lg.is_police, lg.name, lg.color)

# 5. канцелярия (тренировка переопределения методов)


class Stationery:
    title = None

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        print(Stationery.draw(self))
        print('Нужно написать эссе от руки - не беда, помогу, бери меня в РУЧКИ')


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        print('Спасибо, что не грызешь меня, как в прошлый раз, бобёр!')


class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        print('Время испачкать руки')


p = Pen()
p.draw()
print(p.title)
pc = Pencil()
pc.draw()
print(pc.title)
h = Handle()
h.draw()
print(h.title)
