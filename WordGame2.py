#Eliza Lamster
#6/9/21
import random
import os
import sys
import datetime
import time

x=1  #global variable

gameWords= ['python','audio','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']

def menu ():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~                             ~")
    print("~       Guess the Word!       ~")
    print("~                             ~")
    print("~            Menu             ~")
    print("~                             ~")
    print("~       1: Play Game          ~")
    print("~       2: Show Scores        ~")
    print("~       3: Exit Game          ~")
    print("~                             ~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("please enter your selection from 1 to 3")
    inputNumber = input()
    x = int(inputNumber)
    return x
    
def pause():
    print("Do you want to play again?")
    answer1= input()
    answer1=answer1.upper()
    if "Y" in answer1:
        return True
    else:
        return False

def dashPrint():
    if char in guesses:
        print (char,end=' ')
    else:
        print ("-", end=' ')

def fileW():
    FILE=open("ElizaGame.txt", 'a')
    newline="\n"
    writefile =newline+x.strftime("%m")+"/"+x.strftime("%d")+"/"+x.strftime("%y")+"          "+wins+"          "+name
    FILE.write(writefile)
    print("Scores shared")
    print()
    FILE.close()

def fileR():
    FILE=open("ElizaGame.txt", 'r')
    print()
    print("Here is the current scoreboard:")
    time.sleep(1)
    print(FILE.read())
    print()
    time.sleep(1)
    FILE.close()

def fileSortR():
    scoredata="ElizaGame.txt"
    FILE=open(scoredata, 'r')
    content_List=FILE.readlines()
    for element in content_List:
        global elem_List
        elem_List=element.split()
    FILE.close()
    with open(scoredata, "r") as firstfile:
        rows=firstfile.readlines()
        sorted_rows=sorted(rows, key = lambda x: int(x.split()[1]), reverse=True,)
        leaderboard=[sorted_rows[0:9]]
        for row in leaderboard:
            print(row)
            print()
    FILE.close()


os.system('cls')



#start of code
print("Hello!")   
name=input("What is your name?")
name=name.capitalize()

while x !=3:  
    x=menu()
    if(x==1):        #if statement are selection or branching
        global wins
        wins=0
        convert=True
        while convert:
            print()
            print("'Play Game' Chosen")
            print()
            print("Are you ready to start,", name,)
            answer=input()

            answer=answer.upper()
            while "Y" in answer:
                print("Okay. Good luck,", name,)
                time.sleep(1.5)
                os.system('cls')
                word=random.choice(gameWords)
                counter=len(word)
                print("There are", counter, "letters in the word.")
                turns=len(word)
                turns=turns-3
                print("You have", turns, "tries to guess the word.")
                print()
                guesses=''
                
                for char in word:
                    dashPrint()

                while turns>0 and counter>0:               
                    newGuess=input("\n\nGive me a letter   ")
                    if newGuess not in guesses:
                        if newGuess not in word:
                            turns-=1   # short way to write -1 from turns every time
                            print("Wrong!")
                            print("You have", turns, "guesses left")  

                        else:
                            amt=word.count(newGuess)
                            counter-=amt
                            print("Good guess!")
                    else:
                        print("You used this letter already. Try again.")    
                    
                    guesses += newGuess
                    
                    for char in word:
                        dashPrint ()
                print()
                print()
                if counter==0:
                    print("Game Over")
                    print("You won and guessed the word!")
                    wins+=1
                    print("You have currently guessed", wins, "words. Keep playing to increase your score!")
                if turns==0:
                    print("Game Over")
                    print("You ran out of turns. Better luck next time!")
                    print("The word was", word)
                answer="no"
            print("Thank you for playing,", name)

            convert=pause()

 
        # let the user stay in the level and reuse it many times until they want to get back to main menu
    if(x==2):
        wins=str(wins)
        x=datetime.datetime.now()
        convert=True
        while convert:
            print("'Share Scores' selected")
            fileW()
            fileSortR()
            convert=False
print("Goodbye, thank you for playing!")
time.sleep(5)
os.system('cls')

 
        # let the user stay in the level and reuse it many times until they want to get back to main menu
    