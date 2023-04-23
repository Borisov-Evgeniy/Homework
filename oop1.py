# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Cars:
    def __init__(self,maker = None ,model = None, year = None , engine_volume = None ,color = None , price = 0):
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


car = Cars()
car.input_data()
car.print_data()
#-----------------------------------------------------------------------------------------------------------------
# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.
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



book = Book()
book.input_data()
book.print_data()

#---------------------------------------------------------------------------------------------------------------------
# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

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


stadium = Stadium()
stadium.input_data()
stadium.print_data()