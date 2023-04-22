#Task1
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def __eq__(self, other):
#         return self.radius == other.radius
#
#     def __lt__(self, other):
#         return self.radius < other.radius
#
#     def __le__(self, other):
#         return self.radius <= other.radius
#
#     def __gt__(self, other):
#         return self.radius > other.radius
#
#     def __ge__(self, other):
#         return self.radius >= other.radius
#
#     def __add__(self, other):
#         return Circle(self.radius + other)
#
#     def __sub__(self, other):
#         return Circle(self.radius - other)
#
#     def __iadd__(self, other):
#         self.radius += other
#         return self
#
#     def __isub__(self, other):
#         self.radius -= other
#         return self
#
#
#
# # Создаем две окружности
# circle1 = Circle(5)
# circle2 = Circle(10)
#
# # Проверяем равенство и сравниваем радиусы двух окружностей
# if circle1 == circle2:
#     print("Radiuses are equal")
#
# if circle2 > circle1:
#     print("Second circle has larger radius")
# else:
#     print("First circle has larger radius")
#
# # Пропорциональное изменение радиусов окружностей
# circle1 += 3
# circle2 -= 2
# print(circle1.radius)
# print(circle2.radius)

#Task2
# class Complex:
#   def __init__(self, real=0.0, imag=0.0):
#     self.real = real
#     self.imag = imag
#
#   def __add__(self, other):
#     return Complex(self.real + other.real, self.imag + other.imag)
#
#   def __sub__(self, other):
#     return Complex(self.real - other.real, self.imag - other.imag)
#
#   def __mul__(self, other):
#     return Complex(self.real * other.real - self.imag * other.imag,
#                    self.imag * other.real + self.real * other.imag)
#
#   def __truediv__(self, other):
#     denominator = other.real ** 2 + other.imag ** 2
#     real_numerator = self.real * other.real + self.imag * other.imag
#     imag_numerator = self.imag * other.real - self.real * other.imag
#     return Complex(real_numerator / denominator, imag_numerator / denominator)
#
#
# # Создаем два комплексных числа
# a = Complex(1, 2)
# b = Complex(3, 4)
#
# # Применяем операции сложения, вычитания, умножения и деления
# c = a + b
# d = a - b
# e = a * b
# f = a / b
#
# # Выводим результаты
# print(c.real, "+", str(c.imag) + "i")
# print(d.real, "+", str(d.imag) + "i")
# print(e.real, "+", str(e.imag) + "i")
# print(f.real, "+", str(f.imag) + "i")

#Task3
# class Airplane:
#   def __init__(self, model, max_passengers):
#     self.model = model
#     self.max_passengers = max_passengers
#     self.current_passengers = 0
#
#   def __eq__(self, other):
#     return self.model == other.model
#
#   def __add__(self, other):
#     self.current_passengers += other
#     return self
#
#   def __sub__(self, other):
#     self.current_passengers -= other
#     return self
#
#   def __iadd__(self, other):
#     self.current_passengers += other
#     return self
#
#   def __isub__(self, other):
#     self.current_passengers -= other
#     return self
#
#   def __lt__(self, other):
#     return self.max_passengers < other.max_passengers
#
#   def __le__(self, other):
#     return self.max_passengers <= other.max_passengers
#
#   def __gt__(self, other):
#     return self.max_passengers > other.max_passengers
#
#   def __ge__(self, other):
#     return self.max_passengers >= other.max_passengers
#
#
#
# # Создаем два самолета
# airplane1 = Airplane("Boeing 747", 416)
# airplane2 = Airplane("Airbus A380", 853)
#
# # Проверяем равенство типов двух самолетов
# if airplane1 == airplane2:
#   print("Airplane models are equal")
# else:
#   print("Airplane models are not equal")
#
# # Увеличиваем/уменьшаем количество пассажиров в первом самолете
# airplane1 += 100
# airplane1 -= 50
#
# # Сравниваем максимальную вместимость двух самолетов
# if airplane1 > airplane2:
#   print("First airplane has larger max_passengers")
# else:
#   print("Second airplane has larger max_passengers")

#Task 4
# class Flat:
#   def __init__(self, area, price):
#     self.area = area
#     self.price = price
#
#   def __eq__(self, other):
#     return self.area == other.area
#
#   def __ne__(self, other):
#     return self.area != other.area
#
#   def __lt__(self, other):
#     return self.price < other.price
#
#   def __le__(self, other):
#     return self.price <= other.price
#
#   def __gt__(self, other):
#     return self.price > other.price
#
#   def __ge__(self, other):
#     return self.price >= other.price
#
#
#
# # Создаем две квартиры
# flat1 = Flat(50, 100000)
# flat2 = Flat(70, 130000)
#
# # Проверяем равенство и неравенство площадей двух квартир
# if flat1 == flat2:
#   print("Flats have equal area")
# else:
#   print("Flats have different area")
#
# if flat1 != flat2:
#   print("Flats have different area")
# else:
#   print("Flats have equal area")
#
# # Сравниваем цены двух квартир
# if flat1 > flat2:
#   print("First flat is more expensive")
# else:
#   print("Second flat is more expensive")


