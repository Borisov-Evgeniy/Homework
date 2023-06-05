def add_title(title):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print(title.center(50, '='))
            result = func(*args,**kwargs)
            print('='*50)
            return result
        return wrapper
    return decorator


class View:

    @add_title('Ожидание ввода пользователя')
    def wait_user_answer(self):
        print(f"Ожидание ввода пользователя")
        print(f'Доступные команды:\n'
              f'1.Ввод обуви\n'
              f'2.Вывод коллекции обуви\n'
              f'3.Найти пару в коллекции\n'
              f'4.Удаление обувь из коллекции\n'
              f'Выход.Завершить работу.\n'
              )
        query = input('Выберите пункт меню: ')
        return query

    @add_title('Добавление новой обуви')
    def get_new_shoes_data(self):
        print('Добавление новой обуви')
        dict_shoes = {"Принадлежность": None,
                      "Тип обуви": None,
                      "Цвет": None,
                      "Размер": None,
                      "Производитель": None
                      }
        for key in dict_shoes.keys():
            dict_shoes[key] = input(f'Введите {key.lower()} : ')
        return dict_shoes
    @add_title('Ошибка загрузки')
    def throw_at_error(self,e):
        print(e)

    @add_title('Вывод сохраненной обуви: ')
    def show_shoes(self,shoes):
        print('Вывод коллекции: ')
        if shoes:
            [print(f'{i}.{mod}') for i,mod in enumerate(shoes,1)]
        else:
            print('Список пустой!')

    @add_title('Поиск обуви в коллекции:')
    def get_user_find_input(self):
        keywords = input('Введите список слов для поиска через пробел: ').split()
        return keywords

    @add_title('Название обуви')
    def get_shoes_name(self):
        shoes_name= input('Введите тип обуви: ')
        return shoes_name.strip()

    @add_title('Дополнительная информация')
    def get_delethion_context(self):
        number = int(input('Введите номер для удаления: '))
        return number

    @add_title('Результат удаления')
    def return_delete_shoes(self,result):
        print(result)
