# Задание 1
# Создайте класс Circle (окружность). Для данного
# класса реализуйте ряд перегруженных операторов:
# ■ Проверка на равенство радиусов двух окружностей
# (операция = =);
# ■ Сравнения длин двух окружностей (операции >, <,
# <=,>=);
# ■ Пропорциональное изменение размеров окружности,
# путем изменения ее радиуса (операции + - += -=).

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'Радиус круга:  {self.radius}'

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __isub__(self, other):
        self.radius -= other.radius
        return self

    def get_area(self):
        return pi * self.radius ** 2

    def get_circumference(self):
        return 2 * pi * self.radius

#-------------------------------------------------------------------------------------------------------------
# Задание 2
# Создайте класс Complex (комплексное число). Более
# подробно ознакомиться с комплексными числами можно
# по ссылке.
# Создайте перегруженные операторы для реализации
# арифметических операций для по работе с комплексными
# числами (операции +, -, *, /).

class Complex:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)

    def __truediv__(self, other):
        denom = float(other.real ** 2 + other.imag ** 2)
        return Complex((self.real * other.real + self.imag * other.imag) / denom,
                       (self.imag * other.real - self.real * other.imag) / denom)

#--------------------------------------------------------------------------------------------------------------
# Задание 3
# Вам необходимо создать класс Airplane (самолет).
# ■ Проверка на равенство типов самолетов (операция
# = =);
# ■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# ■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции >
# < <= >=).
class Airplane:

    def __init__(self, model, passengers):
        self.model = model
        self.passengers = passengers

    def __eq__(self, other):
        return isinstance(other, Airplane) and self.model == other.model

    def __add__(self, num):
        return Airplane(self.model, self.passengers + num)

    def __sub__(self, num):
        return Airplane(self.model, self.passengers - num)

    def __iadd__(self, num):
        self.passengers += num
        return self

    def __isub__(self, num):
        self.passengers -= num
        return self

    def __lt__(self, other):
        return isinstance(other, Airplane) and self.passengers < other.passengers

    def __le__(self, other):
        return isinstance(other, Airplane) and self.passengers <= other.passengers

    def __gt__(self, other):
        return isinstance(other, Airplane) and self.passengers > other.passengers

    def __ge__(self, other):
        return isinstance(other, Airplane) and self.passengers >= other.passengers


#--------------------------------------------------------------------------------------------------------------
# Задание 4
# Создать класс Flat (квартира). Реализовать перегруженные операторы:
# ■ Проверка на равенство площадей квартир (операция
# ==);
# ■ Проверка на неравенство площадей квартир (операция !=);
# ■ Сравнение двух квартир по цене (операции > < <= >=).

class Flat:

    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return isinstance(other, Flat) and self.area == other.area

    def __ne__(self, other):
        return isinstance(other, Flat) and self.area != other.area

    def __lt__(self, other):
        return isinstance(other, Flat) and self.price < other.price

    def __le__(self, other):
        return isinstance(other, Flat) and self.price <= other.price

    def __gt__(self, other):
        return isinstance(other, Flat) and self.price > other.price

    def __ge__(self, other):
        return isinstance(other, Flat) and self.price >= other.price