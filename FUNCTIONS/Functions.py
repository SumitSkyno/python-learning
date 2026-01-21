#Functions in Python, a block of code which only runs when it is called.
#Function is a "reusable" block of code that performs a specific task.
#basic syntax
"""function name starts with def keyword, followed by the function name and parentheses().
The code block within every function starts with a colon (:) and is indented.
You can pass data, known as parameters, into a function."""

def greet():  #def keyword is used to define a function, followed by the function name and parentheses.(important)
    print("Hello, welcome to the functions module!")
greet()  #Calling the function

#Function with parameters
def greet_user(name):  #name is a parameter
    print("Hello,", name + "!")
    print(f"Welcome to the functions module, {name}!") #Using f-string for formatting
greet_user("Alice")  #Passing argument "Alice" to the function
greet_user("Bob")    #Passing argument "Bob" to the function

#Function with multiple parameters
#If a function doesn't have a return statement, it returns None by default.
def add_numbers(a, b):  #a and b are parameters
    return a + b  #return statement to return the result
result = add_numbers(5, 10)  #Passing arguments 5 and 10 to the function
print("Sum:", result)  #Output: Sum: 15

#Difference between parameters and arguments
#Parameters are the variables listed inside the parentheses in the function definition.
#Arguments are the values that are sent to the function when it is called.
def multiply(x, y):  #x and y are parameters
    return x * y
product = multiply(4, 5)  #4 and 5 are arguments
print("Product:", product)  #Output: Product: 20

#Default parameter value
def greet_person(name="Guest"):  #Default value for name is "Guest"
    print("Hello,", name + "!")
greet_person()  #Using default value
greet_person("Charlie")  #Passing argument "Charlie"

#Keyword arguments
#keyword arguments often called as kwargs, are arguments that are passed to a function by explicitly specifying the parameter name.
def describe_person(name, age):
    print(f"Name: {name}, Age: {age}")
describe_person(age=30, name="David")  #Passing arguments using parameter names

#only positional arguments, only keyword arguments, and mixed arguments
def display_info(city, country):
    print(f"City: {city}, Country: {country}")
#Only positional arguments
display_info("Paris", "France")
#Only keyword arguments
display_info(country="Italy", city="Rome")
#Mixed arguments (positional first, then keyword)
display_info("Berlin", country="Germany")

#using return and /,* in function parameters
def my_function(a, b, /, *, c, d):
  return a + b + c + d
result = my_function(5, 10, c = 15, d = 20)
print("Result:", result)



#Variable scope
#Variables defined inside a function are local to that function and cannot be accessed outside.
def my_function():
    local_variable = "I am local"
    print(local_variable)
my_function()
# print(local_variable)  #This will raise an error because local_variable is not defined outside the function
#Global variable
global_variable = "I am global"
def access_global():
    print(global_variable)  #Accessing global variable inside the function
access_global()
print(global_variable)  #Accessing global variable outside the function


#Function with arbitrary arguments (*args)
def sum_all(*args):  #*args allows for arbitrary number of arguments
    total = 0
    for num in args:
        total += num
    return total
result = sum_all(1, 2, 3, 4, 5)  #Passing multiple arguments
print("Total Sum:", result)  #Output: Total Sum: 15
#Using *args with a greeting function
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")




#Function with arbitrary keyword arguments (**kwargs)
def print_info(**kwargs):  #**kwargs allows for arbitrary keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Eve", age=28, city="New York")  #Passing multiple keyword arguments





