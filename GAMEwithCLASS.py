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


###TEXT
myFont = pygame.font.SysFont('Ink Free', 80)  #В скобочках название и размер шрифта
myTextIMG = myFont.render("FINISH", True, RED) #получаем картинку с нужным текстом

##############CAR
green_car = pygame.image.load("img/yellow car.png")  #загружаем все картинки
red_car = pygame.image.load("img/red car.png")
yellow_car = pygame.image.load("img/green_car.jpg")

car_images = [ pygame.transform.scale(green_car, (200, 100)),
               pygame.transform.scale(red_car, (200, 100)),
               pygame.transform.scale(yellow_car, (200, 100))]

finish = False
class Car(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = choice(car_images)
        self.rect = self.image.get_rect(x = 0, y= randint(0, 400) )

    def update(self):
        global finish
        self.rect.x+=randint(0, 4)
        if self.rect.right >= 800:
            finish = True


############################################
cars = pygame.sprite.Group()
car1 = Car(cars)
car2 = Car(cars)
car3 = Car(cars)


game = True  #Продолжается игра или нет
while game:
    time.tick(FPS) #Ограничение ФПС для цикла
    for e in pygame.event.get():   #берём события по одному
        if e.type == pygame.QUIT:
            game = False

    gamedisplay.fill(BLACK)
    cars.draw(gamedisplay)
    if not finish:
        cars.update()
    else:
        gamedisplay.blit(myTextIMG, (100, 0))
    pygame.display.update()
pygame.quit()
