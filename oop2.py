# Задание 1
# Создайте класс Device, который содержит информацию об устройстве.
# Спомощью механизма наследования, реализуйте класс
# класс Blender (содержит информацию о блендере), класс
# MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые
# для работы методы.

class Device:
    def __init__(self, name, model, brand, price, serial_number):
        self.name = name
        self.model = model
        self.brand = brand
        self.price = price
        self.serial_number = serial_number

class Blender(Device):
    def __init__(self, name, brand, price, model, serial_number, power):
        super().__init__(name, brand, price, model, serial_number)
        self.power = power

class MeatGrinder(Device):
    def __init__(self, name, brand, price, model, serial_number, power):
        super().__init__(name, brand, price, model, serial_number)
        self.power = power

#--------------------------------------------------------------------------------------------------------------------
# Задание 2
# Создайте класс Ship, который содержит информацию
# о корабле.
# С помощью механизма наследования, реализуйте
# класс Frigate (содержит информацию о фрегате), класс
# Destroyer (содержит информацию об эсминце), класс
# Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые
# для работы методы.

class Ship:
    def __init__(self, name, length, displacement, crew_number):
        self.name = name
        self.length = length
        self.displacement = displacement
        self.crew_number = crew_number

class Frigate(Ship):
    def __init__(self, name, length, displacement, crew_number, weapon_type):
        super().__init__(name, length, displacement, crew_number)
        self.weapon_type = weapon_type

class Destroyer(Ship):
    def __init__(self, name, length, displacement, crew_number, missile_type):
        super().__init__(name, length, displacement, crew_number)
        self.missile_type = missile_type

class Cruiser(Ship):
    def __init__(self, name, length, displacement, crew_number, weapon_type, missile_type):
        super().__init__(name, length, displacement, crew_number)
        self.weapon_type = weapon_type
        self.missile_type = missile_type

#---------------------------------------------------------------------------------------------------------------------
# Задание 3
# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и
# поле для хранения копеек (центы, евроценты, копейки
# и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей.

class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def display_total(self):
        return f"{self.dollars}.{self.cents}$"

    def set_amount(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_amount(self, dollars, cents):
        self.dollars += dollars
        self.cents += cents
        if self.cents >= 100:
            self.dollars += self.cents // 100
            self.cents %= 100


money1 = Money(20, 35)
print(money1.display_total())

money1.set_amount(30, 12)
print(money1.display_total())

money1.add_amount(13, 68)
print(money1.display_total())