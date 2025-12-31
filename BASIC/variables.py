""" -Python has no command for variables
    -Variables do not need to be declared with any particular type, and can even change type after they have been set
    -If you want to specify the data type of a variable, this can be done with casting.
    -You can get the data type of a variable with the type() function.
    -Variable names are case-sensitive. 
  """

x="Abc"
y="Xyz"
y=5
z=str(7777)
print (x)
print (y)          # y is overridden, now an integer
print (type(z))

"""A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""
""" - Can assign many values to multiple variables
    - Can assign one value to multiple variables """

a,b,c="orange","apple","mango"
print(a)
print(b)
print(c)


i=j=k="Orange"
print(i,j,k)   #In the print() function, you output multiple variables, separated by a comma:


#Unpack a collection 
cars=["BMW","VW","AUDI"]
l, m, n=cars
print(l,m,n)


#In the print() function, you output multiple variables, separated by a comma:but can't do it string and number
d="Python "
e="is "
f="good"
print(d+e+f)


#example
num=88
ch="Sum is:"
print(ch,(num+2))


"""Global Variables
Variables that are created outside of a function are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.

If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, global and with the original value.

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
To change the value of a global variable inside a function, refer to the variable by using the global keyword:
"""

sub="Testing"

def myfunc():
    global sub      #global variable is change inside the fucntion using global keyword
    sub ="QA"   
myfunc()

print(sub)

