#Eliza
#6/8/2021
print("Welcome to My Game! Please enter one of the menu options.")
print()
print()
print()
print()
print()
print()
print()
print()
#global variables are defined in the far left column, but they can be used anywhere in your program.
    #local variables are in a tabbed column and will only work in their loop, function, etc.
def menu ():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~                             ~")
    print("~          My Game!           ~")
    print("~                             ~")
    print("~            Menu             ~")
    print("~                             ~")
    print("~          1: Easy            ~")
    print("~      2: Intermediate        ~")
    print("~        3: Advanced          ~")
    print("~       4: Exit Game          ~")
    print("~                             ~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

menu () #this is a function call

word=int(input())
print ()
while word in range (1,4):
    if word in range (1,2):
        print("You are now playing the easy level.")
        print("We all start somewhere! \(^^)/")
    if word in range (2,3):
        print("You are now playing the intermediate level.")
        print("Keep playing and you might be able to play the advanced level.")
    if word in range (3,4):
        print("You are now playing the advanced level.")
        print ("Good luck--you'll need it!")
    print()
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



