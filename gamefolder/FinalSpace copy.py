#Eliza Lamster
#6/23/21

import os, sys, time, pygame, random, math, datetime

os.system('cls')  

pygame.init()  

clock=pygame.time.Clock()
#Create my display screen  

WIDTH = 1300  # uppercase because it behaves as constant  
HEIGHT = 800   
screen = pygame.display.set_mode((WIDTH,HEIGHT))  
pygame.display.set_caption("Space Evade!")  

# Define Colors  
WHITE = [255,255,255]  

BLACK = [0,0,0]  
ALPHA=BLACK
NAVY = [19, 7, 130]
BLUEGRAY=[101, 106, 148]
RED=[199, 0, 0]


Wbox=30
dist=10

TitleFont= pygame.font.SysFont("comicsans", 70) 
WordFont=pygame.font.SysFont("comicsans", 50)
LetterFont=pygame.font.SysFont("comicsans",40)

pts=0

def movement():
    pts=0
    rocks=[]
    for i in range (20):
        rockint=random.randint(1,3)
        image = pygame.image.load("gamefolder\images\Rock"+str(rockint)+".jpg")
        rockx=random.randint(0, 1301)
        rocky=0
        rocks.append([rockx, rocky, image, False])
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
        pts+=1
        screen.fill(BLACK)
        screen.blit(img, (xufo,yufo))
        speed=4
        #screen.blit(image, (rockx, rocky))
        pygame.time.delay(4)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                xyz=False
        KeyBoardKey=pygame.key.get_pressed()
        if KeyBoardKey[pygame.K_RIGHT]:
            xufo +=4
            if xufo>1300:
                endGame()
                xyz=False
                pts+=500
                return pts
        number=random.randint(0,9)
        rocks[number][3] = True
        item=0
        for i in range(10):
            if rocks[i][3]:
                rocks[i][1]+=2
            else:
                rocks[i][1]+=1
            imgrock=rocks[i][2]
            rockx=rocks[i][0]
            rocky=rocks[i][1]
            screen.blit(imgrock, (rockx, rocky))
            ufo_rect = pygame.Rect(xufo, yufo, 64, 64)
            rock_rect = pygame.Rect(rockx, rocky, 64, 64)
            if ufo_rect.colliderect(rock_rect): 
                img = pygame.image.load(r"gamefolder\images\Explosion1.jpg")
                pygame.time.delay(500)
                pygame.display.update()
                display_end("~Game Over~", 50, "You lost", 220, "The alien did not make it to safety", 320, "Instead, it got blasted to pieces by an asteroid", 420)
                xyz=False
                pts-=500
                return pts
        pygame.display.flip()



def display_message(message):
    pygame.time.delay(500)
    screen.fill(WHITE)
    text = WordFont.render(message, 1, BLACK)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

def display_end(message1, height1, message2, height2, message3, height3, message4, height4):
    pygame.time.delay(500)
    text1 = TitleFont.render(message1, 1, WHITE)
    screen.blit(text1, (WIDTH/2 - text1.get_width()/2, height1))
    text2 = LetterFont.render(message2, 1, RED)
    screen.blit(text2, (WIDTH/2 - text2.get_width()/2, height2))
    text3 = LetterFont.render(message3, 1, RED)
    screen.blit(text3, (WIDTH/2 - text3.get_width()/2, height3))
    text4 = LetterFont.render(message4, 1, RED)
    screen.blit(text4, (WIDTH/2 - text4.get_width()/2, height4))
    pygame.display.update()
    pygame.time.delay(5000)

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
    screen.blit(text4, (WIDTH/2 - text4.get_width()/2, height4))
    pygame.display.update()
    pygame.time.delay(5000)

def instructions():
    display_instructions("Instructions:", 50, "Press the right arrow to move the spaceship", 220, "To win, make it to the right edge of the map", 320, "If you get hit by an asteroid, you lose", 420)

def endGame():
    display_instructions("~Winner~", 50, "You won!", 220, "The alien got to safety", 320, "He was not harmed by any asteroids", 420)

scoredata="gamefolder\GameScores.txt"

def fileSortR():
    print("reading files")
    FILE=open(scoredata, 'r')
    content_List=FILE.readlines()
    for element in content_List:
        global elem_List
        elem_List=element.split()
    FILE.close()
    with open(scoredata, "r") as firstfile:
        rows=firstfile.readlines()
        sorted_rows=sorted(rows, key = lambda x: int(x.split()[4]), reverse=True,)
        print
        for row in sorted_rows:
            if content_List[1]>3:
                print(row)
            print(row)
    FILE.close()

def fileW():
    print("writing files")
    print("What name would you like to use?")
    name=input()
    FileWrite=open(scoredata,'a')
    x=datetime.datetime.now()
    line=name+"\t"+"SCORED"+"\t"+str(pts)+"\t"+"POINTS"+"\t"+str(x.month)+"/"+str(x.day)+"/"+str(x.year)
    FileWrite.write("\n"+line)
    FileWrite.close

def mainMenu(message):
    testing=True
    while testing:
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

        rect4=pygame.Rect(950, 450, Wbox*10,Wbox*2)
        pygame.draw.rect(screen, NAVY, rect4)
        text = LetterFont.render("Share Scores", 1, WHITE)
        screen.blit(text, ((955, 455)))

        rect5=pygame.Rect(50, 450, Wbox*10,Wbox*2)
        pygame.draw.rect(screen, NAVY, rect5)
        text = LetterFont.render("Show Scores", 1, WHITE)
        screen.blit(text, ((55, 455)))
        pygame.display.update()
        #Check collide Point and rectangle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if rect1.collidepoint((mx,my)):
                    movement()
                if rect2.collidepoint((mx,my)):
                    instructions()
                if rect3.collidepoint((mx,my)):
                    display_message("Goodbye, thank you for playing!")
                    pygame.quit()
                    sys.exit()
                if rect5.collidepoint((mx,my)):
                    fileSortR()
                if rect4.collidepoint((mx,my)):
                    fileW()

a=True
while a==True:
    mainMenu("Please select a menu option")


pygame.quit()