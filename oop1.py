# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Cars:
    def __init__(self,maker = None ,model = None, year = None , engine_volume = None ,color = None , price = None):
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

# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.





# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.
