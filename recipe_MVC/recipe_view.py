class RecipeView:
    @staticmethod
    def display_recipe(recipe):
        print(recipe)

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def get_recipe_input():
        title = input("Enter recipe title: ")
        author = input("Enter recipe author: ")
        recipe_type = input("Enter recipe type: ")
        description = input("Enter recipe description: ")
        video_link = input("Enter recipe video link: ")
        ingredients = input("Enter recipe ingredients (comma-separated): ").split(",")
        cuisine = input("Enter recipe cuisine: ")

        return title, author, recipe_type, description, video_link, ingredients, cuisine

    @staticmethod
    def get_recipe_title_input():
        return input("Enter recipe title to search/delete: ")
