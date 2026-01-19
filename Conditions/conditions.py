# Conditions in Python are used to perform different actions based on different conditions.
#Python supports the usual logical conditions from mathematics: equals: a == b
#not equals: a != b 
#greater than: a > b
#less than: a < b
#greater than or equal to: a >= b
#less than or equal to: a <= b
a=33
b=200   
if b > a:
    print("b is greater than a")
#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition"
elif a == b:
    print("a and b are equal")      
#The else keyword catches anything which isn't caught by the preceding conditions
else:
    print("a is greater than b")
    
#checking number is potoive, negative or zero
num=int(input("Enter a number: "))
if num > 0: 
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")    
