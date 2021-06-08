#Eliza
#6/7/2021
print("Welcome to Grammar Police!")
print("In this game, you will be asked to make a sentance with correct grammar.")
print(") Please enter one of the menu options.")
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
        print("--Challenge 1 Words--")
        print("Dog    Blanket    Depot    Purple    Dwarf")
        answer1=str(input())
        result1=answer1.islower()
        print()
        print()
        print(result1)
        print ()
        print ()
        print("--Challenge 2 Words--")
        print("Mercury    Grey    Harry    Iowa    Microsoft")
        answer2=str(input())
        result2=answer2.istitle()
        print()
        print()
        print(result2)
        print ()
        print ()
        print("--Challenge 3 Words--")
        print("Mercury    Grey    Harry    Iowa    Microsoft")
        answer2=str(input())
        result2=answer2.istitle()
    if word in range (2,3):
        print("You are now playing the intermediate level.")
        print("Keep playing and you might be able to play the advanced level.")
        print ()
        instructions2 ()
        print ()
        print ("There is one challenge in level 2.")
        print("Which clause correctly completes this sentancy:")
        print("'The food was very good,' Annie said,") 
        A="'In fact, it was great'!"
        print(A)
        B=A.capitalize()
        print (B)
        answer2=str(input())
        while "a" in answer2:
            ans2=answer2.upper
        while "b" in answer2:
            ans2=answer2.upper
        if "B" in answer2:
            print("Not Correct :(")  
        if "A" in answer2:
                print ("Correct!")
    if word in range (3,4):
        print("You are now playing the advanced level.")
        print ("Good luck--you'll need it!")
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
print("Thank you for playing My Game!")



