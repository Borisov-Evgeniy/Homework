# Задание 1
# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список (тип
# списка нужно выбрать в зависимости от поставленной
# ниже задачи). После чего нужно показать меню, в котором
# предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число существует в списке,
# нужно вывести сообщение пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь
# вводит с клавиатуры число для удаления)
# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала
# или с конца)
# 4. Проверить есть ли значение в списке
# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все
# вхождения)
# В зависимости от выбора пользователя выполняется
# действие, после чего меню отображается снова.

input_string = input("Введите значения через пробел: ")
lst = input_string.split()
new_lst = []
for i in lst:
    new_lst.append(int(i))
print(new_lst)

def print_menu():
    print('''    Добавить число в список - 1
    Удалить число(а) из списка - 2
    Показать содержимое списка - 3
    Проверка наличия значения в списке - 4
    Заменить значение в списке - 5
    Выход - 6\n
    ''')
def input_value():
    value = int(input('Введите число для добавления в список: '))
    if value in new_lst:
        print('Такое значение уже присутствует в списке!')
    else:
        new_lst.append(value)
        print('Значение добавлено в список:', new_lst)

def del_number():
    value = int(input('Введите число для удаления из списка: '))
    if value in new_lst:
        new_lst.remove(value)
        print(f'Значение {value} удалено из списка:', new_lst)
    else:
        print(f'Значение {value} не найдено в списке!')

def show_lst():
    choice = input('Для сортировки списка по возрастанию, введите - 1\n'
                   'Для сортировки списка по убыванию, введите - 2\n')
    if choice == '1':
        new_lst.sort()
        print(new_lst)
    elif choice == '2':
        new_lst.sort(reverse=True)
        print(new_lst)

def num_search():
    value = int(input('Введите число для проверки: '))
    if value not in new_lst:
        print (f'Значение {value} в списке отсутствует!')
    else:
        print(f'Значение {value} встречается в списке {new_lst.count(value)} раз')

def replace_value():
    old_value = int(input('Какое число заменить?: '))
    new_value = int(input('Какое число вставить?: '))
    replace_all = input('Заменить все значения?: ')

    if replace_all.lower() == "да":
        for i in range(len(new_lst)):
            if new_lst[i] == old_value:
                new_lst[i] = new_value
    else:
        new_lst[new_lst.index(old_value)] = new_value

    print(new_lst)

def main_func():
    while True:
        print_menu()
        choice = input('Введите номер пункта меню: ')
        if choice == '1':
            input_value()
        elif choice == '2':
            del_number()
        elif choice == '3':
            show_lst()
        elif choice == '4':
            num_search()
        elif choice == '5':
            replace_value()
        elif choice == '6':
            break
        else:
            print('Некорректное значение! Попробуйте еще раз.')


main_func()
#-------------------------------------------------------------------------------------------------------------------

class NumbersList:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        if number in self.numbers:
            print(f'Число {number} уже есть в списке')
        else:
            self.numbers.append(number)
            print(f'Число {number} добавлено в список')

    def remove_number(self, number):
        if number not in self.numbers:
            print(f'Число {number} не найдено в списке')
        else:
            self.numbers = [n for n in self.numbers if n != number]
            print(f'Число {number} удалено из списка')

    def show_numbers(self, reverse=False):
        if not self.numbers:
            print('Список пуст')
        elif not reverse:
            print(self.numbers)
        else:
            print(self.numbers[::-1])

    def check_number(self, number):
        if number in self.numbers:
            print(f'Число {number} найдено в списке')
        else:
            print(f'Число {number} не найдено в списке')

    def replace_number(self, old_number, new_number, all_occurrences=False):
        if old_number not in self.numbers:
            print(f'Число {old_number} не найдено в списке')
        else:
            if all_occurrences:
                self.numbers = [new_number if n == old_number else n for n in self.numbers]
            else:
                index = self.numbers.index(old_number)
                self.numbers[index] = new_number
            print(f'Число {old_number} заменено на {new_number}')

def show_menu():
    print('''Меню:
    1. Добавить число в список
    2. Удалить число из списка
    3. Показать список
    4. Проверить наличие числа в списке
    5. Заменить число в списке
    6. Выход
    ''')

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('Некорректный ввод, попробуйте еще раз')

def main():
    lst = NumbersList()
    while True:
        show_menu()
        choice = get_integer_input('Введите номер пункта меню: ')
        if choice == 1:
            number = get_integer_input('Введите число: ')
            lst.add_number(number)
        elif choice == 2:
            number = get_integer_input('Введите число для удаления: ')
            lst.remove_number(number)
        elif choice == 3:
            rev = input('Показать список в обратном порядке? (y/n): ') == 'y'
            lst.show_numbers(reverse=rev)
        elif choice == 4:
            number = get_integer_input('Введите число для поиска: ')
            lst.check_number(number)
        elif choice == 5:
            old_number = get_integer_input('Введите число для замены: ')
            new_number = get_integer_input('Введите новое число: ')
            all_occurrences = input('Заменить все вхождения? (y/n): ') == 'y'
            lst.replace_number(old_number, new_number, all_occurrences)
        elif choice == 6:
            break
        else:
            print('Некорректный ввод, попробуйте еще раз')

main()

# Задание 2
# Реализуйте класс стека для работы со строками (стек
# строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки
# из стека.
# При старте приложения нужно отобразить меню с
# помощью, которого пользователь может выбрать необходимую операцию.

class StringStack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, string):
        if len(self.stack) < self.size:
            self.stack.append(string)
            return True
        else:
            return False

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.size

    def clear(self):
        self.stack = []

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None


size = int(input("Введите размер стека: "))
stack = StringStack(size)

while True:
    print("Меню: ")
    print("1. Поместить строку в стек")
    print("2. Выталкивание строки из стека")
    print("3. Подсчет количества строк в стеке")
    print("4. Проверка, пустой ли стек")
    print("5. Проверка, полный ли стек")
    print("6. Очистка стека")
    print("7. Получение значения без выталкивания верхней строки из стека")
    print("8. Показать стек")
    print("0. Выход")

    choice = int(input("Выберите операцию: "))

    if choice == 1:
        string = input("Введите строку для помещения в стек: ")
        if stack.push(string):
            print("Строка успешно помещена в стек")
        else:
            print("Стек полный")
    elif choice == 2:
        string = stack.pop()
        if string is not None:
            print("Строка", string, "вытолкнута из стека")
        else:
            print("Стек пустой")
    elif choice == 3:
        print("Количество элементов в стеке:", stack.count())
    elif choice == 4:
        print("Стек пустой:", stack.is_empty())
    elif choice == 5:
        print("Стек полный:", stack.is_full())
    elif choice == 6:
        stack.clear()
        print("Стек очищен")
    elif choice == 7:
        string = stack.peek()
        if string is not None:
            print("Значение верхней строки в стеке:", string)
        else:
            print("Стек пустой")
    elif choice == 8:
        print("Содержимое стека:")
        for i in reversed(stack.stack):
            print(i)
    elif choice == 0:
        break
    else:
        print("Неверный выбор, попробуйте еще раз")


# Задание 3
# Измените стек из второго задания, таким образом,
# чтобы его размер был нефиксированным.

class StringStack:
    def __init__(self):
        self.stack = []

    def push(self, string):
        self.stack.append(string)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack = []

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None


stack = StringStack()

while True:
    print("Меню: ")
    print("1. Поместить строку в стек")
    print("2. Выталкивание строки из стека")
    print("3. Подсчет количества строк в стеке")
    print("4. Проверка, пустой ли стек")
    print("5. Очистка стека")
    print("6. Получение значения без выталкивания верхней строки из стека")
    print("7. Показать стек")
    print("0. Выход")

    choice = int(input("Выберите операцию: "))

    if choice == 1:
        string = input("Введите строку для помещения в стек: ")
        stack.push(string)
        print("Строка успешно помещена в стек")
    elif choice == 2:
        string = stack.pop()
        if string is not None:
            print("Строка", string, "вытолкнута из стека")
        else:
            print("Стек пустой")
    elif choice == 3:
        print("Количество элементов в стеке:", stack.count())
    elif choice == 4:
        print("Стек пустой:", stack.is_empty())
    elif choice == 5:
        stack.clear()
        print("Стек очищен")
    elif choice == 6:
        string = stack.peek()
        if string is not None:
            print("Значение верхней строки в стеке:", string)
        else:
            print("Стек пустой")
    elif choice == 7:
        print("Содержимое стека:")
        for i in reversed(stack.stack):
            print(i)
    elif choice == 0:
        break
    else:
        print("Неверный выбор, попробуйте еще раз")