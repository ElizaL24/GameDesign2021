#Eliza Lamster
#6/14/2021
#Today we are learning about files

import os
import sys
import time

#using time to pause your games

print("Hello")
time.sleep(2)
os.system('cls')
print("World")

file=input("What is the name of this file?")
def readFile():
    #makes sure the file exists
    if os.path.exists(file):
        #opening the file
        PEN=open(file, 'r')
        #printing the file
        print(PEN.read())
        PEN.close()
    else:
        print("thank you")
readFile()

fileName="ElizaGame.txt"
if os.path.exists(fileName):
    print("Sorry, that file already exists.")
else:
    FILE=open(fileName, 'w')
    FILE.write("***This is Eliza's file***")
    FILE.close()
    time.sleep(1)
    FILE=open(fileName, 'r')
    print(FILE.read())
FILE=open("ElizaGame.txt", 'a')
newline="\n whatever"
FILE.write(newline)
FILE.close()