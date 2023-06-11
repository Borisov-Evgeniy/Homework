import os
from model import Recipe


class RecipeView:
    def __init__(self):
        self.recipe_db = None

    def set_recipe_db(self, recipe_db):
        self.recipe_db = recipe_db

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_menu(self):
        while True:
            self.clear_screen()
            print("Welcome to Recipe Book!")
            print("1. View Recipes")
            print("2. Add Recipe")
            print("3. Delete Recipe")
            print("4. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.view_recipes()
            elif choice == "2":
                self.add_recipe()
            elif choice == "3":
                self.delete_recipe()
            elif choice == "4":
                exit()

    def view_recipes(self):
        self.clear_screen()
        if len(self.recipe_db.recipes) == 0:
            print("No recipes found!")
        else:
            for recipe in self.recipe_db.recipes:
                print(f"Title: {recipe.title}")
                print(f"Author: {recipe.author}")
                print(f"Category: {recipe.category}")
                print(f"Description: {recipe.description}")
                print(f"Video Link: {recipe.video_link}")
                print("Ingredients:")
                for ingredient in recipe.ingredients:
                    print(f"- {ingredient}")
                print(f"Cuisine: {recipe.cuisine}")
                print("\n")

        input("Press enter to continue...")

    def get_recipe_info(self):
        self.clear_screen()
        title = input("Enter recipe title: ")
        author = input("Enter recipe author: ")
        category = input("Enter recipe category: ")
        description = input("Enter recipe description: ")
        video_link = input("Enter recipe video link: ")
        ingredients = []
        while True:
            ingredient = input("Enter ingredient (or q to quit): ")
            if ingredient == "q":
                break

            ingredients.append(ingredient)

        cuisine = input("Enter cuisine: ")

        return Recipe(title, author, category, description, video_link, ingredients,
                      cuisine)

    def add_recipe(self):
        self.clear_screen()
        recipe = self.get_recipe_info()
        self.recipe_db.add_recipe(recipe)
        print("Recipe added successfully!")
        input("Press enter to continue...")

    def delete_recipe(self):
        self.clear_screen()
        if len(self.recipe_db.recipes) == 0:
            print("No recipes found!")
        else:
            index = 1
            for recipe in self.recipe_db.recipes:
                print(f"{index}. {recipe.title}")
                index += 1

            choice = input("Enter the number of the recipe you want to delete (or q to quit): ")
            if choice == "q":
                return

            index = int(choice) - 1
            if index < 0 or index > len(self.recipe_db.recipes) - 1:
                print("Invalid choice!")
            else:
                recipe = self.recipe_db.recipes[index]
                self.recipe_db.delete_recipe(recipe)
                print("Recipe deleted successfully!")

            input("Press enter to continue...")