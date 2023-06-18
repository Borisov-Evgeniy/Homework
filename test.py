# Задание 1
# Создайте класс, содержащий набор целых чисел.
# В классе должна быть реализована следующая функциональность:
# ■ Сумма элементов набора.
# ■ Среднеарифметическое элементов набора.
# ■ Максимум из элементов набора.
# ■ Минимум из элементов набора.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest).

import unittest


class ListNumber:
    def __init__(self):
        self.lst_number = []

    def __str__(self):
        return f'Список чисел: {self.lst_number}'

    def user_input(self):
        choice = input('Введите список чисел через запятую: \n')
        return [int(num) for num in choice.split(',')]

    def add_number(self, choice):
        self.lst_number.append(choice)

    def __save_number(self):
        memory = choice
        return memory

    def sum_numbers(self):
        total = sum(self.__save_number())
        return f'{total} сумма списка значений'

    def max_number(self):
        total = max(self.__save_number())
        return f'{total} максимальное значение'

    def min_number(self):
        total = min(self.__save_number())
        return f'{total} минимальное значение'

    def average_number(self):
        total = sum(self.__save_number()) / len(self.__save_number())
        return f'{total} среднее арифметическое'

number = ListNumber()
choice = number.user_input()
number.add_number(choice)

print(number.lst_number)
print(number.sum_numbers())
print(number.max_number())
print(number.min_number())
print(number.average_number())

class TestListNumber(unittest.TestCase):
    def setUp(self):
        self.number = ListNumber()

    def test_add_number(self):
        self.number.add_number([1,2,3])
        self.assertEqual(self.number.lst_number, [1,2,3])

    def test_save_number(self):
        self.number.add_number([1,2,3])
        result = self.number._ListNumber__save_number()
        self.assertEqual(result, [1,2,3])

    def test_sum_numbers(self):
        self.number.add_number([1,2,3])
        result = self.number.sum_numbers()
        self.assertEqual(result, '6 сумма списка значений')

    def test_max_number(self):
        self.number.add_number([1,2,3])
        result = self.number.max_number()
        self.assertEqual(result, '3 максимальное значение')

    def test_min_number(self):
        self.number.add_number([1,2,3])
        result = self.number.min_number()
        self.assertEqual(result, '1 минимальное значение')

    def test_average_number(self):
        self.number.add_number([1,2,3])
        result = self.number.average_number()
        self.assertEqual(result, '2.0 среднее арифметическое')

if __name__ == '__main__':
    unittest.main()
#--------------------------------------------------------------------------------------------------
# Задание 2
# Создайте класс для числа. В классе должна быть реализована следующая функциональность:
# ■ Запись и чтение значения.
# ■ Перевод числа в восьмеричную систему исчисления.
# ■ Перевод числа в шестнадцатеричную систему исчисления.
# ■ Перевод числа в двоичную систему исчисления.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest)


import unittest
class Number:
    def __init__(self, value):
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def to_octal(self):
        return oct(self.value)

    def to_hex(self):
        return hex(self.value)

    def to_binary(self):
        return bin(self.value)


class TestNumber(unittest.TestCase):
    def test_set_get_value(self):
        number = Number(10)
        number.set_value(20)
        self.assertEqual(number.get_value(), 20)

    def test_to_octal(self):
        number = Number(10)
        self.assertEqual(number.to_octal(), '0o12')

    def test_to_hex(self):
        number = Number(16)
        self.assertEqual(number.to_hex(), '0x10')

    def test_to_binary(self):
        number = Number(7)
        self.assertEqual(number.to_binary(), '0b111')


if __name__ == '__main__':
    unittest.main()