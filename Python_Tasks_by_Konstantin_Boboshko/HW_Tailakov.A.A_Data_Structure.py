#Task 1
def print_menu():
    print("1. Добавить новое число в список")
    print("2. Удалить все вхождения числа из списка")
    print("3. Показать содержимое списка")
    print("4. Проверить есть ли значение в списке")
    print("5. Заменить значение в списке")
    print("0. Выход")


def input_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print('Ошибка. Неверный формат числа. Попробуйте снова.')


def has_number(numbers, num):
    for n in numbers:
        if n == num:
            return True
    return False


def add_number(numbers):
    num = input_int("Введите число: ")
    if has_number(numbers, num):
        print(f"Число {num} уже есть в списке.")
    else:
        numbers.append(num)
        print(f"Число {num} было добавлено в список.")


def remove_number(numbers):
    num = input_int("Введите число для удаления: ")
    count = 0
    new_list = []
    for n in numbers:
        if n == num:
            count += 1
        else:
            new_list.append(n)
    if count > 0:
        numbers = new_list
        print(f"Число {num} было удалено из списка {count} раз.")
    else:
        print(f"Число {num} не найдено в списке.")


def print_list(numbers):
    direction = input("1. С начала\n2. С конца\n")
    if direction == '2':
        numbers.reverse()
    for n in numbers:
        print(n)


def check_number(numbers):
    num = input_int("Введите число для проверки: ")
    if has_number(numbers, num):
        print(f"Число {num} найдено в списке.")
    else:
        print(f"Число {num} не найдено в списке.")


def replace_number(numbers):
    old_val = input_int("Введите значение, которое нужно заменить: ")
    new_val = input_int("Введите новое значение: ")
    mode = input("1. Заменить первое вхождение\n2. Заменить все вхождения\n")
    found = False
    for i in range(len(numbers)):
        if numbers[i] == old_val:
            if mode == '1':
                found = True
                numbers[i] = new_val
                print(f"Значение {old_val} было заменено на {new_val} в списке.")
                break
            elif mode == '2':
                found = True
                numbers[i] = new_val
    if not found:
        print(f"Значение {old_val} не найдено в списке.")


def main():
    numbers = []
    while True:
        print()
        print_menu()
        choice = input_int("Выберите пункт меню: ")
        if choice == 1:
            add_number(numbers)
        elif choice == 2:
            remove_number(numbers)
        elif choice == 3:
            print_list(numbers)
        elif choice == 4:
            check_number(numbers)
        elif choice == 5:
            replace_number(numbers)
        elif choice == 0:
            print("До свидания!")
            break
        else:
            print("Ошибка. Неверный пункт меню. Попробуйте снова.")


if __name__ == '__main__':
    main()


#Task2
# class StringStack:
#     def __init__(self, size):
#         self.stack = [''] * size
#         self.top = -1
#
#     def push(self, string):
#         if self.top == len(self.stack) - 1:
#             return False
#         else:
#             self.top += 1
#             self.stack[self.top] = string
#             return True
#
#     def pop(self):
#         if self.top == -1:
#             return None
#         else:
#             string = self.stack[self.top]
#             self.top -= 1
#             return string
#
#     def count(self):
#         return self.top + 1
#
#     def is_empty(self):
#         return self.top == -1
#
#     def is_full(self):
#         return self.top == len(self.stack) - 1
#
#     def clear(self):
#         self.top = -1
#
#     def peek(self):
#         if self.top == -1:
#             return None
#         else:
#            return self.stack[self.top]
#
#
#
# stack = StringStack(5)
#
# while True:
#     print("Menu:")
#     print("1. Push a string")
#     print("2. Pop a string")
#     print("3. Count strings in stack")
#     print("4. Check if stack is empty")
#     print("5. Check if stack is full")
#     print("6. Clear stack")
#     print("7. Peek at top of stack")
#     print("0. Exit")
#     choice = input("Enter your choice: ")
#
#     if choice == "1":
#         string = input("Enter a string to push onto the stack: ")
#         if stack.push(string):
#             print("String pushed onto stack.")
#         else:
#             print("Stack is full, string not pushed.")
#     elif choice == "2":
#         string = stack.pop()
#         if string is not None:
#             print("Popped string:", string)
#         else:
#             print("Stack is empty.")
#     elif choice == "3":
#         count = stack.count()
#         if count == 1:
#             print("There is 1 string in the stack.")
#         else:
#             print("There are", count, "strings in the stack.")
#     elif choice == "4":
#         if stack.is_empty():
#             print("Stack is empty.")
#         else:
#             print("Stack is not empty.")
#     elif choice == "5":
#         if stack.is_full():
#             print("Stack is full.")
#         else:
#             print("Stack is not full.")
#     elif choice == "6":
#         stack.clear()
#         print("Stack cleared.")
#     elif choice == "7":
#         string = stack.peek()
#         if string is not None:
#             print("Top string on stack:", string)
#         else:
#             print("Stack is empty.")
#     elif choice == "0":
#         print("Exiting program.")
#         break
#     else:
#         print("Invalid choice, please try again.")


#Use example
#
# print(stack.push("first"))
# print(stack.push("second"))
# print(stack.count())
# print(stack.is_empty())
# print(stack.is_full())
# print(stack.push("third"))
# print(stack.push("fourth"))
# print(stack.push("fifth"))
# print(stack.push("sixth"))
# print(stack.pop())
# print(stack.count())
# print(stack.is_empty())
# print(stack.is_full())
# print(stack.peek())
# stack.clear()
# print(stack.count())

#Task 3
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         if self.is_empty():
#             raise IndexError("pop from an empty stack")
#         return self.items.pop()
#
#     def peek(self):
#         if self.is_empty():
#             raise IndexError("peek from an empty stack")
#         return self.items[-1]
#
#     def size(self):
#         return len(self.items)
#
#     def clear(self):
#         self.top = -1
#
# s = Stack()
# s.push("hi")
# s.push("that")
# s.push("go")
# s.clear()
#
# print(s.peek())
# print(s.size())