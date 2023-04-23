
#Task 1
# class Figure:
#     def calculate_area(self):
#         pass  # Абстрактный метод
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
#
# class Circle(Figure):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return 3.14 * self.radius ** 2
#
#
# class RightTriangle(Figure):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def calculate_area(self):
#         return 0.5 * self.base * self.height
#
#
# class Trapezoid(Figure):
#     def __init__(self, a, b, height):
#         self.a = a
#         self.b = b
#         self.height = height
#
#     def calculate_area(self):
#         return (self.a + self.b) * self.height / 2
#
#
# rectangle = Rectangle(5, 7)
# circle = Circle(4)
# triangle = RightTriangle(6, 3)
# trapezoid = Trapezoid(2, 6, 4)
#
# print("Rectangle area:", rectangle.calculate_area())
# print("Circle area:", circle.calculate_area())
# print("Triangle area:", triangle.calculate_area())
# print("Trapezoid area:", trapezoid.calculate_area())


#Task 2
# class Figure:
#     def calculate_area(self):
#         pass  # Абстрактный метод
#
#     def __str__(self):
#         return "Figure"
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
#     def __int__(self):
#         return self.calculate_area()
#
#     def __str__(self):
#         return f"Rectangle ({self.width} x {self.height}), area: {self.calculate_area()}"
#
#
# class Circle(Figure):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return 3.14 * self.radius ** 2
#
#     def __int__(self):
#         return int(self.calculate_area())
#
#     def __str__(self):
#         return f"Circle (r = {self.radius}), area: {self.calculate_area()}"
#
#
# class RightTriangle(Figure):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def calculate_area(self):
#         return 0.5 * self.base * self.height
#
#     def __int__(self):
#         return int(self.calculate_area())
#
#     def __str__(self):
#         return f"Right Triangle ({self.base} x {self.height}), area: {self.calculate_area()}"
#
#
# class Trapezoid(Figure):
#     def __init__(self, a, b, height):
#         self.a = a
#         self.b = b
#         self.height = height
#
#     def calculate_area(self):
#         return (self.a + self.b) * self.height / 2
#
#     def __int__(self):
#         return int(self.calculate_area())
#
#     def __str__(self):
#         return f"Trapezoid ({self.a}, {self.b}, {self.height}), area: {self.calculate_area()}"
#
# rectangle = Rectangle(5, 7)
# circle = Circle(4)
# triangle = RightTriangle(6, 3)
# trapezoid = Trapezoid(2, 6, 5)
#
# print("Rectangle area:", rectangle.calculate_area())
# print("Circle area:", circle.calculate_area())
# print("Triangle area:", triangle.calculate_area())
# print("Trapezoid area:", trapezoid.calculate_area())
#
# # Используем функции int и str для получения площади и информации о фигуре
# print("Rectangle area (int):", int(rectangle))
# print("Circle area (int):", int(circle))
# print("Triangle area (int):", int(triangle))
# print("Trapezoid area (int):", int(trapezoid))
#
# print(str(rectangle))
# print(str(circle))
# print(str(triangle))
# print(str(trapezoid))

#Task3


import json


class Shape:
    def Show(self):
        pass  # Абстрактный метод

    def Save(self, filename):
        with open(filename, 'a') as file:
            file.write(json.dumps(self.__dict__) + '\n')

    @staticmethod
    def Load(filename):
        with open(filename) as file:
            lines = file.readlines()
            objects = []
            for line in lines:
                data = json.loads(line)
                objects.append(Shape.CreateObject(data))
            return objects

    @staticmethod
    def CreateObject(data):
        shape_type = data.pop('type')
        if shape_type == 'Square':
            return Square(**data)
        elif shape_type == 'Rectangle':
            return Rectangle(**data)
        elif shape_type == 'Circle':
            return Circle(**data)
        elif shape_type == 'Ellipse':
            return Ellipse(**data)
        raise ValueError(f'Unknown shape type: {shape_type}')


class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side
        self.type = 'Square'

    def Show(self):
        print(f"Square ({self.x}, {self.y}), side {self.side}")


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = 'Rectangle'

    def Show(self):
        print(f"Rectangle ({self.x}, {self.y}), width {self.width}, height {self.height}")


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.type = 'Circle'

    def Show(self):
        print(f"Circle ({self.x}, {self.y}), radius {self.radius}")


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = 'Ellipse'

    def Show(self):
        print(f"Ellipse ({self.x}, {self.y}), width {self.width}, height {self.height}")

shapes = [
    Square(0, 0, 5),
    Rectangle(11, 11, 8, 6),
    Circle(5, 5, 3),
    Ellipse(20, 20, 10, 6)
]

for shape in shapes:
    shape.Show()
    shape.Save("shapes.txt")

new_shapes = Shape.Load("shapes.txt")

for shape in new_shapes:
    shape.Show()