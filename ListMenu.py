#Eliza Lamster
#6/9/21
l1="********************************"
l2="*       My game                *"
l3="*                              *"
l4="*    1 - Add Item              *"
l5="*    2 - Delete Item           *"
l6="*    3 - Reverse List Order    *"
l7="*    4 - Find index of char    *"
l8="*    5 - Clear List            *"
l9="*    6 - Show List             *"
l10="*   7 - Exit                  *"
l11="********************************"
x=1  #global variable
def menu():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)
    print(l9)
    print(l10)
    print(l11)
    print("please enter your selection from 1 to 7")
    inputNumber = input()
    x = int(inputNumber)
    return x
def score():
    print(l1)
    print("*        Scores          *")
    print(l3)
    print("*    1 - ???- 999        *")
    print("*    2 - ???- 876        *")
    print("*    3 - ???- 745        *")
    print(l3)
    print(l8)
def pause():
    print("Do you want to play again?")
    answer1= input()
    answer1=answer1.upper()
    if "Y" in answer1:
        return True
    else:
        return False
 
myAnimals=["Dog", "Bear", "Tiger", "Panda", "Shark"]

while x !=4:  
    x=menu()
    if(x==1):        #if statement are selection or branching
        convert=True
        while convert:
            convert=pause()
 
        # let the user stay in the level and reuse it many times until they want to get back to main menu
    if(x==2):
        convert=True
        while convert:
            convert=3
            print("Clear List Chosen")
            print("Here is the current list:")
            print(myAnimals)
            print("Which item would you like to remove? Please enter a number between 1 and", len(myAnimals))
            index=int(input())
            index=index-1
            myAnimals.pop(index)
            print(myAnimals)
            convert=pause()

    if(x==3):
        convert=True
        while convert:
            print("Lowercase Chosen")
            print("Please ener a phrase in upper case")
            answer=input() #input is a function
            answer=answer.lower() #update your variable to the new change if I dont need orginal value 
            print(answer)
            convert=pause()

    if(x==4):
        convert=True
        while convert:
            print("Index of Character Chosen")
            print("Please ener a sentance.")
            sentance=input() #input is a function
            print("please enter a word or character in the sentance that you would like to print")
            character=str(input())
            txt=sentance.index(character)
            print(txt)
            convert=pause()

    if(x==6):        #if statement are selection or branching
        convert=True
        while convert:
            print("Show List Chosen")
            print()
            print("Animals:")
            for animals in myAnimals:
                print(animals)
            convert=pause()
 
print("Goodbye, Thank you for playing")



 
        # let the user stay in the level and reuse it many times until they want to get back to main menu
    