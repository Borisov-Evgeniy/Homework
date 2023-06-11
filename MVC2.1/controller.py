from model import RecipeDatabase
from view import RecipeView

class RecipeController:
    def __init__(self):
        self.recipe_db = RecipeDatabase('recipes.csv')
        self.recipe_view = RecipeView()
        self.recipe_view.set_recipe_db(self.recipe_db)

    def run(self):
        self.recipe_view.main_menu()