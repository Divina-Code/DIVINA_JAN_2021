import pygame
from  random import randint, choice
pygame.init()

gamedisplay = pygame.display.set_mode((800, 600) ) #Создаём экран размером 800 на 600



##############CAR
car_image = pygame.image.load("img/yellow car.png")
car_image = pygame.transform.scale(car_image, (200, 100))

class Car():
    def __init__(self):
        self.image = car_image

        self.rect = self.image.get_rect(x = 0, y= randint(0, 400) )




############################################
car1 = Car()
car2 = Car()
car3 = Car()


game = True  #Продолжается игра или нет
while game:

    for e in pygame.event.get():   #берём события по одному
        if e.type == pygame.QUIT:
            game = False

    gamedisplay.blit(car1.image, car1.rect)
    gamedisplay.blit(car2.image, car2.rect)
    gamedisplay.blit(car3.image, car3.rect)

    pygame.display.update()
pygame.quit()
