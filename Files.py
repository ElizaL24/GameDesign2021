#Eliza Lamster
#6/14/2021
#Today we are learning about files

import os
import sys
import time

#using time to pause your games
os.system('cls')
print("World")

file="asdFre.txt"
FILE=open(file, 'r')
content=FILE.read()
print(content)
newline="\n hello"
content_List=FILE.readlines()
print(content_List)
FILE.close()

