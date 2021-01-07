import pygame
from random import randint as ri

gamedisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snowmans")


def draw_chess(x, y):
    pygame.draw.circle(gamedisplay, WHITE, (x,y), 25 )
    pygame.draw.circle(gamedisplay, WHITE, (x, y-35), 15 )
    if hat:
        pygame.draw.rect(gamedisplay, RED, ((x-10, y-75, 20, 30)))


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
