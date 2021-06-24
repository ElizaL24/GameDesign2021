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
        KeyBoardKey=pygame.key.get_pressed()
        if KeyBoardKey[pygame.K_LEFT]:
            xufo -=speed
            pygame.display.flip()
        if KeyBoardKey[pygame.K_RIGHT]:
            xufo +=speed
            pygame.display.flip()
        
        rockList=["1", "2", "3"]
        rockNumber=random.choice(rockList)
        class Player2(pygame.sprite.Sprite):
                def __init__(self):
                    pygame.sprite.Sprite.__init__(self)
                    self.images = []

                    image = pygame.image.load(os.path.join("gamefolder\images\Asteroid", str(rockNumber), ".jpg")).convert()
                    self.images.append(image)
                    self.image = self.images[0]
                    self.rect = self.image.get_rect()

        player2 = Player2()   # spawn player
        player2.rect.x = 64   # go to x
        player2.rect.y = 64  # go to y
        player_list = pygame.sprite.Group()
        player_list.add(player)
        screen.blit(screen, (100,100))
        player_list.draw(screen) # draw player
        pygame.display.flip()
        clock.tick(40)


def main():
    movement()

    
def instructions():
    print("play")

def display_message(message):
    pygame.time.delay(500)
    screen.fill(WHITE)
    text = WordFont.render(message, 1, BLACK)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)


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
                    display_message("goodbye!!")
                    pygame.quit()
                    sys.exit()
        pygame.display.update()  


mainMenu("Please select a menu option")


pygame.quit()