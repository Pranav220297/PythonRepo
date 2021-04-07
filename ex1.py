'''
Create a program to compare three numbers and find the bigger numbers.
 [topics covered: identified, variable, types, operator, if statement]
 
 '''
 # This is my first program
a = float(input("Pls enter the first number "))

b = float(input("Pls enter the second number ")) 

c = float(input("Pls enter the third number "))

if (a>b) and (a>c) :
    print(a, "is largest")
elif (b>a) and (b>c) :
    print(b, "is largest")
else:
    print(c, "is largest")



 


