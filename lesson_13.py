""" ООП - Объектно ориентированное программирование """
""" Наследование """

class Game:
    def __init__(self, game_name, relize, size, category):
        self.game_name = game_name
        self.relize = relize
        self.size = size
        self.category = category
        
    def info(self):
        return f'Название игры - {self.game_name} - {self.relize} - {self.size} - {self.category}'
    
# game = Game("CsGo2", "2016", "50GB", "shooter")
# print(game.info())

class Roblox(Game):
    def __init__(self, game_name, relize, size, category, multiplayer):
        # super().__init__(game_name, relize, size, category)
        Game.__init__(self, game_name, relize, size, category)
        self.multiplayer = multiplayer
        self.name = 'player'
        self.gender = 'man'
        self.skin = 'VIP'
        self.hp = 100        
        
    def info(self):
        return f'Название игры - {self.game_name} - {self.relize} - {self.size} - {self.category} - {self.multiplayer}'
    
    def info_player(self):
        print(f"Игрок - {self.name}, Пол - {self.gender}, Облик - {self.skin}, Здоровье - {self.hp}")
    
    def edit_player(self):
        name = input("Введите имя игрока: ")
        gender = input("Введите пол игрока: ")
        skin = input("Введите облик: ")
        self.name = name
        self.gender = gender
        self.skin = skin

# roblox = Roblox("Strike", "2015", '2GB', "shooter", "Yes")
# print(roblox.info())
# roblox.edit_player()
# roblox.info_player()

class Strike(Roblox):
    def __init__(self, game_name, relize, size, category):
        super().__init__(game_name, relize, size, category)
        
strike = Strike("strike", 2016, "4GB", "any", "yes")
print(strike.info())


''''Задание: Симуляция Зоопарка с Конструкторами
Создайте классы, которые будут моделировать разных животных в зоопарке, используя множественное наследование и конструкторы для инициализации объектов.

Базовые классы:

Создайте класс Animal, который будет представлять общее животное. У этого класса должен быть конструктор __init__(), который принимает параметр name для имени животного. Также добавьте методы eat() и sleep(), которые выводят сообщения, например, "{name} ест" и "{name} спит".

Создайте класс Walker, который будет представлять животных, которые могут ходить. У этого класса должен быть метод walk(), который выводит сообщение "{name} ходит".

Создайте класс Swimmer, который будет представлять животных, которые могут плавать. У этого класса должен быть метод swim(), который выводит сообщение "{name} плавает".

Создайте класс Flyer, который будет представлять животных, которые могут летать. У этого класса должен быть метод fly(), который выводит сообщение "{name} летает".

Комбинированные классы:
                                            
Создайте класс Penguin, который наследуется от Animal, Walker, и Swimmer. Реализуйте конструктор, который принимает параметр name и вызывает конструктор класса Animal. Добавьте метод describe(), который выводит сообщение о том, что пингвин может ходить и плавать.

Создайте класс Duck, который наследуется от Animal, Walker, Swimmer, и Flyer. Реализуйте конструктор, который принимает параметр name и вызывает конструктор класса Animal. Добавьте метод describe(), который выводит сообщение о том, что утка может ходить, плавать и летать.

Создайте класс Bat, который наследуется от Animal и Flyer. Реализуйте конструктор, который принимает параметр name и вызывает конструктор класса Animal. Добавьте метод describe(), который выводит сообщение о том, что летучая мышь может летать.

Тестирование:

Создайте экземпляры каждого из созданных вами классов, передавая им имена, и вызовите для них методы describe(), а также методы, относящиеся к их поведению (например, walk(), swim(), fly()).'''
