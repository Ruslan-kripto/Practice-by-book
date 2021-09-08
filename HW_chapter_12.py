# 1. Определите класс Apple с четырьмя переменными экземпляра, представляющими четыре свойства яблока.
class Apple:
    def __init__(self, w, c, s, t):
        self.weight = w
        self.color = c
        self.size = s
        self.taste = t
        print("Создано яблоко!")

w_apple = Apple(55, "red", 12, "sweet")
print(w_apple)
print(w_apple.weight)
print(w_apple.color)
print(w_apple.size)
print(w_apple.taste)
print("\n")
""" 2. Создайте класс Circle с методом area, подсчитывающим и возвращающим площадь круга. Затем создайте объект Circle,
вызовите в нем метод area и выведите результат. Воспользуйтесь функцией pi из встроенного в Python модуля math. """
import math
class Circle:
    def __init__(self, r):
        self.radius = r
        print("Создан круг!")

    def area(self):
        return self.radius ** 2 * math.pi

w_circle = Circle(5)
print(w_circle.area())
print("\n")
""" 3. Создайте класс Triangle с методом area, подсчитывающим и возвращающим площадь треугольника. Затем создайте
объект Triangle, вызовите в нем area и выведите результат. """
class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h
        print("Создан треугольник!")

    def area(self):
        return self.height * self.base / 2

w_triangle = Triangle(5, 7)
print(w_triangle)
print(w_triangle.area())
print("\n")
""" 4. Создайте класс Hexagon с методом calculate_perimeter, подсчитывающим и возвращающим периметр шестиугольника.
Затем создайте объект Hexagon, вызовите в нем calculate_perimeter и выведите результат. """
class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6
        print("Создан шестиугольник!")

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6

w_haxagon = Hexagon(5, 6, 4, 5, 6, 4)
print(w_haxagon)
print(w_haxagon.calculate_perimeter())
