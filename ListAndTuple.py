#Eliza Lamster
#6/10/2021
# cntr / will put hashtag, make comment

#Using a module/library by importing
import random

FruitList=["apples", "strawberries", "mangos", "pineapples"]

#prints horizontally
print(FruitList)
print()

#prints vertically
for fruit in FruitList:
    print(fruit)
print()

#prints horizontally without quote marks or brackets
for fruit in FruitList:  #for each element of array, it gets the element
    print(fruit, end=", ")
print()
print()

#prints horizontally without quote marks or brackets and without a comma after the last element in list
counter=len(FruitList)
for x in range(0,counter-1):  #prints all but the last one
    print(FruitList[x], end=", ")
print(FruitList[counter-1])  #prints last one
print()

#Randomly picking a fruit
#randint picks a random number, then finds the fruit that has that index
indx=random.randint(0,counter-1)
print("Your lucky fruit is", FruitList[indx])
print()

#choice randomly picks an iitem from list
word=random.choice(FruitList)
print("Your random fruit is", word)
print()

#checks if apples are in the list. If they are, it removes them
if "apples" in FruitList:
    print("Yes, you got apples.")
    FruitList.remove("apples")
    print(FruitList)
print()

#adds kiwis in first spot
FruitList.insert(0, "kiwis")
print (FruitList)
print()

#adds papayas in third spot
FruitList.insert(2, "papayas")
print (FruitList)
print ()

#Adds limes in last spot
FruitList.append("limes")
print(FruitList)
print()
print()
print()

#Making a tuple
MoreFruit=("Apples", "Pears", "Bananas")


#Converting the tuple to a list
print("Tuple", MoreFruit)
temp=list(MoreFruit)
print("List", temp)

#adding item to list/tuple
temp.insert(1, "Kiwis")
MoreFruit=tuple(temp)
print("Modified Tuple", MoreFruit)
print("Modified List", temp)

for element in MoreFruit:
    print(element)

