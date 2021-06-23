# Maria Suarez  

# Create a Hanggman version of the game:  

# Use images in a list, Use Fonts, render them  

 
 

import os, sys, time, pygame, random, math  

os.system('cls')  

pygame.init()  

#Create my display screen  

WIDTH = 800  # uppercase because it behaves as constant  
HEIGHT = 500   
screen = pygame.display.set_mode((WIDTH,HEIGHT))  
pygame.display.set_caption("Hangman GAME!")  

# Define Colors  
WHITE = [255,255,255]  

BLACK = [0,0,0]  
# Word lists  
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware'] 

# load images to list  

images = []  

for i in range(7): 
    image=pygame.image.load("gamefolder\ImagesHMgame\hangman"+str(i)+".png")
    images.append(image)  
    # screen.blit(images[i], (100,100))  
    # pygame.display.update()  
    # pygame.time.delay(300)  

# Define Font objects  
TitleFont= pygame.font.SysFont("comicsans", 70)  #set the type of font and the size   
WordFont=pygame.font.SysFont("comicsans", 50)  
LetterFont=pygame.font.SysFont("comicsans", 40) 

#Define letters for rectangular buttons 
A=65 
Wbox=30 
dist=10 
letters=[]#an array of arrays  [[x,y, ltr, boolean]] 
#DEfine where to start our drawing 26 letter, 13 letter in each line 
startx= round((WIDTH - (Wbox + dist)*13) /2) #int function round 
starty= 350 

#load the letters into our double array 
def alphabet():
    for i in range(26): 
        x=startx +dist*2+((Wbox +dist)*(i%13)) 
        y=starty+((i//13)*(dist + Wbox *2)) 
        letters.append([x,y,chr(A+i), True]) 
def game_intro(message):
    test=True
    while test:
        #Print message
        screen.fill(WHITE)
        text = WordFont.render(message, 1, BLACK)
        screen.blit(text, (WIDTH/2 - text.get_width()/2, round(HEIGHT/3)))
        #rect1
        rect1=pygame.Rect(150, 350, Wbox*2,Wbox*2)
        pygame.draw.rect(screen, BLACK, rect1, width=1)
        text = LetterFont.render("Yes", 1, BLACK)
        screen.blit(text, (160 , 350))
        #rect 2
        rect2=pygame.Rect(550, 350, Wbox*2,Wbox*2)
        pygame.draw.rect(screen, BLACK, rect2, width=1)
        text = LetterFont.render("No", 1, BLACK)
        screen.blit(text, (560 , 350))
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
                    dis_message("goodbye!!")
                    pygame.quit()
                    sys.exit()

        pygame.display.update()  


#Function to update the screen 

def updateScreen(turns,displayWord):  

    screen.fill(WHITE)  

    title=TitleFont.render("Hangman",1, BLACK)  

    centerTitle= WIDTH/2-title.get_width()/2  

    screen.blit(title, (centerTitle,20))  

    screen.blit(images[turns], (100,100))  

    textW=WordFont.render(displayWord,1, BLACK)  

    screen.blit(textW, (300,150))  

    for letter in letters: 

        x,y,ltr, see= letter 

        if see: 

            rect=pygame.Rect(x-Wbox/2,y-Wbox/2,Wbox,Wbox) 

            pygame.draw.rect(screen, BLACK, rect, width=1)  

            text=LetterFont.render(ltr,1,BLACK) 

            screen.blit(text,(x -text.get_width()/2,y -text.get_height()/2)) 

    pygame.display.update()  




def updateWord(word, guesses):  # function with a parameter to update word  

    displayWord=""  

    for char in word:  

        if char in guesses:  

            displayWord += char+" "  

        else:  

            displayWord += "_ "  

    return displayWord  




def dis_message(message): 

    screen.fill(WHITE) 

    text =TitleFont.render(message,1,BLACK)

    centerTitle= WIDTH/2-text.get_width()/2   
    centerTitleh= HEIGHT/2-text.get_height()/2  

    screen.blit(text, (centerTitle, centerTitleh)) 

    pygame.display.update() 

    pygame.time.delay(2000) 

def dis_message2(message): 

    screen.fill(WHITE) 

    text =LetterFont.render(message,1,BLACK)

    centerTitle= WIDTH/2-text.get_width()/2   
    centerTitleh= HEIGHT/2-text.get_height()/2  

    screen.blit(text, (centerTitle, centerTitleh)) 

    pygame.display.update() 
    pygame.time.delay(10000) 


#always have a way to close your screen  

def main():
    word=random.choice(gameWords).upper() 
    turns= 0   #should we conider controlling this number when he/she misses      
    guesses=[] 
    alphabet()
    check = True  
    while check:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                check = False     
            if event.type == pygame.MOUSEBUTTONDOWN: 
                mx, my =pygame.mouse.get_pos() 
                for letter in letters: 
                    x,y,ltr,see=letter 
                    if see: 
                        rect=pygame.Rect(x-Wbox/2, y-Wbox/2,Wbox, Wbox) 
                        if rect.collidepoint(mx,my):  #if letter has been click 
                            letter[3]=False 
                            guesses.append(ltr) 
                            if ltr not in word: 
                                turns +=1 

                

        displayWord=updateWord(word, guesses)  

        updateScreen(turns, displayWord)  

        #check if we won or lost the game 

        won=True 

        for letter in word: 

            if letter not in guesses: 

                won=False 

                break 

        if won: 

            dis_message("You Won!!!") 

            break 

        if turns == 6: 

            dis_message("You lost") 

            break   

main()
while True:
    game_intro("Would you like to play again?")
pygame.quit()  

sys.exit()  

 