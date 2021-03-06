# Игра - Висилица
# Компьютер выбирает случайное слово из списка, игрок долже отгодать за 7 попыток

import random

def hangman():
    """ В данной функции находится игра. """
    game_words = ["кот", "автомобиль", "тетрадь", "телефон", "стул", "стол", "салфетка", "солнце", "браузер"]
    word = random.choice(game_words)
    wrong = 0  # кол-во ошибок
    stages = ["",  # рисунок, который появляется по мере выявления ошибки в букве
             "________        ",
             "|        |      ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)  # список в котором храниться слово ["к", "о", "т"]
    board = ["__"] * len(word)  # заменяет элементы списка слова на символ _
    win = False  # Следит за тем, выиграл ли игрок или нет
    print("Добро пожаловать на казнь!")  # приветствие

    while wrong < len(stages) - 1:  # до тех пор пока кол-во ошибок меньше чем кол-во строк в рисунке виселецы
        print("\n")
        msg = "Введите букву: "
        char = input(msg)  # запрашиваем букву у игрока

        if char in rletters:  # проверяем, есть ли данная буква в слове
            cind = rletters.index(char)
            board[cind] = char  # обновить изображение слова на экране
            rletters[cind] = '@'  # заменяем повторную букву на этот символ, чтобы в следующий раз найти второе вхождение

        else:  # если буквы нет в слове, прибавить к ошибке 1
            wrong += 1

        print((" ".join(board)))  # вывести доску с отгадываемыми буквами на экран
        e = wrong + 1  # делает срез для текущей версии висельника
        print("\n".join(stages[0: e]))  # вывод текушего изображения висилицы

        if "__" not in board:  # если нет пустых символов, значит игрок победил
            print("Вы выиграли! Было загаданно слово: ")
            print(" ".join(board))  # вывести доску с отгаданным словом
            win = True  # победа = правда
            break  # остановить цикл

    if not win:
        print("\n".join(stages[0: wrong]))
        print("Вы проиграли! Было загаданно слово: {}.".format(word))

hangman()
