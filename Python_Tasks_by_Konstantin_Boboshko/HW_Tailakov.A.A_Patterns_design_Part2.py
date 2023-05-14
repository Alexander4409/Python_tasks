#Task 1
# class Command:
#     def execute(self):
#         pass
#
#
# class Light:
#     def turn_on(self):
#         print("Light is ON")
#
#     def turn_off(self):
#         print("Light is OFF")
#
#
# class LightOnCommand(Command):
#     def __init__(self, light):
#         self.light = light
#
#     def execute(self):
#         self.light.turn_on()
#
#
# class LightOffCommand(Command):
#     def __init__(self, light):
#         self.light = light
#
#     def execute(self):
#         self.light.turn_off()
#
#
# class RemoteControl:
#     def __init__(self):
#         self.commands = {}
#
#     def register_command(self, command_name, command):
#         self.commands[command_name] = command
#
#     def execute_command(self, command_name):
#         if command_name in self.commands:
#             self.commands[command_name].execute()
#         else:
#             print("Unknown command")
#
#
# # Создаем объекты освещения и команды для включения и выключения света
# light = Light()
# light_on_command = LightOnCommand(light)
# light_off_command = LightOffCommand(light)
#
# # Создаем пульт и регистрируем команды
# remote_control = RemoteControl()
# remote_control.register_command("ON", light_on_command)
# remote_control.register_command("OFF", light_off_command)
#
# # Тестируем работу пульта
# remote_control.execute_command("ON")  # Включаем свет
# remote_control.execute_command("OFF")  # Выключаем свет
# remote_control.execute_command("Switch")  # Команда не зарегистрирована

#Task 2
# import time
#
#
# class NumberSet:
#     def get_numbers(self):
#         pass
#
#
# class FileNumberSet(NumberSet):
#     def __init__(self, filename):
#         self.filename = filename
#         self.numbers = []
#         self.load_numbers()
#
#     def load_numbers(self):
#         # Загрузка чисел из файла
#         with open(self.filename, 'r') as file:
#             numbers = file.read().split()
#             self.numbers = [int(num) for num in numbers]
#
#     def get_numbers(self):
#         return self.numbers
#
#
# class NumberSetProxy(NumberSet):
#     def __init__(self, number_set):
#         self.number_set = number_set
#
#     def get_numbers(self):
#         self.log_access()
#         return self.number_set.get_numbers()
#
#     def log_access(self):
#         with open('log.txt', 'a') as file:
#             timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#             file.write(f'Accessed number set at {timestamp}\n')
#
#
# class NumberSetObserver:
#     def __init__(self, number_set):
#         self.number_set = number_set
#         self.observers = []
#         self.start_monitoring()
#
#     def start_monitoring(self):
#         while True:
#             # Проверяем, изменился ли файл
#             if self.is_file_updated():
#                 self.number_set.load_numbers()
#                 self.notify_observers()
#             time.sleep(1)
#
#     def is_file_updated(self):
#         # Здесь можно реализовать логику проверки изменений в файле но у меня как всегда мало времени :(
#         # В данном примере просто считаем, что файл всегда обновляется
#         return True
#
#     def notify_observers(self):
#         for observer in self.observers:
#             observer.notify()
#
#     def attach_observer(self, observer):
#         self.observers.append(observer)
#
#
# class NumberSetStatistics:
#     def __init__(self, number_set):
#         self.number_set = number_set
#
#     def notify(self):
#         numbers = self.number_set.get_numbers()
#         if numbers:
#             print(f'Sum: {sum(numbers)}')
#             print(f'Min: {min(numbers)}')
#             print(f'Max: {max(numbers)}')
#
#
# # Создание экземпляра FileNumberSet
# file_number_set = FileNumberSet('numbers.txt')
#
# # Создание экземпляра NumberSetProxy и NumberSetObserver с использованием одного экземпляра FileNumberSet
# proxy_number_set = NumberSetProxy(file_number_set)
# observer = NumberSetObserver(file_number_set)
#
# # Подключение наблюдателя NumberSetStatistics
# observer.attach_observer(NumberSetStatistics(file_number_set))
#
# # Получение чисел с использованием прокси-объекта
# numbers = proxy_number_set.get_numbers()
# print(numbers)

#Task 3
# Реализация паттерна Одиночка (Singleton)
class Library:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls.books = []
        return cls._instance

    def add_book(self, book):
        self.books.append(book)
        Logger().log(f"Added book: {book.title}")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            Logger().log(f"Removed book: {book.title}")

    def display_books(self):
        Logger().log("Book Catalog:")
        for book in self.books:
            Logger().log(str(book))

# Реализация паттерна Одиночка (Singleton)
class Logger:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls.log_file = open("log.txt", "a")  # Открыть лог-файл для записи
        return cls._instance

    def log(self, message):
        print(message)
        self.log_file.write(message + "\n")

# Реализация паттерна Строитель (Builder)
class BookBuilder:
    def __init__(self):
        self.book = Book()

    def set_title(self, title):
        self.book.title = title
        return self

    def set_author(self, author):
        self.book.author = author
        return self

    def set_publisher(self, publisher):
        self.book.publisher = publisher
        return self

    def build(self):
        return self.book

class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publisher = ""

    def __str__(self):
        return f"Book: {self.title} by {self.author}, published by {self.publisher}"

# Реализация паттерна Строитель (Builder)
class LibrarianBuilder:
    def __init__(self):
        self.librarian = Librarian()

    def set_name(self, name):
        self.librarian.name = name
        return self

    def set_id(self, id):
        self.librarian.id = id
        return self

    def build(self):
        return self.librarian

class Librarian:
    def __init__(self):
        self.name = ""
        self.id = ""

    def __str__(self):
        return f"Librarian: {self.name} (ID: {self.id})"

# Реализация паттерна Строитель (Builder)
class ReaderBuilder:
    def __init__(self):
        self.reader = Reader()

    def set_name(self, name):
        self.reader.name = name
        return self

    def set_membership_number(self, membership_number):
        self.reader.membership_number = membership_number
        return self

    def build(self):
        return self.reader

class Reader:
    def __init__(self):
        self.name = ""
        self.membership_number = ""

    def __str__(self):
        return f"Reader: {self.name} (Membership No: {self.membership_number})"

# Реализация паттерна Наблюдатель (Observer)
class Observable:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

class Logger(Observable):
    def __init__(self):
        super().__init__()
        self.log_file = open("log.txt", "a")  # Открыть лог-файл для записи

    def log(self, message):
        print(message)
        self.log_file.write(message + "\n")
        self.notify_observers(message)

class Display:
    def update(self, message):
        print(f"Displaying: {message}")

# Пример использования:
library = Library()
logger = Logger()
display = Display()
logger.register_observer(display)

# Добавление книги в библиотеку
book_builder = BookBuilder()
book_builder.set_title("Book Title")
book_builder.set_author("Author Name")
book_builder.set_publisher("Publisher Name")
book = book_builder.build()
library.add_book(book)

# Удаление книги из библиотеки
library.remove_book(book)

# Закрытие лог-файла
logger.log_file.close()

