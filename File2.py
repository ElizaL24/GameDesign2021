#Eliza Lamster
#6/14/2021
#Today we are learning about files

import os
import sys
import time

#using time to pause your games
os.system('cls')

file="asdFre.txt"
FILE=open(file, 'r')
content=FILE.read()
print(content)
FILE.close()
FILE=open(file, 'r')
content_List=FILE.readlines()
time.sleep(.5)
print()
print(content_List)
FILE.close()
print()
time.sleep(.5)
for element in content_List:
    print ("Line:", element, end="")
    elem_List=element.split()
    print(elem_List)
    print()



