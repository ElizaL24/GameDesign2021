#Eliza Lamster
#6/23/21

import os, sys, time, pygame, random, math

os.system('cls')  

pygame.init()  

clock=pygame.time.Clock()
#Create my display screen  

WIDTH = 1300  # uppercase because it behaves as constant  
HEIGHT = 800   
screen = pygame.display.set_mode((WIDTH,HEIGHT))  
pygame.display.set_caption("Spave Evade!")  

# Define Colors  
WHITE = [255,255,255]  

BLACK = [0,0,0]  
ALPHA=BLACK
NAVY = [19, 7, 130]
BLUEGRAY=[101, 106, 148]

Wbox=30
dist=10

TitleFont= pygame.font.SysFont("comicsans", 70) 
WordFont=pygame.font.SysFont("comicsans", 50)
LetterFont=pygame.font.SysFont("comicsans",40)



def movement():
    print("playing")
    screen.fill(BLACK)
    x=10
    y=385
    rad=30
    hbox,wbox=20,20
    xufo=30
    yufo=385
    img = pygame.image.load(r"gamefolder\images\UFOspritefinal.jpg")

    xyz=True
    while xyz:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                xyz=False

        screen.fill(BLACK)
        screen.blit(img, (xufo,yufo))
        pygame.display.flip()
        speed=4
        rockList=["1", "2", "3"]
        rockNumber=random.choice(rockList)
        rockint=random.randint(0,2)
        global image
        image = pygame.image.load("gamefolder\images\Rock"+str(rockNumber)+".jpg")
        rockx=random.randint(0, 1301)
        rocky=0
        def Explosion():
            if image.screen_rect.collidepoint(xufo, yufo):
                img = pygame.image.load(r"gamefolder\images\Explosion1.jpg")
        xx=True
        while xx==True:
            screen.blit(image, (rockx, rocky))
            pygame.time.delay(4)
            KeyBoardKey=pygame.key.get_pressed()
            if KeyBoardKey[pygame.K_RIGHT]:
                xufo +=4
                if xufo>1300:
                    endGame()
                    xx=False
                rocky+=6
                screen.fill(BLACK)
                screen.blit(img, (xufo,yufo))
                screen.blit(image, (rockx,rocky))
                pygame.display.update()
                break
            else:
                rocky-=6
                screen.fill(BLACK)
                screen.blit(image, (rockx,rocky))
                pygame.display.update()
                break
            if rocky>1301:
                xx=False

        pygame.display.update()
        clock.tick(40)


   

def main():
    movement()

def display_message(message):
    pygame.time.delay(500)
    screen.fill(WHITE)
    text = WordFont.render(message, 1, BLACK)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

def display_instructions(message1, height1, message2, height2, message3, height3, message4, height4):
    pygame.time.delay(500)
    screen.fill(BLUEGRAY)
    text1 = TitleFont.render(message1, 1, WHITE)
    screen.blit(text1, (WIDTH/2 - text1.get_width()/2, height1))
    text2 = LetterFont.render(message2, 1, BLACK)
    screen.blit(text2, (WIDTH/2 - text2.get_width()/2, height2))
    text3 = LetterFont.render(message3, 1, BLACK)
    screen.blit(text3, (WIDTH/2 - text3.get_width()/2, height3))
    text4 = LetterFont.render(message4, 1, BLACK)
    screen.blit(text4, (WIDTH/2 - text3.get_width()/2, height4))
    pygame.display.update()
    pygame.time.delay(9000)

def instructions():
    display_instructions("Instructions:", 50, "Press the right arrow to move the spaceship", 220, "To win, make it to the right edge of the map", 320, "If you get hit by an asteroid, you lose", 420)

def endGame():
    display_instructions("~Winner~", 50, "You won!", 220, "The alien got to safety", 320, "He was not harmed by any asteroids", 420)


def mainMenu(message):
    test=True
    while test:
        #Print message
        screen.fill(BLACK)
        text = WordFont.render(message, 1, WHITE)
        screen.blit(text, (WIDTH/2 - text.get_width()/2, round(HEIGHT/3)))
       
        #rect1
        rect1=pygame.Rect(50, 350, Wbox*10,Wbox*2)
        pygame.draw.rect(screen, NAVY, rect1)
        text = LetterFont.render("Play", 1, WHITE)
        screen.blit(text, (55 , 355))
       
        #rect 2
        rect2=pygame.Rect(500, 350, Wbox*10,Wbox*2)
        pygame.draw.rect(screen, NAVY, rect2)
        text = LetterFont.render("Instructions", 1, WHITE)
        screen.blit(text, (505 , 355))

        #rect 3
        rect3=pygame.Rect(950, 350, Wbox*10,Wbox*2)
        pygame.draw.rect(screen, NAVY, rect3)
        text = LetterFont.render("Exit Game", 1, WHITE)
        screen.blit(text, ((955, 355)))
       
        #Check collide Point and rectangle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if rect1.collidepoint((mx,my)):
                    main()
                if rect2.collidepoint((mx,my)):
                    instructions()
                if rect3.collidepoint((mx,my)):
                    display_message("Goodbye, thank you for playing!")
                    pygame.quit()
                    sys.exit()
        pygame.display.update()  


mainMenu("Please select a menu option")


pygame.quit()