#1. Создайте программу Python для интернет-магазина, состоящую из двух основных классов:
# CustomerManager и ProductInventory. Класс CustomerManager должен отвечать за обработку операций, связанных с
# клиентами, таких как добавление новых клиентов, обновление информации о клиентах и получение данных о клиентах.
# Он должен иметь такие методы, как add_customer(), update_customer() и get_customer().
# Класс ProductInventory должен отвечать за управление запасами товаров в магазине.
# Он должен обрабатывать такие операции, как добавление продуктов, обновление информации о продукте и получение
# сведений о продукте. Он должен иметь такие методы, как add_product(), update_product() и get_product().
# Разделяя управление клиентами и запасами продуктов на отдельные классы, вы гарантируете, что каждый класс
# несет единую ответственность, делая программу более модульной и простой в обслуживании.

# class CustomerManager:
#     def __init__(self):
#         self.customers = []
#
#     def add_customer(self, customer):
#         self.customers.append(customer)
#
#     def update_customer(self, customer_id, new_info):
#         for customer in self.customers:
#             if customer["id"] == customer_id:
#                 customer.update(new_info)
#                 break
#
#     def get_customer(self, customer_id):
#         for customer in self.customers:
#             if customer["id"] == customer_id:
#                 return customer
#         return None
#
#
# class ProductInventory:
#     def __init__(self):
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def update_product(self, product_id, new_info):
#         for product in self.products:
#             if product["id"] == product_id:
#                 product.update(new_info)
#                 break
#
#     def get_product(self, product_id):
#         for product in self.products:
#             if product["id"] == product_id:
#                 return product
#         return None
#
#
# # Пример использования
#
# customer_manager = CustomerManager()
# product_inventory = ProductInventory()
#
# # Добавление клиентов
# customer_manager.add_customer({"id": 1, "name": "John Doe"})
# customer_manager.add_customer({"id": 2, "name": "Jane Smith"})
#
# # Добавление продуктов
# product_inventory.add_product({"id": 1, "name": "Product 1"})
# product_inventory.add_product({"id": 2, "name": "Product 2"})
#
# # Обновление информации о клиенте
# customer_manager.update_customer(1, {"name": "John Doe Updated"})
#
# # Обновление информации о продукте
# product_inventory.update_product(2, {"name": "Product 2 Updated"})
#
# # Получение данных о клиенте
# customer = customer_manager.get_customer(1)
# print("Customer:", customer)
#
# # Получение сведений о продукте
# product = product_inventory.get_product(2)
# print("Product:", product)

#2. Разработайте систему управления библиотекой Python, позволяющую добавлять новые типы книг без изменения существующей
# кодовой базы. В системе должен быть базовый класс Book, определяющий общие свойства и методы для всех типов книг.
# Подклассы, такие как FictionBook, NonFictionBook и ReferenceBook, должны наследоваться от класса Book и
# предоставлять определенные реализации для соответствующих типов. Чтобы добавить новый тип книги, вы должны иметь
# возможность создать новый подкласс книги и реализовать необходимые функции без изменения существующего кода.
# Библиотечная система должна по-прежнему иметь возможность беспрепятственно обрабатывать новый тип книг. Придерживаясь
# принципа открытости/закрытости, система управления библиотекой позволит легко расширять ее без необходимости
# изменения основной кодовой базы, повышая удобство сопровождения и снижая риск появления ошибок.

# class Book:
#     def __init__(self, title, author, publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#
#     def get_title(self):
#         return self.title
#
#     def get_author(self):
#         return self.author
#
#     def get_publication_year(self):
#         return self.publication_year
#
#
# class FictionBook(Book):
#     def __init__(self, title, author, publication_year, genre):
#         super().__init__(title, author, publication_year)
#         self.genre = genre
#
#     def get_genre(self):
#         return self.genre
#
#
# class NonFictionBook(Book):
#     def __init__(self, title, author, publication_year, topic):
#         super().__init__(title, author, publication_year)
#         self.topic = topic
#
#     def get_topic(self):
#         return self.topic
#
#
# class ReferenceBook(Book):
#     def __init__(self, title, author, publication_year, department):
#         super().__init__(title, author, publication_year)
#         self.department = department
#
#     def get_department(self):
#         return self.department
#
#
# # Использование
#
# # Создание различных книг
# fiction_book = FictionBook("Fiction Book", "John Doe", 2022, "Mystery")
# non_fiction_book = NonFictionBook("Non-Fiction Book", "Jane Smith", 2021, "History")
# reference_book = ReferenceBook("Reference Book", "James Johnson", 2020, "Science")
#
# # Получение информации
# print("Title:", fiction_book.get_title())
# print("Author:", non_fiction_book.get_author())
# print("Publication Year:", reference_book.get_publication_year())
# print("Genre:", fiction_book.get_genre())
# print("Topic:", non_fiction_book.get_topic())
# print("Department:", reference_book.get_department())

# 3. Создайте программу Python, определяющую иерархию классов для различных геометрических фигур, таких как Shape,
# Circle, Rectangle и Triangle. Класс Shape должен служить базовым классом, предоставляя общие свойства и методы
# для всех фигур. Каждый конкретный класс формы (Circle, Rectangle, Triangle) должен наследоваться от
# Shape и реализовывать свои собственные методы, такие как calculate_area() и calculate_perimeter().
# Программа должна позволять вам рассматривать любую фигуру как экземпляр класса Shape, обеспечивая соблюдение
# принципа подстановки Лисков. Это означает, что вы должны иметь возможность заменить любую конкретную фигуру
# объектом Shape в любой части программы, не влияя на её выполнение. Разрабатывая иерархию классов в соответствии
# с принципом замещения Лискова, вы создаете систему, которая является более гибкой, расширяемой и способной
# единообразно обрабатывать операции, связанные с формами.

# import math
#
#
# class Shape:
#     def calculate_area(self):
#         pass
#
#     def calculate_perimeter(self):
#         pass
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return math.pi * self.radius ** 2
#
#     def calculate_perimeter(self):
#         return 2 * math.pi * self.radius
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
#     def calculate_perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# class Triangle(Shape):
#     def __init__(self, side1, side2, side3):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#
#     def calculate_area(self):
#         # Использование формулы Герона
#         s = (self.side1 + self.side2 + self.side3) / 2
#         return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
#
#     def calculate_perimeter(self):
#         return self.side1 + self.side2 + self.side3
#
#
# # Пример использования
#
# circle = Circle(5)
# rectangle = Rectangle(4, 6)
# triangle = Triangle(3, 4, 5)
#
# # Рассматриваем фигуры как экземпляры класса Shape
# shapes = [circle, rectangle, triangle]
#
# # Вычисление площади и периметра для каждой фигуры
# for shape in shapes:
#     print("Area:", shape.calculate_area())
#     print("Perimeter:", shape.calculate_perimeter())
#     print()
#
# # Замена конкретной фигуры объектом Shape
# circle_as_shape = Shape()
# circle_as_shape.calculate_area()
# circle_as_shape.calculate_perimeter()

#4. Разработайте программу Python для службы обмена сообщениями, которая включает два отдельных интерфейса:
# TextMessaging и MultimediaMessaging. Интерфейс TextMessaging должен определять методы, специфичные для текстовых
# сообщений, такие как send_text_message(), receive_text_message() и get_message_history(). Интерфейс
# MultimediaMessaging должен включать методы, специфичные для мультимедийных сообщений, такие как
# send_multimedia_message(), Receive_multimedia_message() и view_media_gallery(). Классы, представляющие различные
# службы обмена сообщениями, должны реализовывать соответствующие интерфейсы в зависимости от их возможностей.
# Например, класс, реализующий TextMessaging, может обрабатывать текстовые сообщения, а класс, реализующий
# MultimediaMessaging, может обрабатывать как текстовые, так и мультимедийные сообщения. Разделяя интерфейсы,
# вы гарантируете, что классам нужно будет реализовать только соответствующие методы, предотвращая их принуждение
# к предоставлению ненужной функциональности. Это способствует лучшей организации кода и снижает вероятность
# раздувания классов или нарушения принципа единой ответственности.

# from abc import ABC, abstractmethod
#
#
# class TextMessaging(ABC):
#     @abstractmethod
#     def send_text_message(self, message):
#         pass
#
#     @abstractmethod
#     def receive_text_message(self):
#         pass
#
#     @abstractmethod
#     def get_message_history(self):
#         pass
#
#
# class MultimediaMessaging(ABC):
#     @abstractmethod
#     def send_multimedia_message(self, message, media):
#         pass
#
#     @abstractmethod
#     def receive_multimedia_message(self):
#         pass
#
#     @abstractmethod
#     def view_media_gallery(self):
#         pass
#
#
# class TextMessageService(TextMessaging):
#     def __init__(self):
#         self.message_history = []
#
#     def send_text_message(self, message):
#         print("Sending text message:", message)
#         self.message_history.append(message)
#
#     def receive_text_message(self):
#         if self.message_history:
#             return self.message_history[-1]
#         else:
#             return "No text messages received."
#
#     def get_message_history(self):
#         return self.message_history
#
#
# class MultimediaMessageService(MultimediaMessaging):
#     def __init__(self):
#         self.message_history = []
#         self.media_gallery = []
#
#     def send_multimedia_message(self, message, media):
#         print("Sending multimedia message:", message, "with media:", media)
#         self.message_history.append(message)
#         self.media_gallery.append(media)
#
#     def receive_multimedia_message(self):
#         if self.message_history:
#             return self.message_history[-1]
#         else:
#             return "No multimedia messages received."
#
#     def view_media_gallery(self):
#         return self.media_gallery
#
#
# # Пример использования
#
# text_service = TextMessageService()
# multimedia_service = MultimediaMessageService()
#
# text_service.send_text_message("Hello!")
# multimedia_service.send_multimedia_message("Check out this photo.", "photo.jpg")
#
# print(text_service.receive_text_message())
# print(multimedia_service.receive_multimedia_message())
#
# print(text_service.get_message_history())
# print(multimedia_service.view_media_gallery())

#5. Разработайте систему ведения журнала Python, которая поддерживает различные типы средств ведения журнала, например
# ConsoleLogger, FileLogger и DatabaseLogger. Реализуйте принцип инверсии зависимостей, используя абстракции
# (интерфейсы) для ведения журнала. Определите интерфейс с именем Logger, который включает такие методы,
# как log_info(), log_warning() и log_error(). Каждый класс регистратора (ConsoleLogger, FileLogger, DatabaseLogger)
# должен реализовать этот интерфейс и предоставить собственную реализацию методов ведения журнала. Модули высокого
# уровня в системе должны зависеть от интерфейса регистратора, а не от конкретных реализаций регистратора.
# Это позволяет легко подключать или заменять различные типы регистраторов, не влияя на функциональность модулей
# высокого уровня. Придерживаясь принципа инверсии зависимостей, вы создаете гибкую и расширяемую систему ведения
# журналов, которая обеспечивает слабую связанность и модульность вашей кодовой базы.

from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log_info(self, message):
        pass

    @abstractmethod
    def log_warning(self, message):
        pass

    @abstractmethod
    def log_error(self, message):
        pass


class ConsoleLogger(Logger):
    def log_info(self, message):
        print("INFO:", message)

    def log_warning(self, message):
        print("WARNING:", message)

    def log_error(self, message):
        print("ERROR:", message)


class FileLogger(Logger):
    def __init__(self, file_path):
        self.file_path = file_path

    def log_info(self, message):
        self._write_log("INFO", message)

    def log_warning(self, message):
        self._write_log("WARNING", message)

    def log_error(self, message):
        self._write_log("ERROR", message)

    def _write_log(self, level, message):
        with open(self.file_path, "a") as file:
            log_entry = f"{level}: {message}"
            file.write(log_entry + "\n")


class DatabaseLogger(Logger):
    def __init__(self, database):
        self.database = database

    def log_info(self, message):
        self._save_log("INFO", message)

    def log_warning(self, message):
        self._save_log("WARNING", message)

    def log_error(self, message):
        self._save_log("ERROR", message)

    def _save_log(self, level, message):
        log_entry = f"{level}: {message}"
        # save log entry to database


# Пример использования

logger = ConsoleLogger()
logger.log_info("This is an informational message.")
logger.log_warning("This is a warning message.")
logger.log_error("This is an error message.")

file_logger = FileLogger("log.txt")
file_logger.log_info("This is an informational message.")
file_logger.log_warning("This is a warning message.")
file_logger.log_error("This is an error message.")

database_logger = DatabaseLogger("example_database")
database_logger.log_info("This is an informational message.")
database_logger.log_warning("This is a warning message.")
database_logger.log_error("This is an error message.")
