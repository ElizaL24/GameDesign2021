#Eliza Lamster
#6/4/2021
#Asking user for base
#input is input()2
print ("hello")
print()
print()
print()
print()
print ("what is the base?")
base=int(input())
print ()
print ("multiplication table for", base)
print ()
for var in range (1,11):
    resolved=base*var
    print (base, " x ", var, " = ", resolved)
print ()
print ("addition table for", base)
print ()
for var in range (1,11):
    print (base, " + ", var, " = ", base+var)
print ()
print ("division table for", base)
print ()
for var in range (1,11):
    print (base, " / ", var, " = ", base/var)
print ()
print ("subtraction table for", base)
print ()
for var in range (1,11):
    print (base, " - ", var, " = ", base-var)
print ()
print ("Thank you and have a great day")

