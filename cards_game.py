class Card:  # класс - карта.
    suits = ["пикей", "червей", "бубей", "треф"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "валету", "даму", "короля", "туза"]

    def __init__(self, v, s):  # инициализируем объект-карту (значение и масть)
        """suit and value - целые числа"""
        self.value = v  # значение карты
        self.suit = s  # масть карты

    def __lt__(self, c2):  # определяем магический метод для того, чтобы сравнить 2 карты
        if self.value < c2.value:  # если значение одной карты менньше чем другой
            return True  # вернуть истина
        if self.value == c2.value:  # если значение 2 карт одинково
            if self.suit < c2.suit:  # то сравнить их по масти
                return True
            else:
                return False
        return False

    def __gt__(self, c2):  # определяем магическй метод для того, чтобы сравнить 2 карты
        if self.value > c2.value: # если значение одной карты менньше чем другой
            return True  # вернуть истина
        if self.value == c2.value:  # если значение 2 карт одинково
            if self.suit > c2.value:  # то сравнить их по масти
                return True
            else:
                return False
        return False

    def __repr__(self):  # переопределяем магический метод, для того чтобы вывести объект-карту на экран
        v = self.values[self.value] + " of " + self.suits[self.suit]  # (например, в виде 2 червей)
        return v

#card1 = Card(10, 1)
#card2 = Card(10, 4)
#print(card1 < card2)
#>>> True

#card3 = Card(3, 2)
#print(card3)
#>>> 3 of бубей

from random import shuffle  # импортируем функцию shuffle из модуля random

class Deck:  # создаем игральную колоду
    def __init__(self):
        self.cards = []  # список для карт-объектов
        for i in range(2, 15):  # запускаем двойной цикл, каждое значение проходит через все масти,
            for j in range(4):  # а потом другое значение и другое, всего 52 карты-объекта
                self.cards.append(Card(i, j))  # внести карты-объекты в пустой список
        shuffle(self.cards)  # перемешать все карты-объекты

    def rm_card(self):  # изымает и возвращает карту из списка cards, или возвращает None, если список пуст
        if len(self.cards) == 0:
            return
        return self.cards.pop()

#deck1 = Deck()
#for card in deck1.cards:
#    print(card)
#>>> выводит на экран все 52 карты

class Player:  # инициализация объекта - игрока
    def __init__(self, name):
        self.wins = 0  # кол-во выигранных раундов
        self.card = None  # карта игрока, кторую он держит в момент раунда
        self.name = name  # имя игрока

class Game:  # сама игра
    def __init__(self):
        name1 = input("name player 1: ")  # имя 1 игрока
        name2 = input("name player 2: ")  # имя 2 игрока
        self.deck = Deck()  # создание колоды и ее сохранение в переменной экземпляра класса
        self.p1 = Player(name1)  # создание 1 игрока
        self.p2 = Player(name2)  # создание 2 игрока

    def wins(self, winner):  # метод, который выводит на экран имя победителя раунда
        w = "{} забирает карты"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):  # игровой стол, игроки тянут и показывают карты
        d = "{} кладет {}, а {} кладет {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):  # метод, запускающий игру
        cards = self.deck.cards  # 52 карты
        print("Let's go!")
        while len(cards) >= 2:  # до тех пор пока игрок не нажмет на Х или в колоде останется меньше 2 карт
            m = "Нажмите Х для выхода. Нажмите любую другую клавишу для начала игры."
            response = input(m)  # запрс на подтверждение игрока о готовности игры
            if response == "x":  # если игрок нажал Х, то игра прекращается
                break
            p1c = self.deck.rm_card()  # первый игрок берет карту
            p2c = self.deck.rm_card()  # второй игрок берет карту
            p1n = self.p1.name  # имя первого игрока
            p2n = self.p2.name  # имя второго игрока
            self.draw(p1n, p1c, p2n, p2c)  # вывод на экран действий за столом
            if p1c > p2c:  # если карта первого игрока больше чем у второго
                self.p1.wins += 1  # прибавить к победам первого игрока 1
                self.wins(self.p1.name)  # вывод на экран победителя раунда
            else:  # если наоборот
                self.p2.wins += 1  # прибавить к победам второго игрока 1
                self.wins(self.p2.name)  # вывод на экран победителя раунда

        win = self.winner(self.p1, self.p2)  # передаем в переменную колическво побед в раундах каждого игрока

        print("Игра окончена. {} выиграл!".format(win))

    def winner(self, p1, p2):  # определяем победителя
        if p1.wins > p2.wins:  # если кол-во побед 1 игрока больше чем у 2 игрока
            return p1.name  # вернуть имя 1 игрока
        if p1.wins < p2.wins:  # если кол-во побед 2 игрока больше чем у 1 игрока
            return p2.name  # вернуть имя 2 игрока
        return "Ничья!"  # если у обоих игроков одинаковое количесво выигранныхраундов, то объявить ничью

game = Game()  # инициализировать объект ИГРА
game.play_game()  # запустить игру
