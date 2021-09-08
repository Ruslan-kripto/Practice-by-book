def f():
    """ Возвращает а в квадрате
    :параметр а: целое число
    :return: целочисленное а в квадрате
    """
    try:
        a = int(input("Enter the number: "))
        print(a ** 2)
    except ValueError:
        print("Error")
f()

def x():
    """ Преобразовывает вводные данные в строку
    :параметр а: string
    """
    a = str(input("Enter the string: "))
    print(a)
x()

def y(a, b, c, d = 4, f = 5):
    """ возвращает сумму всех обязательных параметров с двумя необязательными параметрами
    :param a: integer
    :param b: integer
    :param c: integer
    :param d: integer 4
    :param f: integer 5
    :return: integer
    """
    try:
        total = a + b + c + d + f
        print(total)
    except ValueError:
        print("Parameters is only an integer")
y(1, 2, 3)

def v():
    """ делит целое число на 2, после чего результат присваевается параметру второй функци z(), которая умножает его на 4
    :param x: целое число
    :return: число х деленое на 2
    """
    try:
        x = int(input("Введите целое число: "))
        return x / 2
    except ValueError:
        print("Error, x is not integer.")


def z():
    """ принимает результат функции v() и умножает его на 4
    :return: v() * 4
    """
    return s * 4
s = v()
#print(s)
n = z()
print(n)

def w():
    """ преобразовывает string в float
    :парамерт i: строка
    :return: строка преобразованная в float
    """
    try:
        i = float(input("Введите число: "))
        return i
    except ValueError:
        print("Error")

result = w()
print(result)
