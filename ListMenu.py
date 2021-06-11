#Eliza Lamster
#6/9/21
l1="********************************"
l2="*       My game                *"
l3="*                              *"
l4="*    1 - Add Item              *"
l5="*    2 - Delete Item           *"
l6="*    3 - Ask if Item in List   *"
l7="*    4 - Find Item             *"
l8="*    5 - Reverse List Order    *"
l9="*    6 - Exit                  *"
l10="*******************************"
x=1
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
    print("please enter your selection from 1 to 6")
    x = int(input())
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

while x!=6:
    x=menu()
    if(x==1):
        convert=True
        while convert:
            convert=3
            print("Add Item Chosen")
            print("Here is the current list:")
            print(myAnimals)
            print("What animal would you like to add?")
            animal=str(input())
            len2=len(myAnimals)
            len2=len2+2
            print("Which spot would you like your item in? Please enter a number between 1 and", len(myAnimals))
            print("Your animal will be before the animal in the slot of the number you enter.")
            print("If you would like it to go last, enter Last")
            spot=input()
            if "Last" in spot:
                myAnimals.append(animal)
                print(myAnimals)
            else:
                spot=int(spot)
                spot=spot-1
                myAnimals.insert(spot,animal)
                print(myAnimals)
            convert=pause()
 
        # let the user stay in the level and reuse it many times until they want to get back to main menu
    if(x==2):
        convert=True
        while convert:
            convert=3
            print("Delete Item Chosen")
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
            convert=3
            print("Ask if List Contains Item Chosen")
            print("Please enter the item you want to search the list for.")
            searchx=str(input()) #input is a function
            searchx=searchx.capitalize() #update your variable to the new change if I dont need orginal value 
            if searchx in myAnimals:
                print("Yes,", searchx, "is in the list.")
            else:
                print("No,", searchx, "is not in the list.")
            convert=pause()

    if(x==4):
        convert=True
        while convert:
            print("Find Item Chosen")
            print("Please enter the item you want to find in the list.")
            findx=str(input()) #input is a function
            findx=findx.capitalize()
            indexx=myAnimals.index(findx)
            indexx=indexx+1
            print(findx, "is in spot", indexx)
            convert=pause()

    if(x==5):        #if statement are selection or branching
        convert=True
        while convert:
            print("Reverse List Order Chosen")
            myAnimals.reverse()
            print(myAnimals)
            convert=pause()
 
print("Goodbye, Thank you for playing")



 
        # let the user stay in the level and reuse it many times until they want to get back to main menu
    