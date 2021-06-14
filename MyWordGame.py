#Eliza Lamster
#6/11/2021
#We are creating a list of words
#The computer will randomly select a word from the list for the user to guess
#Give the user multiple tries
#Show the word to the user with the characters they have guessed

import random
gameWords= ['python','audio','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
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
    print("There are", counter, "letters in the word")
    print()
    turns=len(word)
    turns=turns-3
    guesses=''
    while turns>0 and counter>0:
        for char in word:
            if char in guesses:
                print (char,end=' ')
            else:
                print ("-", end=' ')
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
    print()
    print()
    print("Game Over")
    print("The word was", word)
    answer=input("Would you like to play again?").upper()
print("Thank you for playing,", name)
    