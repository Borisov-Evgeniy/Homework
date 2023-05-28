# Задание 1
# Создайте реализацию паттерна Command. Протестируйте работу созданного класса.

from abc import ABC, abstractmethod

class Calculator:
    def __init__(self):
        self.current = 0
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)
        self.current = command.execute(self.current)
        return self.current

    def execute_commands(self):
        for c in self.commands:
            self.current = c.execute(self.current)

    def undo(self):
        command = self.commands.pop()
        self.current = command.undo(self.current)
        return self.current

class Command(ABC):
    @abstractmethod
    def execute(self, current):
        pass

    @abstractmethod
    def undo(self, current):
        pass

class AddCommand(Command):
    def __init__(self, operand):
        self.operand = operand

    def execute(self, current):
        return current + self.operand

    def undo(self, current):
        return current - self.operand

class SubtractCommand(Command):
    def __init__(self, operand):
        self.operand = operand

    def execute(self, current):
        return current - self.operand

    def undo(self, current):
        return current + self.operand

class MultiplyCommand(Command):
    def __init__(self, operand):
        self.operand = operand

    def execute(self, current):
        return current * self.operand

    def undo(self, current):
        return current / self.operand

class DivideCommand(Command):
    def __init__(self, operand):
        self.operand = operand

    def execute(self, current):
        if self.operand == 0:
            raise ValueError("Cannot divide by zero.")
        return current / self.operand

    def undo(self, current):
        return current * self.operand

class PowerCommand(Command):
    def __init__(self, operand):
        self.operand = operand

    def execute(self, current):
        return current ** self.operand

    def undo(self, current):
        return current ** (1 / self.operand)

calc = Calculator()
calc.add_command(AddCommand(17))
calc.add_command(AddCommand(17))
print(calc.current)
# -----------------------------------------------------------------------------------------------------------
# Задание 2
# Есть класс, предоставляющий доступ к набору чисел.
# Источником этого набора чисел является некоторый
# файл. С определенной периодичностью данные в файле
# меняются (надо реализовать механизм обновления).
# Приложение должно получать доступ к этим данным и
# выполнять набор операций над ними (сумма, максимум,
# минимум и т.д.). При каждой попытке доступа к этому
# набору необходимо вносить запись в лог-файл. При реализации используйте паттерн Proxy (для логгирования)
# и другие необходимые паттерны.

import datetime,time
class Numbers:
    def __init__(self, number_file):
        self.number_file = number_file
        self.number = []
        self.refresh_interval = 5
        self.load_numbers()

    def load_numbers(self):
        with open(self.number_file, 'r') as file:
            self.numbers = [int(line) for line in file]
    def save_numbers(self):
        with open (self.number_file, 'w') as file:
            for number in self.numbers:
                file.write(str(number) + '\n')

    def add_number(self,number):
        self.numbers.append(number)
        self.save_numbers()

    def remove_number(self,number):
        self.numbers.remove(number)
        self.save_numbers()

    def sum(self):
        return sum(self.numbers)

    def maximum(self):
        return max(self.numbers)

    def minimum(self):
        return min(self.numbers)

    def start_refresh(self):
        while True:
            self.load_numbers()
            print('Обновлено!')
            time.sleep(self.refresh_interval)

class NumberProxy(Numbers):

    def __init__(self, number_file, log_file):
        super().__init__(number_file)
        self.log_file = log_file

    def add_number(self,number):
        with open(self.log_file,'a') as file:
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"{time} Добавление числа {number}\n")
            super().add_number(number)

    def remove_number(self, number):
        with open(self.log_file, "a") as f:
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"{time}: Удаление числа {number}\n")
        super().remove_number(number)

    def sum(self):
        with open(self.log_file, "a") as f:
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"{time}: Вычисление суммы\n")
        return super().sum()

    def maximum(self):
        with open(self.log_file, "a") as f:
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"{time}: Вычисление максимума\n")
        return super().maximum()

    def minimum(self):
        with open(self.log_file, "a") as f:
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"{time}: Вычисление минимума\n")
        return super().minimum()


add_num = NumberProxy('num.txt','log.txt')
add_num.add_number(45)
add_num.add_number(12)
add_num.add_number(32)
add_num.add_number(1)
add_num.remove_number(12)
with open('log.txt','r') as f:
    print(f.read())
add_num.start_refresh()
# ---------------------------------------------------------------------------------------------------------
# Задание 3
# Создайте приложение для работы в библиотеке. Оно
# должно оперировать следующими сущностями: Книга,
# Библиотекарь, Читатель. Приложение должно позволять
# вводить, удалять, изменять, сохранять вфайл, загружать из
# файла, логгировать действия, искать информацию (результаты поиска выводятся на экран или файл) о сущностях.
# При реализации используйте максимально возможное
# количество паттернов проектирования

import logging
logging.basicConfig(filename= 'log.txt', level=logging.INFO)

class Model:
    def __init__(self):
        self.books = {}
        self.librarians = {}
        self.readers = {}

    def add_book(self,book):
        self.books[book.title] = book

    def remove_book(self, book=None):
        del self.books[book.title]

    def add_librarian(self, librarian):
        self.librarians[librarian.name] = librarian

    def remove_librarian(self, librarian):
        del self.librarians[librarian.name]

    def add_reader(self, reader):
        self.readers[reader.name] = reader

    def remove_reader(self, reader):
        del self.readers[reader.name]

    def get_book(self, title):
        return self.books.get(title)

    def get_librarian(self, name):
        return self.librarians.get(name)

    def get_reader(self, name):
        return self.readers.get(name)

class Book:
    def __init__(self,model,title,author = None ,year = None):
        self.model = model
        self.title = title
        self.author = author
        self.year = year
        self.model.add_book(self)

    def __str__(self):
        return f"{self.title} / {self.author} / {self.year} "
    def remove(self):
        self.model.remove_book(self)

class Reader:
    def __init__(self,model,name = None):
        self.model = model
        self.name = name
        self.model.add_reader(self)

    def remove(self):
        self.model.remove_reader(self)

    def __str__ (self):
        return f" Читатель: {self.name}"

class Librarian:
    def __init__(self, model, name=''):
        self._model = model
        self.name = name
        self._model.add_librarian(self)

    def __str__(self):
        return f"Библиотекарь: {self.name}"

    def remove(self):
        self._model.remove_librarian(self)

class LoggingProxy:
    def __init__(self,obj):
        self.obj = obj
        self.logging = logging.getLogger(obj.__class__.__name__)

    def __getattr__(self, item):
        orig_attr = self._obj.__getattribute__(item)
        if callable(orig_attr):
            def new_attr(*args,**kwargs):
                result = orig_attr(*args,**kwargs)
                self._logger.info(f"Вызыван метод {attr} c аргументами:{args,kwargs}")
                return result
            return new_attr()
        else:
            return  orig_attr

model = Model()
book = LoggingProxy(Book(model, title="1984",author="George Orwell"))
librarian = LoggingProxy(Librarian(model,name="John Week"))
reader = LoggingProxy(Reader(model, name= 'Karl'))
