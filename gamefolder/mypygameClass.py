#Eliza Lamster
#6/16/2021

import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP

# K_UP
# K_DOWN
# K_RIGHT
# K_LEFT

pygame.init()
pygame.time.delay(100)
WIDTH=500
HEIGHT=600
bg=pygame.image.load("gamefolder\images\Sunsetst.jpg")
#create object to open window
screen=pygame.display.set_mode((WIDTH,HEIGHT))


lightBlue=(171,219,227)

lavender=(172, 155, 181)

magenta=(111, 4, 72)

white=(255,255,255)

pinkSalmon=(157, 40, 72)

pygame.display.flip()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(lavender)
pygame.display.set_caption("My Game")
pygame.display.update()

x=10
y=10
rad=30
hbox,wbox=20,20
rect=pygame.Rect(x, y, hbox,wbox)
rect2=pygame.Rect(x, y+50, hbox,wbox)

JumpCheck=False
jump=10
check=True
while check:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            check=False
    speed=2
    KeyBoardKey=pygame.key.get_pressed()
    if KeyBoardKey[pygame.K_LEFT]:
        rect.x -=speed
    if KeyBoardKey[pygame.K_RIGHT]:
        rect.x +=speed

    if not JumpCheck:
        if KeyBoardKey[pygame.K_UP]:
            rect.y -=speed
        if KeyBoardKey[pygame.K_DOWN]:
            rect.y +=speed
        if KeyBoardKey[K_SPACE]:
            JumpCheck=True
    else:
        if jump>=-10:
            rect.y-=(jump*abs(jump))/2
            jump-=1
        else:
            jump=10
            JumpCheck=False
    if KeyBoardKey[pygame.K_y]:
        rad +=speed
    if KeyBoardKey[pygame.K_h]:
        rad-=speed
        KeyBoardKey=pygame.key.get_pressed()
    if KeyBoardKey[pygame.K_a]:
        rect2.x -=speed
    if KeyBoardKey[pygame.K_d]:
        rect2.x +=speed
    if KeyBoardKey[pygame.K_w]:
        rect2.y -=speed
    if KeyBoardKey[pygame.K_s]:
        rect2.y +=speed
    if rect.colliderect(rect2):
        rect.x -=3
        rect2.x +=3
    circle=pygame.draw.circle(screen,(white), (x+240, y+290), rad, 4)
    if circle.collidepoint(rect.x+10, rect.y+10):
        rect.x-=10
        rect.y-=4
    if circle.collidepoint(rect2.x+10, rect2.y+10):
        rect2.x-=10
        rect2.y-=4
    if rect.x < 10: rect.x=10
    if rect.x > WIDTH-wbox-10: rect.x=WIDTH-wbox-10
    if rect.y < 10: rect.y=10
    if rect.y > HEIGHT-hbox-10: rect.y=HEIGHT-hbox-10
    if rect2.x < 10: rect2.x=10
    if rect2.x > WIDTH-wbox-10: rect2.x=WIDTH-wbox-10
    if rect2.y < 10: rect2.y=10
    if rect2.y > HEIGHT-hbox-10: rect2.y=HEIGHT-hbox-10
    if rad > 240: rad=240
    screen.fill(lavender)

    screen.blit(bg,(0,0))

    pygame.draw.rect(screen,(pinkSalmon),rect)
    pygame.draw.rect(screen,(lightBlue),rect2)
    pygame.draw.circle(screen,(white), (x+240, y+290), rad, 4)
    pygame.display.flip()
    pygame.time.delay(30)
pygame.quit()

