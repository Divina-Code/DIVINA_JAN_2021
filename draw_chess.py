import pygame
from random import randint as ri

pygame.init()

BLACK = (0,0,0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)



gamedisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snowmans")


#####ТЕКСТ НА ЭКРАН
#1
myFont = pygame.font.SysFont('Ink Free', 80)  #В скобочках название и размер шрифта
#2
myTextIMG = myFont.render("Hello", True, RED) #получаем картинку с нужным текстом
myTextIMG2 = myFont.render("How are u", True, RED) #получаем картинку с нужным текстом


def draw_chess(x, y):
    """

    :param x: Размер поля в клетках по ширине
    :param y: Размер поля в клетках по высоте
    :return:
    """
    startX = 100 #Вам нужно принимать этот параметр как необязательный, а не задавать тут
    startY = 100
    SIZE = 20

    for a in range(x):
        if a%2:
            pygame.draw.rect(gamedisplay, RED, ((startX+a*SIZE, startY, SIZE, SIZE)))
        else:
            pygame.draw.rect(gamedisplay, WHITE, ((startX+a*SIZE, startY, SIZE, SIZE)))




game = True
while game:

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            game = False


    draw_chess(8,8)
    #3
    gamedisplay.blit(myTextIMG, (250, 0))
    gamedisplay.blit(myFont.render("How are u", True, RED), (250, 100))
    pygame.display.update()
pygame.quit()
