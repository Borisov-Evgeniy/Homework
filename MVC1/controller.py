from model import Model,DecodeError
from view import View

class Controller:
    def __init__(self):
        self.view = View()
        try:
            self.model = Model('shoes.txt')
        except DecodeError as e:
            self.view.throw_at_error(e)
    def run(self):
        query = None
        while query != 'Выход':
            query = self.view.wait_user_answer()
            self.resolve_user_answer(query)

    def resolve_user_answer(self,query):
        if query == '1':
            shoes_data = self.view.get_new_shoes_data()
            self.model.add_new_shoes(shoes_data)
        if query == '2':
            shoes = self.model.shoes
            self.view.show_shoes(shoes)
        if query == '3':
            keywords = self.view.get_user_find_input()
            shoes = self.model.find_shoes(keywords)
            self.view.show_shoes(shoes)
        if query == '4':
            shoes_name = self.view.get_shoes_name()
            shoes = self.model.find_shoes(shoes_name)
            result = self.model.delete_shoes(shoes)
            if result == "Cлишком много моделей!":
                self.view.show_shoes(shoes)
                number = self.view.get_delethion_context()
                result = self.model.delete_shoes(shoes[number - 1])
            self.view.return_delete_shoes(result)
