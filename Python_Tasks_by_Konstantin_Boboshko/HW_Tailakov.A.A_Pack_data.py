#Task 1
# import json
# import pickle
#
#
# class Car:
#     def __init__(self):
#         self.model_name = ''
#         self.year = 0
#         self.manufacturer = ''
#         self.engine_size = 0
#         self.color = ''
#         self.price = 0
#
#     def set_model_name(self, model_name):
#         self.model_name = model_name
#
#     def set_year(self, year):
#         self.year = year
#
#     def set_manufacturer(self, manufacturer):
#         self.manufacturer = manufacturer
#
#     def set_engine_size(self, engine_size):
#         self.engine_size = engine_size
#
#     def set_color(self, color):
#         self.color = color
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_model_name(self):
#         return self.model_name
#
#     def get_year(self):
#         return self.year
#
#     def get_manufacturer(self):
#         return self.manufacturer
#
#     def get_engine_capacity(self):
#         return self.engine_size
#
#     def get_color(self):
#         return self.color
#
#     def get_price(self):
#         return self.price
#
#     def input_car_data(self):
#         self.set_model_name(input("Input the model of the vehicle: "))
#         self.set_year(int(input("Enter year of manufacture: ")))
#         self.set_manufacturer(input("Enter the manufacturer: "))
#         self.set_engine_size(float(input("Enter the engine capacity: ")))
#         self.set_color(input("Enter the colour of the vehicle: "))
#         self.set_price(float(input("Enter the price: ")))
#
#     def output_car_data(self):
#         print(f"Model: {self.get_model_name()}")
#         print(f"The year of manufacture: {self.get_year()}")
#         print(f"Manufacturer: {self.get_manufacturer()}")
#         print(f"Engine capacity: {self.get_engine_capacity()}")
#         print(f"Colour of the vehicle: {self.get_color()}")
#         print(f"Price: {self.get_price()}")
#
#     def pack_json(self, filename):
#         with open(filename, 'w') as f:
#             json.dump(self.__dict__, f, indent=4)
#
#     def unpack_json(self, filename):
#         with open(filename, 'r') as f:
#             data = json.load(f)
#             self.model_name = data['model_name']
#             self.year = data['year']
#             self.manufacturer = data['manufacturer']
#             self.engine_size = data['engine_size']
#             self.color = data['color']
#             self.price = data['price']
#
#     def pack_pickle(self, filename):
#         with open(filename, 'wb') as f:
#             pickle.dump(self.__dict__, f)
#
#     def unpack_pickle(self, filename):
#         with open(filename, 'rb') as f:
#             data = pickle.load(f)
#             self.model_name = data['model_name']
#             self.year = data['year']
#             self.manufacturer = data['manufacturer']
#             self.engine_size = data['engine_size']
#             self.color = data['color']
#             self.price = data['price']
#
#
# # Использование:
#
# my_car = Car()
#
# # Ввод данных
# my_car.input_car_data()
#
# # Выгрузка в файлы JSON и Pickle
# my_car.pack_json('car.json')
# my_car.pack_pickle('car.pkl')
#
# # Создание нового объекта из файла JSON
# new_car = Car()
# new_car.unpack_json('car.json')
# new_car.output_car_data()
#
# # Создание нового объекта из файла Pickle
# new_car = Car()
# new_car.unpack_pickle('car.pkl')
# new_car.output_car_data()
#
# # Вывод данных
# print(f"Model: {my_car.get_model_name()}")
# print(f"The year of manufacture: {my_car.get_year()}")

#Task 2
# import json
# import pickle
#
# class Book:
#     def __init__(self):
#         self.title = ''
#         self.year = 0
#         self.publisher = ''
#         self.genre = ''
#         self.author = ''
#         self.price = 0
#
#     def set_title(self, title):
#         self.title = title
#
#     def set_year(self, year):
#         self.year = year
#
#     def set_publisher(self, publisher):
#         self.publisher = publisher
#
#     def set_genre(self, genre):
#         self.genre = genre
#
#     def set_author(self, author):
#         self.author = author
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_title(self):
#         return self.title
#
#     def get_year(self):
#         return self.year
#
#     def get_publisher(self):
#         return self.publisher
#
#     def get_genre(self):
#         return self.genre
#
#     def get_author(self):
#         return self.author
#
#     def get_price(self):
#         return self.price
#
#     def input_book_data(self):
#         self.set_title(input("Enter book title: "))
#         self.set_year(int(input("Enter year of issue: ")))
#         self.set_publisher(input("Enter publisher: "))
#         self.set_genre(input("Enter Genre: "))
#         self.set_author(input("Enter author: "))
#         self.set_price(float(input("Enter the price ")))
#
#     def output_book_data(self):
#         print(f"Book title: {self.get_title()}")
#         print(f"Year of issue: {self.get_year()}")
#         print(f"Publisher: {self.get_publisher()}")
#         print(f"Genre: {self.get_genre()}")
#         print(f"Author: {self.get_author()}")
#         print(f"Price: {self.get_price()}")
#
#     def pack_book_data_json(self, filename):
#         with open(filename, 'w') as f:
#             json.dump(self.__dict__, f)
#
#     def unpack_book_data_json(self, filename):
#         with open(filename, 'r') as f:
#             data = json.load(f)
#             self.__dict__.update(data)
#
#     def pack_book_data_pickle(self, filename):
#         with open(filename, 'wb') as f:
#             pickle.dump(self.__dict__, f)
#
#     def unpack_book_data_pickle(self, filename):
#         with open(filename, 'rb') as f:
#             data = pickle.load(f)
#             self.__dict__.update(data)
#
# my_book = Book()
#
# my_book.input_book_data()
# my_book.output_book_data()
#
# print(f"Book title: {my_book.get_title()}")
# print(f"Year of issue: {my_book.get_year()}")
#
# my_book.pack_book_data_json('book_data.json')
# my_book.unpack_book_data_json('book_data.json')
# my_book.output_book_data()
#
# my_book.pack_book_data_pickle('book_data.pickle')
# my_book.unpack_book_data_pickle('book_data.pickle')
# my_book.output_book_data()

#Task3

import json
import pickle
class Stadium:
    def __init__(self):
        self.name = ''
        self.opening_date = ''
        self.country = ''
        self.city = ''
        self.capacity = 0

    def set_name(self, name):
        self.name = name

    def set_opening_date(self, opening_date):
        self.opening_date = opening_date

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_name(self):
        return self.name

    def get_opening_date(self):
        return self.opening_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

    def input_stadium_data(self):
        self.set_name(input("Enter stadium name: "))
        self.set_opening_date(input("Enter opening date: "))
        self.set_country(input("Enter country: "))
        self.set_city(input("Enter city: "))
        self.set_capacity(int(input("Enter capacity: ")))

    def output_stadium_data(self):
        print(f"Stadium name: {self.get_name()}")
        print(f"Opening date: {self.get_opening_date()}")
        print(f"Country: {self.get_country()}")
        print(f"City: {self.get_city()}")
        print(f"Stadium Capacity: {self.get_capacity()}")

    def dump_json(self, filename):
        with open(filename, 'w') as f:
            json.dump({'name': self.name, 'opening_date': self.opening_date,
                       'country': self.country, 'city': self.city,
                       'capacity': self.capacity}, f)

    def load_json(self, filename):
        with open(filename, 'r') as f:
            data_dict = json.load(f)
            self.name = data_dict['name']
            self.opening_date = data_dict['opening_date']
            self.country = data_dict['country']
            self.city = data_dict['city']
            self.capacity = data_dict['capacity']

    def dump_pickle(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    def load_pickle(self, filename):
        with open(filename, 'rb') as f:
            obj = pickle.load(f)
            self.name = obj.name
            self.opening_date = obj.opening_date
            self.country = obj.country
            self.city = obj.city
            self.capacity = obj.capacity

my_stadium = Stadium()

my_stadium.input_stadium_data()
my_stadium.output_stadium_data()

# Dumping and loading with JSON
json_file = 'stadium.json'
my_stadium.dump_json(json_file)
my_stadium.load_json(json_file)
my_stadium.output_stadium_data()

# Dumping and loading with Pickle
pickle_file = 'stadium.pickle'
my_stadium.dump_pickle(pickle_file)
my_stadium.load_pickle(pickle_file)
my_stadium.output_stadium_data()

print(f"Stadium name: {my_stadium.get_name()}")
print(f"Stadium Capacity: {my_stadium.get_capacity()}")





