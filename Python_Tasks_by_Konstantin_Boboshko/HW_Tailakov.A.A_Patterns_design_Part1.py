# #Task 1
# class Car:
#     def __init__(self):
#         self.make = None
#         self.model = None
#         self.year = None
#         self.color = None
#         self.mileage = None
#
#     def __str__(self):
#         return f"Car: {self.year} {self.make} {self.model}, Color: {self.color}, Mileage: {self.mileage}"
#
# class CarBuilder:
#     def __init__(self):
#         self.car = Car()
#
#     def set_make(self, make):
#         self.car.make = make
#         return self
#
#     def set_model(self, model):
#         self.car.model = model
#         return self
#
#     def set_year(self, year):
#         self.car.year = year
#         return self
#
#     def set_color(self, color):
#         self.car.color = color
#         return self
#
#     def set_mileage(self, mileage):
#         self.car.mileage = mileage
#         return self
#
#     def build(self):
#         return self.car
#
# # Пример использования
# car_builder = CarBuilder()
# car = car_builder.set_make("Toyota").set_model("Corolla").set_year(2014).set_color("White").set_mileage(1000).build()
# print(car)

#Task2
# class Pasta:
#     def __init__(self):
#         self.pasta_type = None
#         self.sauce = None
#         self.fillings = []
#         self.add_ons = []
#
#     def __str__(self):
#         description = f"Type: {self.pasta_type}\n"
#         description += f"Sauce: {self.sauce}\n"
#         description += f"Fillings: {', '.join(self.fillings)}\n"
#         description += f"Add-ons: {', '.join(self.add_ons)}\n"
#         return description
#
# class PastaBuilder:
#     def __init__(self):
#         self.pasta = Pasta()
#
#     def set_pasta_type(self, pasta_type):
#         self.pasta.pasta_type = pasta_type
#         return self
#
#     def set_pasta_sauce(self, sauce):
#         self.pasta.sauce = sauce
#         return self
#
#     def add_filling(self, filling):
#         self.pasta.fillings.append(filling)
#         return self
#
#     def add_add_on(self, add_on):
#         self.pasta.add_ons.append(add_on)
#         return self
#
#     def build(self):
#         return self.pasta
#
# class PastaFactory:
#     def create_pasta(self, pasta_type):
#         builder = PastaBuilder()
#
#         if pasta_type == "Carbonara":
#             return builder.set_pasta_type("Carbonara") \
#                           .set_pasta_sauce("Creamy Alfredo") \
#                           .add_filling("Bacon") \
#                           .add_filling("Parmesan") \
#                           .build()
#         elif pasta_type == "Bolognese":
#             return builder.set_pasta_type("Bolognese") \
#                           .set_pasta_sauce("Meat Sauce") \
#                           .add_filling("Ground Beef") \
#                           .add_filling("Onions") \
#                           .add_filling("Tomatoes") \
#                           .build()
#         elif pasta_type == "Pesto":
#             return builder.set_pasta_type("Pesto") \
#                           .set_pasta_sauce("Basil Garlic and Olive Oil") \
#                           .add_filling("basil") \
#                           .add_filling("garlic") \
#                           .add_filling("pine nuts") \
#                           .add_add_on("Parmesan") \
#                           .build()
#         else:
#             raise ValueError("Invalid pasta type")
#
# # Пример использования
# factory = PastaFactory()
#
# carbonara = factory.create_pasta("Carbonara")
# print(carbonara)
#
# bolognese = factory.create_pasta("Bolognese")
# print(bolognese)
#
#
# aglio_e_olio = factory.create_pasta("Pesto")
# print(aglio_e_olio)

#Task 3
# import copy
#
# class PastaPrototype:
#     def clone(self):
#         return copy.deepcopy(self)
#
# class Pasta(PastaPrototype):
#     def __init__(self, pasta_type, sauce, fillings):
#         self.pasta_type = pasta_type
#         self.sauce = sauce
#         self.fillings = fillings
#
#     def __str__(self):
#         return f"Pasta: {self.pasta_type}, Sauce: {self.sauce}, Fillings: {', '.join(self.fillings)}"
#
# # Пример использования
# carbonara = Pasta("Carbonara", "Creamy Alfredo", ["Bacon", "Parmesan"])
#
# # Создание клона пасты Carbonara
# carbonara_clone = carbonara.clone()
# print(carbonara_clone)
#
# # изменение свойства клонированной пасты
# carbonara_clone.sauce = "Marinara"
# carbonara_clone.fillings.append("Mushrooms")
# carbonara_clone.fillings.append("Chilly flakes")
#
# # Вывод оригинальной пастуы и ее клона
# print(carbonara)
# print(carbonara_clone)