# 1. Напишите функцию analysis_and_summarize_file, которая принимает имя файла в
# качестве входных данных. Файл содержит большое количество текстовых данных.
# Функция должна прочитать содержимое файла, проанализировать данные для сбора
# соответствующей информации (например, частота слов, количество строк, средняя длина слова)
# и создать сводный отчет в новом файле.

# def analysis_and_summarize_file(file_name):
#     with open(file_name, 'r', encoding="utf-8") as f:
#         content = f.read()
#
#         # Разделение текста на строки
#         lines = content.split('\n')
#
#         # Подсчет количества строк
#         num_lines = len(lines)
#
#         # Разделение текста на слова
#         words = content.split()
#
#         # Подсчет количества слов
#         num_words = len(words)
#
#         # Подсчет частоты слов
#         word_frequency = {}
#         for word in words:
#             if word in word_frequency:
#                 word_frequency[word] += 1
#             else:
#                 word_frequency[word] = 1
#
#         # Вычисление средней длины слова
#         total_word_length = sum(len(word) for word in words)
#         average_word_length = total_word_length / num_words
#
#         # Создание сводного отчета
#         report = f"Файл: {file_name}\n"
#         report += f"Количество строк: {num_lines}\n"
#         report += f"Количество слов: {num_words}\n"
#         report += f"Средняя длина слова: {average_word_length:.2f}\n"
#         report += "Частота слов:\n"
#         for word, frequency in word_frequency.items():
#             report += f"{word}: {frequency}\n"
#
#         # Создание нового файла с отчетом
#         report_filename = f"{file_name}_summary.txt"
#         with open(report_filename, 'w') as report_file:
#             report_file.write(report)
#
#         print(f"Сводный отчет создан в файле: {report_filename}")
#
#     # Пример использования функции
#
#
# analysis_and_summarize_file("log.txt")


# 2. Напишите две функции: encrypt_file и decrypt_file. Функция encrypt_file должна
# принимать имя файла и ключ в качестве входных данных, считывать содержимое файла,
# шифровать содержимое с помощью пользовательского алгоритма шифрования и записывать
# зашифрованные данные в новый файл. Функция decrypt_file должна принимать имя файла
# и тот же ключ в качестве входных данных, читать зашифрованное содержимое файла,
# расшифровывать содержимое с использованием обратного алгоритма и записывать
# расшифрованные данные в новый файл. Создайте декоратор с именем encryption_logging,
# который регистрирует сведения об операциях шифрования и дешифрования,
# такие как имя файла, ключ и отметка времени.
# import time
#
# def encryption_logging(func):
#     def wrapper(filename, key):
#         timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
#         print(f"Encryption operation started at {timestamp}")
#         print(f"File: {filename}")
#         print(f"Key: {key}")
#         result = func(filename, key)
#         print(f"Encryption operation completed at {timestamp}")
#         return result
#     return wrapper
#
# @encryption_logging
# def encrypt_file(filename, key):
#     with open(filename, 'r') as file:
#         content = file.read()
#
#     encrypted_content = encrypt(content, key)
#
#     encrypted_filename = f"encrypted_{filename}"
#     with open(encrypted_filename, 'w') as encrypted_file:
#         encrypted_file.write(encrypted_content)
#
#     return encrypted_filename
#
# @encryption_logging
# def decrypt_file(filename, key):
#     with open(filename, 'r') as encrypted_file:
#         encrypted_content = encrypted_file.read()
#
#     decrypted_content = decrypt(encrypted_content, key)
#
#     decrypted_filename = f"decrypted_{filename}"
#     with open(decrypted_filename, 'w') as decrypted_file:
#         decrypted_file.write(decrypted_content)
#
#     return decrypted_filename
#
# def encrypt(content, key):
#     encrypted_content = ""
#     for char in content:
#         encrypted_char = chr(ord(char) + key)  # Простой сдвиг символов на ключ
#         encrypted_content += encrypted_char
#     return encrypted_content
#
# def decrypt(content, key):
#     decrypted_content = ""
#     for char in content:
#         decrypted_char = chr(ord(char) - key)  # Обратный сдвиг символов на ключ
#         decrypted_content += decrypted_char
#     return decrypted_content
#
#
# encrypted_file = encrypt_file("example.txt", "my_key")
# print(f"Encrypted file: {encrypted_file}")
#
# decrypted_file = decrypt_file(encrypted_file, "my_key")
# print(f"Decrypted file: {decrypted_file}")


# 3. Напишите функцию с именем analysis_file_sizes, которая принимает путь к каталогу
# в качестве входных данных. Функция должна рекурсивно обходить каталог и его подкаталоги и
# вычислять общий размер всех файлов, содержащихся в них. Результат должен быть возвращен в
# удобочитаемом формате, например, в килобайтах (КБ), мегабайтах (МБ) или гигабайтах (ГБ).
# Реализуйте эту функциональность с помощью модуля os в Python.

# import os
#
# def analysis_file_sizes(directory):
#     total_size = 0
#
#     # Рекурсивная функция для обхода каталога
#     def calculate_size(path):
#         nonlocal total_size
#
#         if os.path.isfile(path):
#             # Если путь указывает на файл, добавляем его размер к общему размеру
#             total_size += os.path.getsize(path)
#         elif os.path.isdir(path):
#             # Если путь указывает на каталог, рекурсивно обходим его содержимое
#             for item in os.listdir(path):
#                 item_path = os.path.join(path, item)
#                 calculate_size(item_path)
#
#     calculate_size(directory)
#
#     # Функция для преобразования размера в удобочитаемый формат
#     def format_size(size):
#         if size < 1024:
#             return f"{size} Б"
#         elif size < 1024**2:
#             return f"{size/1024:.2f} КБ"
#         elif size < 1024**3:
#             return f"{size/1024**2:.2f} МБ"
#         else:
#             return f"{size/1024**3:.2f} ГБ"
#
#     return format_size(total_size)


# directory_path = '/path/to/directory' # - требуется фактический адрес
# total_size = analysis_file_sizes(directory_path)
# print(f"Total size: {total_size}")