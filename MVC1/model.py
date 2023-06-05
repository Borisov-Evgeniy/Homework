import json

class Shoes:
    def __init__(self,gender,type,color,size,manufacture):
        self.gender = gender
        self.type = type
        self.color = color
        self.size = size
        self.manufacture = manufacture

    def __str__(self):
        return f'{self.manufacture} - {self.type}'

class DecodeError(Exception):
    pass

class Model:
    def __init__(self, filepath):
        self.filepath = filepath
        self.__shoes = {}
        try:
            self.data = json.load(open(self.filepath, 'r', encoding='utf-8'))
            for shoe in self.data.values():
                self.__shoes[f'{shoe["manufacture"]} {shoe["type"]}'] = Shoes(*shoe.values())
        except json.JSONDecodeError:
            raise DecodeError
        except FileNotFoundError:
            with open(self.filepath, 'w') as file:
                file.write("{}")

    @property
    def shoes(self):
        return self.__shoes

    def save_shoes(self):
        dict_shoes = {f'{shoes.manufacture} {shoes.type}' : shoes.__dict__ for shoes in self.__shoes.values()}
        json.dump(dict_shoes, open(self.filepath, 'w', encoding='utf-8'))
    def add_new_shoes(self, shoes_data):
        new_shoes = Shoes(*shoes_data.values())
        self.__shoes[f'{new_shoes.manufacture} {new_shoes.type}'] = new_shoes
        self.save_shoes()

    def find_shoes(self, keywords):
        shoes_dict = {}
        for i in self.__shoes.values():
            for word in keywords:
                if i in shoes_dict:
                    break
                for prop in i.__dict__.values():
                    if prop.isdigit():
                        continue
                    if word.lower() in str(prop).lower():
                        shoes_dict[i] = i
                        break
        return list(shoes_dict.values())



    def delete_shoes(self,shoes):
        if not shoes:
            return 'Информация для удаления не найдена!'
        elif len(shoes) == 1:
            shoes = shoes[0]
            key = f'{shoes.manufacture} {shoes.type}'
            self.__shoes.pop(key)
            self.save_shoes()
            return 'Информация удалена!'
        else:
            return "Cлишком много моделей!"