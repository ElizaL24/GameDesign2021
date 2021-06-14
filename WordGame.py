#Eliza Lamster
#6/11/2021
#We are creating a list of words
#The computer will randomly select a word from the list for the user to guess
#Give the user multiple tries
#Show the word to the user with the characters they have guessed

import random

def dashPrint():
    if char in guesses:
        print (char,end=' ')
    else:
        print ("-", end=' ')

gameWords= ['python','audio','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']

def pause():
    print("Do you want to play again?")
    answer1= input()
    answer1=answer1.upper()
    if "Y" in answer1:
        return True
    else:
        return False

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

menu () #this is a function call

word=int(input())
print ()


while x !=4:  
    x=menu()
    if(x==1):        #if statement are selection or branching
        convert=True
        while convert:
            print()
            print("'Play Game' Chosen")
            print()
            print("Hello!")
            name=input("What is your name?")
            name=name.capitalize()
            print("Do you want to guess a word,", name,)
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
                if turns==0:
                    print("Game Over")
                    print("You ran out of turns. Better luck next time!")
                    print("The word was", word)
                answer=input("Would you like to play again?").upper()
            print("Thank you for playing,", name)

            convert=pause()

    if word in range (2,3):
        print()
        print("'Show Scores' Chosen")
        print()
    if word in range (3,4):
        print()
    





    