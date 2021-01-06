import pygame

pygame.init()

gamedisplay = pygame.display.set_mode((800, 600))  # Создаём экран размером 800 на 600
pygame.display.set_caption("Guess the flag")  #Меняем заголовок окна
gamedisplay.fill((100, 100, 100))

russia = pygame.image.load("img/Russia.png")
gb = pygame.image.load("img/greatbritan.jpg")
ukraine = pygame.image.load("img/ukraine.jpg")
usa = pygame.image.load("img/usa.jpg")
japan = pygame.image.load("img/yaponii-flag.png")


russia = pygame.transform.scale(russia, (250, 180))
gb = pygame.transform.scale(gb, (250, 180))
ukraine = pygame.transform.scale(ukraine, (250, 180))
usa = pygame.transform.scale(usa, (250, 180))
japan = pygame.transform.scale(japan, (250, 180))

game = True  # Продолжается игра или нет
while game:

    for e in pygame.event.get():  # берём события по одному
        if e.type == pygame.QUIT:
            game = False


    gamedisplay.blit(russia, (0, 0))
    gamedisplay.blit(japan, (251, 0))

    pygame.display.update()
pygame.quit()
