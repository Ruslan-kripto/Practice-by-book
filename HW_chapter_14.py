""" 1. Добавьте переменную square_list в класс Square так, чтобы всякий раз,
когда вы создаете новый объект Square, он добавлялся в список. """
class Square1:
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self.s1)

    def print_size(self):
        print("s1 = {}".format(self.s1))

sq1 = Square1(4)
sq2 = Square1(16)
sq3 = Square1(43)
print(Square1.square_list)
print(sq3.print_size())

""" 2. Измените класс Square так, чтобы когда вы выводите объект Square, выводилось сообщение с длинами всех четырех
сторон фигуры. Например, если вы создадите квадрат при помощи Square(29) и осуществите вывод, Python должен вывести
строку 29 на 29 на 29 на 29. """
class Square2:
    def __init__(self, s1):
        self.s1 = s1

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

sq11 = Square2(77)
sq22 = Square2(55)
sq33 = Square2(33)
print(sq33)

""" 3. Напишите функцию, которая принимает два объекта в качестве параметров и возвращает True, если они являются
одним и тем же объектом, и False в противном случае. """
def proverka(x, y):
    return x is y
print(proverka("a", "a"))
