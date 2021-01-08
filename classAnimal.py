class Animal():
    ###КОНСТРУКТОР
    def __init__(self, name, age, colors, weight):
        self.name = name
        self.age = age
        self.colors = colors
        self.weight = weight
        self.favorite_food = 'meet'

    def sleep(self):
        print(self.name, "is sleeping....ZZZZZzzzzzz")

    def eat(self, food):
        self.weight += food

    def play(self):
        self.weight -= 0.01



class Cat(Animal):
    def __init__(self, name, age, colors, weight):
        Animal.__init__(self, name, age, colors, weight)

    def purr(self):
        print("Mrrrrrrrrrrrr")


class Tiger(Cat):
    def __init__(self, name, age, colors, weight):
        super().__init__(name, age, colors, weight)

    def sleep(self):
        print("Danger sleeping")


class Dog(Animal):
    def __init__(self, name, age, colors, weight):
        super().__init__(name, age, colors, weight)

    def tapki(self):
        print("Вот тапки")

class Giraff(Animal):
    def __init__(self, name, age, colors, weight):
        super().__init__(name, age, colors, weight)
        self.neck = 2





bonya = Cat("Bonya", 3, ('black', 'white', 'ginger'), 4)
bobik = Dog("Bobik", 7, ("blue", 'red', 'gray'), 8)
giraff = Giraff("Samson", 28, ('ginger', 'broun'), 700)
tiger = Tiger("Sherhan", 3, ('ginger', 'black'), 100)

bonya.sleep()
bobik.sleep()
giraff.sleep()
tiger.sleep()

bonya.purr()
print(giraff.neck)

