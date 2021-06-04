#Eliza Lamster
#6/4/2021
#We are going to print a multiplication table for 2
# Using print statement
# input --> variable is a container to keep data
# They need to have a valid and unique name. Will have unique address
base = 2
var2 = 7
print (1 * base)
print (2 * base)
print (3 * base)
print (4 * base)
print (5 * base)
print (6 * base)
print (7 * base)
print (8 * base)
print (9 * base)
print (10 * base)
# repetition implies looping
# when looping until exact number, use for statement
for i in range(1,11):  #beginning of range is included, end isn't
  print(i * base, end= "    ")
base =3
print ()
for i in range(1,11):  #beginning of range is included, end isn't
    print(i * base, end= "    ")
base =4
print ()
print ()
for i in range(1,11):  #beginning of range is included, end isn't
    print(i * base, end= "    ")
print ()
print ()
print ()
# when we have severa; repetitions we can use veral loops
# sometimes they can be nested loops (loop inside a loop)
for var in range (2,11):
    print ("multiplication table for", end=" ")
    print (var)
    for i in range (1,11):
        print (i, end=" ")
        print ("x", end=" ")
        print (var, end=" = ")
        print (i * var, end="   ")
        print ()
    print ()
#commit test

