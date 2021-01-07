import pygame
from random import randint as ri

gamedisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snowmans")


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



BLACK = (0,0,0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)

game = True
while game:

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            game = False


    draw_chess(8,8)

    pygame.display.update()
pygame.quit()
