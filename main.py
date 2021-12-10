from abc import ABC


def move():
    print('moving')


def block():
    print('blocked the hit')


class Robots(ABC):
    # Абстрактный класс Robots

    def attack(self):
        print(f'{self.__class__.__name__} attack enemy ')

    def kill(self):
        print(f'{self.__class__.__name__} kill enemy ')

    def charged(self):
        print('charge at the station')

    def death(self):
        print(f'{self.__class__.__name__} dead')


def waving():
    print('hand waving')


class Gareth(Robots):
    def __init__(self, mood, intellect, friendliness):
        self.mood = mood
        self.intellect = intellect
        self.friendliness = friendliness
        self.name = 'Gareth'

    def die(self):
        print('dead by laser')

    def punch(self):
        print(f'{self.__class__.__name__} Hit enemy')

    def fly(self):
        print(f'fly and avoid hit')

    def backflip(self):
        print(f'{self.__class__.__name__} do a backflip')


class Bob(Robots):
    def __init__(self, endurance, forces, name):
        self.endurance = endurance
        self.forces = forces
        self.name = name

    def dance(self):
        print(f'{self.__class__.__name__} a danced')

    def laser(self):
        print('produces a laser')

    def cool_the_laser(self):
        print('cools the laser')

    def sets_fire_to_laser(self):
        print('sets fire to laser')

    def murder(Gareth):
        print(f'{Bob} kill with name {Gareth}')


class Moji(Robots):
    def __init__(self, name, appliances, sadness):
        self.name = name
        self.appliances = appliances
        self.sadness = sadness

    def wrench(self):
        print('tightening the bolts')

    def tightening_the_bolts(self):
        print('tightens screws')

    def electroscope(self):
        print('checks charge')

    def fix(self):
        print(f'{self.__class__.__name__} fix Bob')

    def shout(self):
        print('lets fix you')

    def heal(self):
        print(f'participant 3 with name {self.name} heal participant 1 with name Bob')


class Gigant(Robots):
    def __init__(self, armor, rage):
        self.name = 'Loki'
        self.armor = armor
        self.rage = rage

    def ram(self):
        print('runs to ram')

    def picks_up_a_stone(self):
        print(f'{self.__class__.__name__} get stone')

    def throws_a_three(self):
        print('throw three')

    def shout(self):
        print('Im a giant!')

    def murder(self):
        print(f'participant 4 with name {self.name} kill participant 3 with name {Moji.name}')


bob = Bob(80, 100, 'Bob')
Moji = Moji('Moji', 60, 70)
Gigant = Gigant(90, 90)
Gareth = Gareth(70, 100, 'Gareth')


print('fight!')

bob.dance()
Gareth.backflip()
bob.attack()
Moji.fix()
Gigant.death()

