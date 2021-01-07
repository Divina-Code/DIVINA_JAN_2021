class Cat():
    ###КОНСТРУКТОР
    def __init__(self, name, age, colors, weight):
        self.name = name
        self.age = age
        self.colors = colors
        self.weight = weight
        favorite_food = 'meet'

    def sleep(self):
        print(self.name, "is sleeping....ZZZZZzzzzzz")

    def eat(self, food):
        self.weight += food

    def play(self):
        self.weight -= 0.01


bonya = Cat("Bonya", 3, ('black', 'white', 'ginger'), 4)
tom = Cat("Tom", 7, ("blue", 'red', 'gray'), 8)

print(bonya.weight + tom.weight)
bonya.sleep()
tom.sleep()

bonya.eat(0.015)
tom.eat(0.02)

print(bonya.weight)
print(tom.weight)

bonya.play()
tom.play()

print(bonya.weight)
print(tom.weight)
