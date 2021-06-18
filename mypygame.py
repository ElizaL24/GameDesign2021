#Eliza Lamster
#6/16/2021

import pygame

pygame.init()
pygame.time.delay(100)
WIDTH=500
HEIGHT=600
bg=pygame.image.load(Desktop/Game Design 10/GameDesign2021/images/Sunsetave.jpg)
#create object to open window
surface=pygame.display.set_mode((WIDTH,HEIGHT))

color=15, 15, 15,
surface.fill(color)
pygame.display.flip()


color=(171,219,227)


pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
pygame.display.flip()

color=(172, 155, 181)

pygame.draw.rect(surface, color, pygame.Rect(120, 30, 60, 60))
pygame.display.flip()

color=(111, 4, 72)

pygame.draw.rect(surface, color, pygame.Rect(210, 30, 60, 60))
pygame.display.flip()


color=(157, 40, 72)


pygame.draw.rect(surface, color, pygame.Rect(300, 30, 60, 60))
pygame.display.flip()

color=(140, 72, 87)


pygame.draw.rect(surface, color, pygame.Rect(390, 30, 60, 60))
pygame.display.flip()


color=(184, 155, 136)


pygame.draw.rect(surface, color, pygame.Rect(390, 30, 60, 60))
pygame.display.flip()

check=True
while check:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            check=False
pygame.quit()

