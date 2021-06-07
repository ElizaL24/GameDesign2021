#Eliza Lamster
#6/7/2021

num1=19
num2=3.5
num3=0x12F293E8294F2873F2735372923F
phrase="Hello There! "
#code below shows the type of data
print(type(phrase))
print(type(num1))
print(type(num2))
print(type(num3))
#below are the functions of a string)
num=len(phrase)
print(num)
print(phrase[3:num-5])
print(phrase[0])
print(phrase[3:6]) #prints from 3 to 5
print(phrase[6:]) #prints from 6 to end
print(phrase *2) #prints it twice

#concadenaation is joining strings
phrase = phrase + "The weather is rainy today"
print(phrase)
line1="rain rain "
line2="go away "
line3="come again some other day"
print(line1+line2)
print(line2+line3)
print(line1+line2+line3)

#the while show you whether something is in the phrase
while "There" in phrase:
    print("There" in phrase)
    phrase="done"  #if the phrase isn't changed, the program will print true forever because of the loop

