from recipe_model import Recipe
from recipe_view import RecipeView
from recipe_controller import RecipeController


class RecipeApp:
    def __init__(self):
        self.model = Recipe
        self.view = RecipeView
        self.controller = RecipeController(self.model, self.view)
        self.filename = "recipes.txt"  # Имя файла для сохранения рецептов

    def run(self):
        self.controller.load_recipes(self.filename)

        while True:
            self.view.display_message("\nRecipe App Menu:")
            self.view.display_message("1. Add Recipe")
            self.view.display_message("2. Delete Recipe")
            self.view.display_message("3. Search Recipe")
            self.view.display_message("4. Save Recipes")
            self.view.display_message("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_recipe()
            elif choice == "2":
                self.delete_recipe()
            elif choice == "3":
                self.search_recipe()
            elif choice == "4":
                self.save_recipes()
            elif choice == "5":
                self.view.display_message("Exiting Recipe App...")
                break
            else:
                self.view.display_message("Invalid choice. Please try again.")

    def add_recipe(self):
        self.view.display_message("\nAdd Recipe:")
        title, author, recipe_type, description, video_link, ingredients, cuisine = self.view.get_recipe_input()
        self.controller.add_recipe(title, author, recipe_type, description, video_link, ingredients, cuisine)

    def delete_recipe(self):
        self.view.display_message("\nDelete Recipe:")
        title = self.view.get_recipe_title_input()
        self.controller.delete_recipe(title)

    def search_recipe(self):
        self.view.display_message("\nSearch Recipe:")
        title = self.view.get_recipe_title_input()
        self.controller.search_recipe(title)

    def save_recipes(self):
        self.controller.save_recipes(self.filename)


if __name__ == "__main__":
    app = RecipeApp()
    app.run()
