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
# Driver Code

for element in content_List:
    global elem_List
    elem_List=element.split()
    print(elem_List)

scoredata="asdFre.txt"

with open(scoredata, "r") as firstfile:
    rows=firstfile.readlines()
    sorted_rows=sorted(rows, key = lambda x: int(x.split()[3]), reverse=False)
    print(sorted_rows)

    




