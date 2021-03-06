#Eliza Lamster
#6/23/21

import os, sys, time, pygame, random, math

os.system('cls')  

pygame.init()  

clock=pygame.time.Clock()
#Create my display screen  

WIDTH = 800  # uppercase because it behaves as constant  
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

    char=pygame.Rect(x, y, hbox,wbox)
    class Player(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.images = []

                img = pygame.image.load(os.path.join(r"gamefolder\images\UFOspritefinal.jpg")).convert()
                img.convert_alpha() 
                img.set_colorkey(ALPHA)
                self.images.append(img)
                self.image = self.images[0]
                self.rect = self.image.get_rect()
    xufo=30
    yufo=385
    xyz=True
    while xyz:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                xyz=False

        screen.fill(BLACK)
        player = Player()   # spawn player
        player.rect.x = xufo   # go to x
        player.rect.y = yufo  # go to y
        player_list = pygame.sprite.Group()
        player_list.add(player)
        screen.blit(screen, (xufo,yufo))
        player_list.draw(screen) # draw player
        pygame.display.flip()
        clock.tick(40)

        speed=4

        rockList=["1", "2", "3"]
        rockNumber=random.choice(rockList)
        rockint=random.randint(0,2)
        image = pygame.image.load("gamefolder\images\Rock"+str(rockNumber)+".jpg")
        rockx=random.randint(0, 801)
        rocky=800
        screen.blit(image, (rockx,rocky))
        pygame.time.delay(10)
        xx=True
        while xx==True:
            pygame.time.delay(4)
            rocky-=4
            screen.fill(BLACK)
            screen.blit(image, (rockx,rocky))
            pygame.display.update()
            KeyBoardKey=pygame.key.get_pressed()
            if KeyBoardKey[pygame.K_RIGHT]:
                xufo +=speed
                pygame.display.flip()

            if rocky<0:
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



def mainMenu(message):
    test=True
    while test:
        #Print message
        screen.fill(BLACK)
        text = WordFont.render(message, 1, WHITE)
        screen.blit(text, (WIDTH/2 - text.get_width()/2, round(HEIGHT/3)))
       
        #rect1
        rect1=pygame.Rect(50, 350, Wbox*7,Wbox*2)
        pygame.draw.rect(screen, NAVY, rect1)
        text = LetterFont.render("Play", 1, WHITE)
        screen.blit(text, (55 , 355))
       
        #rect 2
        rect2=pygame.Rect(295, 350, Wbox*7,Wbox*2)
        pygame.draw.rect(screen, NAVY, rect2)
        text = LetterFont.render("Instructions", 1, WHITE)
        screen.blit(text, (300 , 355))

        #rect 3
        rect3=pygame.Rect(540, 350, Wbox*7,Wbox*2)
        pygame.draw.rect(screen, NAVY, rect3)
        text = LetterFont.render("Exit Game", 1, WHITE)
        screen.blit(text, ((545, 355)))
       
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