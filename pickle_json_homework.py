# Задание 1
# К уже реализованному классу «Автомобиль» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.

import json
import pickle
class Cars:
    def __init__(self, maker=None, model=None, year=None,
                 engine_volume=None, color=None, price=0):
        self.maker = maker
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_maker(self, maker):
        self.maker = maker

    def set_engine_volume(self, engine_volume):
        self.engine_volume = engine_volume

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_maker(self):
        return self.maker

    def get_engine_volume(self):
        return self.engine_volume

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def input_data(self):
        self.model = input("Введите модель: ")
        self.year = input("Введите год выпуска: ")
        self.maker = input("Введите производителя: ")
        self.engine_volume = input("Введите объем двигателя: ")
        self.color = input("Введите цвет машины: ")
        self.price = input("Введите цену: ")

    def print_data(self):
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.maker}")
        print(f"Объем двигателя: {self.engine_volume}")
        print(f"Цвет машины: {self.color}")
        print(f"Цена: {self.price}")

    def to_json(self):
        return json.dumps(self.__dict__)

    def from_json(self, json_data):
        self.__dict__ = json.loads(json_data)

    def to_pickle(self):
        return pickle.dumps(self)

    def from_pickle(self, pickle_data):
        loaded_object = pickle.loads(pickle_data)
        if isinstance(loaded_object, Cars):
            new_object = Cars()
            new_object.__dict__.update(loaded_object.__dict__)
            return new_object
        else:
            raise TypeError("Cannot load object of type {}".format(type(loaded_object)))


car = Cars()
car.input_data()
#------------------------------------------------------------------------------------------------------------------------------
# Задание 2
# К уже реализованному классу «Книга» добавьте возможность упаковки и распаковки данных с использованием json и pickle.

class Book:
    def __init__(self, title = None, year = None, publisher = None, genre = None, author = None, price = 0):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_title(self, title):
        self.title = title

    def set_year(self, year):
        self.year = year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_genre(self, genre):
        self.genre = genre

    def set_author(self, author):
        self.author = author

    def set_price(self, price):
        self.price = price

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def input_data(self):
        self.title = input("Введите название книги: ")
        self.year = input("Введите год выпуска: ")
        self.publisher = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = input("Введите цену: ")

    def print_data(self):
        print(f"Название книги: {self.title}")
        print(f"Год выпуска: {self.year}")
        print(f"Издатель: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Цена: {self.price}")

    def to_json(self):
        return json.dumps(self.__dict__)

    def from_json(self, json_data):
        self.__dict__ = json.loads(json_data)

    def to_pickle(self):
        return pickle.dumps(self)

    def from_pickle(self, pickle_data):
        loaded_object = pickle.loads(pickle_data)
        if isinstance(loaded_object, Book):
            new_object = Book()
            new_object.__dict__.update(loaded_object.__dict__)
            return new_object
        else:
            raise TypeError("Cannot load object of type {}".format(type(loaded_object)))



book = Book()
book.input_data()
book.print_data()
#---------------------------------------------------------------------------------------------------------------------------
# Задание 3
# К уже реализованному классу «Стадион» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle

class Stadium:
    def __init__(self, name = None, opening_date = None, country = None, city = None, capacity = 0):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def set_name(self, name):
        self.name = name

    def set_opening_date(self, opening_date):
        self.opening_date = opening_date

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_name(self):
        return self.name

    def get_opening_date(self):
        return self.opening_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

    def input_data(self):
        self.name = input('Введите название стадиона: ')
        self.opening_date = input('Введите дату открытия стадиона: ')
        self.country = input('Введите страну: ')
        self.city = input('Введите город: ')
        self.capacity = input('Введите вместимость стадиона: ')

    def print_data(self):
        print(f'Название стадиона: {self.name}')
        print(f'Дата открытия стадиона: {self.opening_date}')
        print(f'Страна: {self.country}')
        print(f'Город: {self.city}')
        print(f'Вместимость: {self.capacity}')

    def to_json(self):
        return json.dumps(self.__dict__)

    def from_json(self, json_data):
        self.__dict__ = json.loads(json_data)

    def to_pickle(self):
        return pickle.dumps(self)

    def from_pickle(self, pickle_data):
        loaded_object = pickle.loads(pickle_data)
        if isinstance(loaded_object, Stadium):
            new_object = Stadium()
            new_object.__dict__.update(loaded_object.__dict__)
            return new_object
        else:
            raise TypeError("Cannot load object of type {}".format(type(loaded_object)))

stadium = Stadium()
stadium.input_data()
stadium.print_data()