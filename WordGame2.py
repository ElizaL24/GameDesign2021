#Eliza Lamster
#6/9/21
import random
import os
import sys

x=1  #global variable

def dashPrint():
    if char in guesses:
        print (char,end=' ')
    else:
        print ("-", end=' ')

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

def score():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~                             ~")
    print("~            Scores           ~")             
    print("~        1: Play Game         ~")
    print("~        2: Show Scores       ~")
    print("~        3: Exit Game         ~")
    print("~                             ~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def pause():
    print("Do you want to play again?")
    answer1= input()
    answer1=answer1.upper()
    if "Y" in answer1:
        return True
    else:
        return False

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
                word=random.choice(gameWords)
                counter=len(word)
                print("There are", counter, "letters in the word.")
                turns=len(word)
                turns=turns-3
                print("You have", turns, "tries to guess the word.")
                print(word)
                print()
                guesses=''
                
                for char in word:
                    dashPrint()

                while turns>0 and counter>0:               
                    newGuess=input("\n\nGive me a letter")
                    if newGuess not in word:
                        turns-=1   # short way to write -1 from turns every time
                        print("Wrong!")
                        print("You have", turns, "guesses left")  

                    else:
                        amt=word.count(newGuess)
                        counter-=amt
                        print("Good guess!")
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
        convert=True
        while convert:
            print("'Share Scores' selected")
            FILE=open("ElizaGame.txt", 'a')
            newline="\nPlayer Scores"
            FILE.write(newline)
            FILE.write(newline)
            FILE.close()
            print("Scores shared")
            convert=False
print("Goodbye, thank you for playing!")


 
        # let the user stay in the level and reuse it many times until they want to get back to main menu
    