import pygame
from  random import randint, choice
pygame.init()

gamedisplay = pygame.display.set_mode((800, 600) ) #Создаём экран размером 800 на 600


####COLORS
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

###FPS
time = pygame.time.Clock()
FPS = 60


##############CAR
green_car = pygame.image.load("img/yellow car.png")  #загружаем все картинки
red_car = pygame.image.load("img/red car.png")
yellow_car = pygame.image.load("img/green_car.jpg")

car_images = [ pygame.transform.scale(green_car, (200, 100)),
               pygame.transform.scale(red_car, (200, 100)),
               pygame.transform.scale(yellow_car, (200, 100))]


class Car():
    def __init__(self):
        self.image = choice(car_images)
        self.rect = self.image.get_rect(x = 0, y= randint(0, 400) )

    def move(self):
        self.rect.x+=randint(0, 1)



############################################
car1 = Car()
car2 = Car()
car3 = Car()


game = True  #Продолжается игра или нет
while game:
    time.tick(FPS) #Ограничение ФПС для цикла
    for e in pygame.event.get():   #берём события по одному
        if e.type == pygame.QUIT:
            game = False

    gamedisplay.fill(BLACK)
    gamedisplay.blit(car1.image, car1.rect)
    gamedisplay.blit(car2.image, car2.rect)
    gamedisplay.blit(car3.image, car3.rect)

    car1.move()
    car2.move()
    car3.move()

    pygame.display.update()
pygame.quit()
