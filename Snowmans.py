import pygame
from random import randint as ri

gamedisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snowmans")


def draw_snowmen(x, y, hat=False):
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

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = e.pos
            if ri(0, 10):
                draw_snowmen(mouseX, mouseY)
            else:
                draw_snowmen(mouseX, mouseY, True)





    pygame.display.update()
pygame.quit()
