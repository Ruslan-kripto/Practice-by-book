# 1. Найдите у себя на компьютере файл и выведите его содержимое с помощью Python.
import os
r = os.path.join("C:\\", "Users", "Aser", "Ruslan", "M_Dowsen", "lesson7", "test.txt")
print(r)

with open("C:\\Users\\Aser\\Ruslan\\M_Dowsen\\lesson7\\test.txt", "r") as ee:
    print(ee.read())

with open("test2.txt", "r") as s:
    print(s.read())

# 2. Напишите программу, которая задает пользователю вопрос и сохраняет ответ в файл.
answer = input("Hello! What is your name?: ")
with open("test4.txt", "w") as w:
    w.write(answer)


""" 3. Примите элементы в списке списков [["Звездные войны", "Терминатор", "Искусственный интеллект"],
["Дурак", "Матильда", "Левиафан"], ["Люди в черном", "Я - робот", "Эволюция"]] и запишите их в CSV-файл. 
Данные каждого списка должны быть строкой в файле, при этом каждый элемент списка должен быть отделен запятой. """
import csv
lists = [["Звездные войны", "Терминатор", "Искусственный интеллект"],
         ["Дурак", "Матильда", "Левиафан"],
         ["Люди в черном", "Я - робот", "Эволюция"]]

with open("movies2.csv", "w") as f:
    n = csv.writer(f, delimiter=",")
    for movie in lists:
        n.writerow(movie)
