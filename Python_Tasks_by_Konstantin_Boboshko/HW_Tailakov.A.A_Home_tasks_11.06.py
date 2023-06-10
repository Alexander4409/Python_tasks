# 1. Реализуйте шаблон Factory Method, чтобы создать SocialMediaAccountFactory,
# который создает различные типы учетных записей социальных сетей (например, Facebook, Instagram, Twitter).
# Кроме того, реализуйте шаблон прокси, создав учетную запись ProxySocialMediaAccount,
# которая выступает в качестве прокси для фактической учетной записи в социальной сети,
# предоставляя дополнительные функции, такие как модерация контента и контроль доступа.

# from abc import ABC, abstractmethod
#
# class SocialMediaAccount(ABC):
#     @abstractmethod
#     def post(self, content):
#         pass
#
# class FacebookAccount(SocialMediaAccount):
#     def post(self, content):
#         print(f"Posting on Facebook: {content}")
#
# class InstagramAccount(SocialMediaAccount):
#     def post(self, content):
#         print(f"Posting on Instagram: {content}")
#
# class TwitterAccount(SocialMediaAccount):
#     def post(self, content):
#         print(f"Posting on Twitter: {content}")
#
# class SocialMediaAccountFactory(ABC):
#     @abstractmethod
#     def create_account(self):
#         pass
#
# class FacebookAccountFactory(SocialMediaAccountFactory):
#     def create_account(self):
#         return FacebookAccount()
#
# class InstagramAccountFactory(SocialMediaAccountFactory):
#     def create_account(self):
#         return InstagramAccount()
#
# class TwitterAccountFactory(SocialMediaAccountFactory):
#     def create_account(self):
#         return TwitterAccount()
#
# # Пример использования:
#
# account_factory = FacebookAccountFactory()
# account = account_factory.create_account()
# account.post("Hello, Facebook!")
#
# account_factory = InstagramAccountFactory()
# account = account_factory.create_account()
# account.post("Hello, Instagram!")
#
# account_factory = TwitterAccountFactory()
# account = account_factory.create_account()
# account.post("Hello, Twitter!")
#
# class ProxySocialMediaAccount(SocialMediaAccount):
#     def __init__(self, real_account):
#         self.real_account = real_account
#
#     def post(self, content):
#         if self._is_content_allowed(content):
#             self.real_account.post(content)
#         else:
#             print("Content moderation: This content is not allowed.")
#
#     def _is_content_allowed(self, content):
#         banned_words = ["spam", "virus", "inappropriate"]
#         for word in banned_words:
#             if word in content.lower():
#                 return False
#         return True
#
# # Пример использования прокси:
#
# facebook_account = FacebookAccount()
# proxy_account = ProxySocialMediaAccount(facebook_account)
#
# proxy_account.post("Hello, Facebook!")
# proxy_account.post("Inappropriate content!")


#
# 2. Создайте класс File, в котором опишите базовые методы для работы с файлами через функции, встроенные в python.
# Затем реализуйте шаблон Proxy, создав класс FileProxy, который действует как прокси для фактического класса File.
# FileProxy должен предоставлять дополнительные функции, такие как регистрация попыток чтения файлов,
# ограничение прав доступа и кэширование содержимого файла

# import os
#
# class File:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def read(self):
#         print(f"Reading file: {self.filename}")
#         with open(self.filename, 'r') as file:
#             content = file.read()
#         return content
#
#     def write(self, data):
#         print(f"Writing to file: {self.filename}")
#         with open(self.filename, 'w') as file:
#             file.write(data)
#
#     def append(self, data):
#         print(f"Appending to file: {self.filename}")
#         with open(self.filename, 'a') as file:
#             file.write(data)
#
#     def delete(self):
#         print(f"Deleting file: {self.filename}")
#         try:
#             os.remove(self.filename)
#             print(f"File deleted: {self.filename}")
#         except FileNotFoundError:
#             print(f"File not found: {self.filename}")
#
#
# class FileProxy:
#     def __init__(self, filename, role=None):
#         self.filename = filename
#         self.file = None
#         self.cache = None
#         self.access_logs = []
#         self.role = role
#
#     def read(self):
#         self._register_access("read")
#         if self._check_access("read"):
#             if self.cache is not None:
#                 print("Retrieving content from cache.")
#                 return self.cache
#             else:
#                 self.file = File(self.filename)
#                 content = self.file.read()
#                 self.cache = content
#                 return content
#
#     def write(self, data):
#         self._register_access("write")
#         if self._check_access("write"):
#             self.file = File(self.filename)
#             self.file.write(data)
#             self._clear_cache()
#
#     def append(self, data):
#         self._register_access("append")
#         if self._check_access("append"):
#             self.file = File(self.filename)
#             self.file.append(data)
#             self._clear_cache()
#
#     def delete(self):
#         self._register_access("delete")
#         if self._check_access("delete"):
#             self.file = File(self.filename)
#             self.file.delete()
#             self._clear_cache()
#
#     def _register_access(self, operation):
#         self.access_logs.append(operation)
#
#     def _check_access(self, operation):
#         if self.role is None:
#             print("Access denied. Your role is undefined.")
#             return False
#         elif self.role == "admin":
#             return True
#         elif self.role == "user":
#             if operation == "read":
#                 return True
#             else:
#                 print("Access denied. You do not have permission to perform this operation.")
#                 return False
#         else:
#             print("Access denied. Unknown role.")
#             return False
#
#     def _clear_cache(self):
#         self.cache = None
#
#
# # Пример использования класса FileProxy
#
# # Создаем экземпляр FileProxy с ролью "user"
# file_proxy = FileProxy('example.txt', 'user')
#
# # Чтение файла
# content = file_proxy.read()
# print(content)
#
# # Попытка записи в файл (будет отклонена, так как это юзер)
# file_proxy.write("Some data")  # сообщение "Access denied. You do not have permission to perform this operation."
#
# # Создаем экземпляр FileProxy с ролью "admin"
# file_proxy_admin = FileProxy('example.txt', 'admin')
#
# # Запись в файл (разрешено для админа)
# file_proxy_admin.write("Some data")  # сообщение "Writing to file: example.txt"
#
# # Повторное чтение файла (данные только из кэша)
# content_cached = file_proxy_admin.read()
# print(content_cached)  # содержимое файла без вывода "Reading file: example.txt"
#
# # Удаление файла (только админ)
# file_proxy_admin.delete()  # сообщение "Deleting file: example.txt"


# 3. Напишите программу дистанционного управления электронными устройствами (например, телевизором, DVD-плеером),
# используя шаблон Command. Реализуйте набор команд (например, PowerOnCommand, PowerOffCommand, VolumeUpCommand,
# VolumeDownCommand), которые инкапсулируют действия, выполняемые на устройствах.
# На пульте дистанционного управления должны быть кнопки для выполнения этих команд,
# и он должен иметь возможность отменить или повторить выполненные команды.
# Пример использования такого кода:

# 	remote_control = RemoteControl()
#
#
# 	power_on_command = PowerOnCommand(tv)
# 	volume_up_command = VolumeUpCommand(tv)
#
# 	remote_control.set_command(0, power_on_command)  # Кнопка 0 будет включать ТВ
# 	remote_control.set_command(1, volume_up_command)  # Кнопка 1 будет увеличивать громкость
#
# 	remote_control.press_button(0)  # Включает ТВ
# 	remote_control.press_button(1)  # Поднимает уровень громкости

# Класс команды
class Command:
    def execute(self):
        pass

    def undo(self):
        pass

# Команда включения устройства
class PowerOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.power_on()

    def undo(self):
        self.device.power_off()

# Команда выключения устройства
class PowerOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.power_off()

    def undo(self):
        self.device.power_on()

# Команда увеличения громкости
class VolumeUpCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.volume_up()

    def undo(self):
        self.device.volume_down()

# Команда уменьшения громкости
class VolumeDownCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.volume_down()

    def undo(self):
        self.device.volume_up()

# Класс удаленного управления
class RemoteControl:
    def __init__(self):
        self.commands = {}

    def set_command(self, button, command):
        self.commands[button] = command

    def press_button(self, button):
        if button in self.commands:
            command = self.commands[button]
            command.execute()

# Класс устройства (например, телевизора)
class Television:
    def __init__(self):
        self.power = False
        self.volume = 0

    def power_on(self):
        self.power = True
        print("Телевизор включен")

    def power_off(self):
        self.power = False
        print("Телевизор выключен")

    def volume_up(self):
        if self.power:
            self.volume += 1
            print("Уровень громкости:", self.volume)

    def volume_down(self):
        if self.power and self.volume > 0:
            self.volume -= 1
            print("Уровень громкости:", self.volume)

# Пример использования

tv = Television()

remote_control = RemoteControl()

power_on_command = PowerOnCommand(tv)
volume_up_command = VolumeUpCommand(tv)

remote_control.set_command(0, power_on_command) # Кнопка 0 будет включать ТВ
remote_control.set_command(1, volume_up_command)  # Кнопка 1 будет увеличивать громкость

remote_control.press_button(0)  # Включает ТВ
remote_control.press_button(1)# Поднимает уровень громкости
remote_control.press_button(1)
