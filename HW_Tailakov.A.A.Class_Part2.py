#Task 1
class Fraction:
    # counter = 0

    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        # Fraction.counter += 1

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @numerator.setter
    def numerator(self, value):
        self.__numerator = value

    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise ValueError('Атата !')
        self.__denominator = value

    def output_fraction(self):
        print(f"{self.numerator} / {self.denominator}")

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    @staticmethod
    def counter():
        print(f'counter = {Fraction.counter}')


fr1 = Fraction(10, 15)
fr2 = Fraction(15, 15)

result_addition = fr1.__add__(fr2)
result_subtraction = fr1.__sub__(fr2)
result_multiplication = fr1.__mul__(fr2)
result_division = fr1.__truediv__(fr2)

print("Addition:")
result_addition.output_fraction()
print()

print("Subtraction:")
result_subtraction.output_fraction()
print()

print("Multiplication:")
result_multiplication.output_fraction()
print()

print("Division:")
result_division.output_fraction()
print()

# #Task 2
# class TemperatureConverter:
#     count = 0
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         TemperatureConverter.count += 1
#         return (celsius * 9/5) + 32
#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         TemperatureConverter.count += 1
#         return (fahrenheit - 32) * 5/9
#     @staticmethod
#     def get_count():
#         return TemperatureConverter.count
# # Пример использования
#
# converter = TemperatureConverter()
# celsius_temp = 25
# fahrenheit_temp = converter.celsius_to_fahrenheit(celsius_temp)
# print(f"{celsius_temp} градусов Цельсия = {fahrenheit_temp} градусов Фаренгейта")
# fahrenheit_temp = 77
# celsius_temp = converter.fahrenheit_to_celsius(fahrenheit_temp)
# print(f"{fahrenheit_temp} градусов Фаренгейта = {celsius_temp} градусов Цельсия")
# count = converter.get_count()
# print(f"Количество конвертаций температуры: {count}")

#Task 3
# class Converter:
#     @staticmethod
#     def from_metric_to_english(length):
#         inch = length / 0.0254
#         foot = inch / 12
#         yard = foot / 3
#         mile = yard / 1760
#         return {
#             "inch": inch,
#             "foot": foot,
#             "yard": yard,
#             "mile": mile
#         }
#
#     @staticmethod
#     def from_english_to_metric(length):
#         meter = length * 0.3048
#         kilometer = meter / 1000
#         return {
#             "meter": meter,
#             "kilometer": kilometer
#         }
#
#
# # Пример использования
# print(Converter.from_metric_to_english(
#     1000))
# print(Converter.from_english_to_metric(1))