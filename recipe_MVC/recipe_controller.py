class RecipeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_recipe(self, title, author, recipe_type, description, video_link, ingredients, cuisine):
        recipe = self.model(title, author, recipe_type, description, video_link, ingredients, cuisine)
        self.model.recipes.append(recipe)
        self.view.display_message("Recipe added successfully.")

    def delete_recipe(self, title):
        recipe = self.get_recipe_by_title(title)
        if recipe:
            self.model.recipes.remove(recipe)
            self.view.display_message("Recipe deleted successfully.")
        else:
            self.view.display_message("Recipe not found.")

    def search_recipe(self, title):
        recipe = self.get_recipe_by_title(title)
        if recipe:
            self.view.display_recipe(recipe)
        else:
            self.view.display_message("Recipe not found.")

    def get_recipe_by_title(self, title):
        for recipe in self.model.recipes:
            if recipe.title.lower() == title.lower():
                return recipe
        return None

    def save_recipes(self, filename):
        self.model.save_recipes(self.model.recipes, filename)

    def load_recipes(self, filename):
        self.model.recipes = self.model.load_recipes(filename)
