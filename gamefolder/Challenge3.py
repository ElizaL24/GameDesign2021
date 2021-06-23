#Eliza Lamster
#6/8/2021
print("Welcome to Grammar Police!")
print("In this game, you will be asked to make a sentance with correct grammar.")
print("Please enter one of the following menu options by typing in the corresponding number.")
print()
print()
print()
print()
print()
print()
print()
print()

def menu ():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~                             ~")
    print("~       Grammar Police!       ~")
    print("~                             ~")
    print("~            Menu             ~")
    print("~                             ~")
    print("~          1: Easy            ~")
    print("~      2: Intermediate        ~")
    print("~        3: Advanced          ~")
    print("~       4: Exit Game          ~")
    print("~                             ~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def instructions1 ():
    print("Type in the given words. Capitalize the words that should be capitalized.")
    print("Once you are ready to submit, press 'enter'.")

def instructions2 ():
    print("Type in the letter corresponding to the correctly capitalized sentance.")
    print("Once you are ready to submit, press 'enter'.")

def pause():
    print("press 'enter' to continue")
    input()


menu ()

word=int(input()) 
print ()
while word in range (1,4):

    if word in range (1,2):
        print("You are now playing the easy level.")
        print("We all start somewhere! \(^^)/")
        print ()
        instructions1 ()
        print ()
        print ("There are two challenges in level 1.")
        print()
        pause()
        print("--Challenge 1 Words--")
        print()
        print("Dog    Blanket    Depot    Purple    Dwarf")
        print()
        answer1=str(input())
        result1=answer1.islower()
        print()
        print(result1)
        print ()
        pause()
        print("--Challenge 2 Words--")
        print ()
        print("Pluto    Grey    Harry    Iowa    Microsoft")
        answer2=str(input()) #input is a function
        result2=answer2.istitle() #istitle is a method of string. You have to refer it with a dot
        print()
        print(result2)
        print ()

    if word in range (2,3):
        print("You are now playing the intermediate level.")
        print("Keep playing and you might be able to play the advanced level.")
        print ()
        instructions2 ()
        print ()
        print ("There are two challenges in level 2.")
        print()
        pause()
        print("--Challenge 1--")
        print()
        print("Which clause correctly completes this sentancy:")
        print("'The food was very good,' Annie said,") 
        A="'In fact, it was great!'"
        print("A: ", A)
        B=A.capitalize()
        print ("B: ", B)
        answer2=(input())
        if "a" in answer2:
            ans2=answer2
            answer2=ans2.upper()
        if "b" in answer2:
            ans2=answer2
            answer2=ans2.upper()
        if "B" in answer2:
            print("Correct!")  
        if "A" in answer2:
                print ("Not Correct :(")
        print ()
        pause ()
        print ()
        print("--Challenge 2--")
        print()
        print()
        print ("which of these acronyms is capitalized correctly?")
        A="nasa"
        print("A: ", A)
        B=A.swapcase()
        print ("B: ", B)
        answer22=(input())
        if "a" in answer22:
            ans22=answer22
            answer22=ans22.upper()
        if "b" in answer22:
            ans22=answer22
            answer22=ans22.upper()
        if "B" in answer22:
            print("Correct!")  
        if "A" in answer22:
                print ("Not Correct :(")
        print ()
        print ()

    if word in range (3,4):
        print("You are now playing the advanced level.")
        print ("Good luck--you'll need it!")
        print ()
        print ("O U T   O F   O R D E R")  #I wasn't sure what to put in this level, so it's out of order for now.
    print()
    print()
    print("game over")
    print()
    print()
    print()
    menu ()   
    print("If you would like to play again, enter a number between 1 and 3")
    word=int(input())
print()
print()
print("Thank you for playing Grammar Police!")



