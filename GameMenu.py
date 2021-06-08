#Eliza
#6/7/2021
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
    print("~        Level: Easy          ~")
    print("~    Level: Intermediate      ~")
    print("~      Level: Advanced        ~")
    print("~         Exit Game           ~")
    print("~                             ~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

menu () #this is a function call

word=str(input())
print ()
while "Level" in word:
    print("You are now playing", word)
    print()
    print()
    print()
    print("game over")
    print()
    print()
    print()
    menu ()   
    word=str(input())
print()
print()
print("Thank you for playing My Game!")


