import json

class Recipe:
    def __init__(self, title, author, recipe_type, description, video_link, ingredients, cuisine):
        self.title = title
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients
        self.cuisine = cuisine

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nType: {self.recipe_type}\nDescription: {self.description}\nVideo Link: {self.video_link}\nIngredients: {self.ingredients}\nCuisine: {self.cuisine}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "recipe_type": self.recipe_type,
            "description": self.description,
            "video_link": self.video_link,
            "ingredients": self.ingredients,
            "cuisine": self.cuisine
        }

    @staticmethod
    def from_dict(recipe_dict):
        return Recipe(
            recipe_dict["title"],
            recipe_dict["author"],
            recipe_dict["recipe_type"],
            recipe_dict["description"],
            recipe_dict["video_link"],
            recipe_dict["ingredients"],
            recipe_dict["cuisine"]
        )

    @staticmethod
    def save_recipes(recipes, filename):
        recipe_dicts = [recipe.to_dict() for recipe in recipes]
        with open(filename, "w") as file:
            json.dump(recipe_dicts, file, indent=4)

    @staticmethod
    def load_recipes(filename):
        try:
            with open(filename, "r") as file:
                recipe_dicts = json.load(file)
                recipes = [Recipe.from_dict(recipe_dict) for recipe_dict in recipe_dicts]
                return recipes
        except FileNotFoundError:
            return []
