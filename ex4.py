

def largest(a,b,c):
    if (a>b) and (a>c) :
        return a
    elif (b>a) and (b>c) :
        return b
    else:
        return c
    
a = float(input("Pls enter the first number "))
b = float(input("Pls enter the second number ")) 
c = float(input("Pls enter the third number "))

larg = largest(a,b,c)
print(larg, 'is LARGEST')