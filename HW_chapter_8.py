# 1. Вызовите какую-нибудь другую функцию из модуля statistics
import statistics
nums = [56, 44, 32, 11, 5, 99, 125, 225]
print("Наивысшее среднее:", statistics.median_high(nums))
print("Самое малое среднее:", statistics.median_low(nums))
print("Среднее значение:", statistics.median(nums))

""" 2. Создайте модуль cubed, содержащий функцию, которая принимает в качестве параметра число, возводит это
число в куб и возвращает его. Импортируйте и вызовите функцию из другого модуля. """
import cubed
z = cubed.cub(4)
print(z)
