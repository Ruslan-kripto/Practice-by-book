""" 1. Создайте классы Rectangle и Square с методом calculate_perimeter,вычисляющим периметр фигур,
которые эти классы представляют. Создайте объекты Rectangle и Square вызовите в них этот метод. """
class Rectangle():
    def __init__(self, w, l):
        self.weight = w
        self.len = l

    def calculate_perimeter(self):
        return self.weight * 2 + self.len * 2

class Square1():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(20, 30)
print("Периметр прямоугольника: {}".format(a_rectangle.calculate_perimeter()))
a_square = Square1(20)
print("Периметр квадрата: {}".format(a_square.calculate_perimeter()))
print("\n")

""" 2. В классе Square определите метод change_size, позволяющий передавать ему число, которое увеличивает или уменьшает
(если оно отрицательное) каждую сторону объекта Square на соответствующее значение. """
class Square2():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size

b_square = Square2(100)
print("Old size square: {}".format(b_square.s1))
b_square.change_size(200)
print("New size square: {}".format(b_square.s1))
print("\n")

""" 3. Создайте класс Shape. Определите в нем метод what_am_i, который при вызове выводит строку "Я — фигура.". 
Измените ваши классы Rectangle и Square из предыдущих заданий для наследования от Square, создайте объекты Square и
Rectangle и вызовите в них новый метод. """
class Shape():
    def what_am_i(self):
        print("Я - фигура.")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.weight = w
        self.len = l

    def calculate_perimeter(self):
        return self.weight * 2 + self.len * 2

class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

n_rectangle = Rectangle(20, 40)
n_rectangle.what_am_i()
n_square = Square(34)
n_square.what_am_i()
print("\n")

# 4. Создайте классы Horse и Rider. Используйте композицию, чтобы смоделировать лошадь с всадником на ней.
class Horse():
    def __init__(self, name):
        self.name = name

class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

r_horse = Horse("Svetozar")
the_rider = Rider("Ruslan", r_horse)
print("Лошадь Руслана: {}".format(the_rider.horse.name))
