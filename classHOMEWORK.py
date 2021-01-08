"""
создать класс ВОИН
Характеристики:
--Здоровье (на старте 100)
--Имя(сообщается при создании персонажа)
--Урон(рандомный от 5 до 15)
--жив или нет (Если здоровье 0 или меньше, то умер)

Действия:
--Получить урон
--Покушать (увеличивает здоровте на некую величину)
--Прокачться (увеличение наносимого урона)
--Любая доп функция

"""

"""
по шаблогу создаются два воина
запускается цикл, который длится до тех пор, пока оба живы
воины по очереди бьют друг друга

рандомно могут им выпадать бонусы - покушать или прокачаться

"""
from random import randint as ri
from time import sleep

class Warrior():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = ri(5,15)
        self.isAlive = True


    def get_damage(self, damage):
        self.health-=damage

        if self.health<=0:
            self.health=0
            self.isAlive = False
        print(f"{self.name} получил урон {damage} и теперь его здоровье:{self.health}")


    def eat(self):
        self.health+=ri(20, 40)

        if self.health>100:
            self.health = 100

        print(f"{self.name} подкрепился и теперь его здоровье:{self.health}")

    def upgrade(self):
        self.damage+=ri(1, 3)
        print(f"{self.name} прокачался и теперь его урон:{self.damage}")

    def sleep(self):
        self.health+=50
        if self.health>100:
            self.health = 100




warrior1 = Warrior("Святозар")
warrior2 = Warrior("Ярополк")

while warrior1.isAlive and warrior2.isAlive:
    warrior1.get_damage(warrior2.damage)
    warrior2.get_damage(warrior1.damage)

    rand = ri(0, 12)
    if rand == 1:
        warrior1.eat()
    elif rand == 2:
        warrior2.eat()

    elif rand == 3:
        warrior1.upgrade()
    elif rand == 4:
        warrior2.upgrade()

    # elif rand == 5:
    #     warrior1.sleep()
    # elif rand == 6:
    #     warrior2.sleep()



    print("*"*30)
    sleep(1)

if warrior1.isAlive:
    print(f'{warrior1.name} WIN!')
elif warrior2.isAlive:
    print(f'{warrior2.name} WIN!')
else:
    print(f"It's a DRAW")
