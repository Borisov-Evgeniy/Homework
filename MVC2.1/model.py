import csv
class Recipe:
    def __init__(self, title, author, category, description, video_link, ingredients, cuisine):
        self.title = title
        self.author = author
        self.category = category
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients
        self.cuisine = cuisine

class RecipeDatabase:
    def __init__(self, db_file):
        self.db_file = db_file
        self.recipes = []
        self.load_db()

    def load_db(self):
        try:
            with open(self.db_file, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    recipe = Recipe(row['Title'], row['Author'], row['Category'], row['Description'],
                                    row['Video Link'], row['Ingredients'].split(','), row['Cuisine'])
                    self.recipes.append(recipe)
        except:
            pass

    def save_db(self):
        with open(self.db_file, 'w', newline='') as csvfile:
            fieldnames = ['Title', 'Author', 'Category', 'Description', 'Video Link', 'Ingredients', 'Cuisine']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for recipe in self.recipes:
                writer.writerow({'Title': recipe.title, 'Author': recipe.author, 'Category': recipe.category,
                                 'Description': recipe.description, 'Video Link': recipe.video_link,
                                 'Ingredients': ','.join(recipe.ingredients), 'Cuisine': recipe.cuisine})

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        self.save_db()

    def delete_recipe(self, recipe):
        self.recipes.remove(recipe)
        self.save_db()