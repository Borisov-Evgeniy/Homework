# Задание 1
# Создать базовый класс Фигура с методом для подсчета
# площади. Создать производные классы: прямоугольник,
# круг, прямоугольный треугольник, трапеция со своими
# методами для подсчета площади.

import math
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f"Площадь равна: {self.area()} см."

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Trapezium(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height
#----------------------------------------------------------------------------------------------------------------
# Задание 2
# Для классов из задания 1 нужно переопределить магические методы int(возвращает площадь) и str(возвращает
# информацию о фигуре).

from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f"Площадь равна: {int(self)} см."

    def __int__(self):
        area = self.area()
        if not isinstance(area, (int, float)):
            raise ValueError("Невозможно преобразовать площадь в целое число")
        return int(area)


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __int__(self):
        area = self.area()
        if not isinstance(area, (int, float)):
            raise ValueError("Невозможно преобразовать площадь в целое число")
        return int(area)


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __int__(self):
        area = self.area()
        if not isinstance(area, (int, float)):
            raise ValueError("Невозможно преобразовать площадь в целое число")
        return int(area)


class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __int__(self):
        area = self.area()
        if not isinstance(area, (int, float)):
            raise ValueError("Невозможно преобразовать площадь в целое число")
        return int(area)


class Trapezium(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __int__(self):
        area = self.area()
        if not isinstance(area, (int, float)):
            raise ValueError("Невозможно преобразовать площадь в целое число")
        return int(area)
#
# #---------------------------------------------------------------------------------------------------------------------
# Задание 3
# Создайте базовый класс Shape для рисования плоских
# фигур.
# Определите методы:
# ■ Show() — вывод на экран информации о фигуре;
# ■ Save() — сохранение фигуры в файл;
# ■ Load() — считывание фигуры из файла.
# Определите производные классы:
# ■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# ■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# ■ Circle — окружность с заданными координатами центра и радиусом;
# ■ Ellipse — эллипс с заданными координатами верхнего
# угла описанного вокруг него прямоугольника со сторонами, параллельными осям координат, и размерами
# этого прямоугольника.
# Создайте список фигур, сохраните фигуры в файл,
# загрузите в другой список и отобразите информацию о
# каждой из фигур.

from abc import ABC, abstractmethod
import math
import re


class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def show(self):
        print(f"Координаты: ({self.x}, {self.y})")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(f"{self.__class__.__name__}({self.x},{self.y}")
            if isinstance(self, Square):
                f.write(f",{self.side})\n")
            elif isinstance(self, Rectangle):
                f.write(f",{self.width},{self.height})\n")
            elif isinstance(self, Circle):
                f.write(f",{self.radius})\n")
            elif isinstance(self, Ellipse):
                f.write(f",{self.a},{self.b})\n")

    @staticmethod
    def load(file):
        with open(file, 'r') as f:
            shape_str = f.readline().strip()
            if shape_str.startswith('Circle'):
                # поиск координат круга
                x, y, r = map(float, re.findall(r'\d+\.*\d*', shape_str))
                return Circle(x, y, r)
            elif shape_str.startswith('Rectangle'):
                # поиск координат треугольника
                x1, y1, x2, y2 = map(float, re.findall(r'\d+\.*\d*', shape_str))
                return Rectangle(x1, y1, x2, y2)
            elif shape_str.startswith('Square'):
                # поиск координат квадрата
                square_str = re.findall(r'\d+\.*\d*', shape_str)
                if len(square_str) == 2:
                    x, y = map(float, square_str)
                    return Square(x, y, 0)
                elif len(square_str) == 3:
                    x, y, a = map(float, square_str)
                    return Square(x, y, a)
                else:
                    raise ValueError(f"Некорректный формат координат в файле: {shape_str}")
            elif shape_str.startswith('Ellipse'):
                # Поиск координад эллипса
                x, y, a, b = map(float, re.findall(r'\d+\.*\d*', shape_str))
                return Ellipse(x, y, a, b)
            else:
                raise ValueError(f"Некорректный формат фигуры в файле: {shape_str}")


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Ellipse(Shape):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a
        self.b = b

    def area(self):
        return math.pi * self.a * self.b

    def perimeter(self):
        return 2 * math.pi * math.sqrt((self.a ** 2 + self.b ** 2) / 2)

shapes = [Square(0, 0, 5), Rectangle(10, 10, 5, 10), Circle(20, 20, 3), Ellipse(30, 30, 4, 6)]
for shape in shapes:
    shape.show()
    shape.save(f"{shape.__class__.__name__}.txt")

new_shapes = []
for shape in shapes:
    new_shapes.append(Shape.load(f"{shape.__class__.__name__}.txt"))

for shape in new_shapes:
    shape.show()

