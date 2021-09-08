# 1. Создайте список ваших любимых музыкантов
my_list_of_favorite_musicians = ["Imagine Dragons", "System of a down", "Nickel Beck", "Lindsey Stirling"]
print("Список моих любимых исполнителей: ", my_list_of_favorite_musicians)

# 2. Создайте список кортежей, где каждый кортеж содержит долготу и широту
# любого места, в котором вы жили или которое посещали
my_list_of_places_Ive_been = []
usa_atlanta_sity = (33.7489924, -84.3902644)
russia_anapa_sity = (44.894272, 37.316887)
russia_moscow_sity = (55.7504461, 37.6174943)
russia_kazan_sity = (55.7823547, 49.1242266)
russia_kirov_sity = (58.6035257, 49.6639029)
my_list_of_places_Ive_been.append(usa_atlanta_sity)
my_list_of_places_Ive_been.append(russia_anapa_sity)
my_list_of_places_Ive_been.append(russia_moscow_sity)
my_list_of_places_Ive_been.append(russia_kazan_sity)
my_list_of_places_Ive_been.append(russia_kirov_sity)
print("\nКоординаты городов, в которых я побывал: ", my_list_of_places_Ive_been)

# 3. Создайте словарь, содержащий различные данные о вас: рост, любимый цвет, любимый актер и т.д.
my_dict = {"height": 184,
           "favorite color": "blue",
           "favorite actor": "Benedict Kemberbetch",
           "favorite football club": "Manchester Unaited"}
print("\ninfo to me", my_dict)

# 4 Напишите программу, которая запрашивает у пользователя его вес, любимый цвет или актер,
# и возвращает результат из словаря, созданного в предыдущем задании
y = input("\nenter you favorite color: ")
if y in my_dict["favorite color"]:
    color = my_dict["favorite color"]
    print(color)
else:
    print("Not found")

# 5 Создайте словарь, связывающий ваших любимых музыкантов со списком ваших любимых песен, написанных ими
my_favorite_songs = {"Imagine Dragons": "Gold, Beliver, Radioctive, Monster",
                     "System of a down": "Psuho, Lonley day, Get pilot",
                     "Nikel Beack": "Home",
                     "Lindsey Stirling": "Pheniks"}
print("\nmy favorite songs", my_favorite_songs)

# 6. Списки, кортежи и словари — лишь некоторые из встроенных в Python контейнеров. Самостоятельно изучите множества
# (тип контейнеров). В каком случае бы вы использовали множество?
z = set()
print("\n", z)

x = set("Hello")
print(x)

v = {"a", "b", "c", "d"}
print(v)

w = {i ** 2 for i in range(10)}  # генератор множеств
print(w)

words = ["hello", "daddy", "hello", "mum"]
print(set(words))

"""
Множество в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.
Чаще всего множества в Python используются для проверки на принадлежность, удаления повторов из последовательности
и выполнения математических операций, таких как пересечение, объединение, поиск разностей и симметрических разностей.
"""