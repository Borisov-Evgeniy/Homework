# Задание 1
# Создайте реализацию паттерна Builder. Протестируйте
# работу созданного класса.

class Pizza:
    def __init__(self,builder):
        self.size = builder.size
        self.cheese = builder.cheese
        self.ingridients = builder.ingridients
    def __str__(self):
        return f"У нас получилась пицца размером {self.size} см, с сыром " \
               f"{self.cheese} и {', '.join(map(str,self.ingridients))}"

class PizzaBuilder:
    def __init__(self,size):
        self.size = size
        self.cheese = None
        self.ingridients = []

    def add_cheese(self,cheese):
        self.cheese = cheese
        return self

    def add_ingridients(self,ingridients):
        self.ingridients.append(ingridients)
        return self

    def build(self):
        return Pizza(self)

pizza = PizzaBuilder(35).add_cheese('Моцарела').add_ingridients(['Пеперони','лук','помидоры']).build()
print(pizza)
#----------------------------------------------------------------------------------------------------------------------
# Задание 2
# Создайте приложение для приготовления пасты. Приложение должно уметь создавать минимум три вида пасты.
# Классы различной пасты должны иметь следующие
# методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны.

class Pasta:
    def __init__(self, pasta_type, sauce, filling, ingridients):
        self.pasta_type = pasta_type
        self.sauce = sauce
        self.filling = filling
        self.ingridients = ingridients

    def __str__(self):
        return f" Мы приготовили пасту {self.pasta_type} с {self.sauce}, {self.filling}, и {self.ingridients}"

class PastaFactory:
    def create_pasta(self,pasta_type):
        if pasta_type == 'Спаггети':
            return Pasta('Спаггети','Томатытный соус','Фарш',['Сыр пармезан'])
        elif pasta_type == 'Фетучини':
            return Pasta('Фетучини', 'Соус альфредо', 'Курица', ['Брокколи','Сыр пармезан'])
        elif pasta_type == 'Пенне':
            return Pasta('Пенне','Соус болоньезе', 'Сосиски', ['Грибы', 'Сыр пармезан'])
        else:
            return None
factory = PastaFactory()

spaghetti = factory.create_pasta("Спаггети")
print(spaghetti)

fettuccine = factory.create_pasta("Фетучини")
print(fettuccine)

penne = factory.create_pasta("Пенне")
print(penne)
#---------------------------------------------------------------------------------------------------------------------
# Задание 3
# Создайте реализацию паттерна Prototype. Протестируйте работу созданного класса.

import copy

class Shape:
    def draw(self):
        pass

    def clone(self):
        pass

class Circle(Shape):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        print(f"Рисуем круг с координатами ({self.x}, {self.y}) и радиусом {self.z}.")

    def clone(self):
        return copy.deepcopy(self)

circle = Circle(10, 20, 30)
clone_circle = circle.clone()
clone_circle.draw()