n = int(input("Enter n: "))

sum = 0
for i in range(1,n + 1):
    sum += i
print("The sum of n is: ",sum)

print("=============")

n1 = int(input("Enter n1: "))
sum1 = 0
for i in range(1,n1 + 1):
    sum1 += i
print("The sum of n is: ",sum1)

print("=============")
# Writing a function for calculating sum from 1 to n:


def sumOne_n(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
#Call Function
output = sumOne_n(n)
print("Sum of all number till n is",output)
n1 = int(input("Enter n:"))
output1 = sumOne_n(n)
print("Sum of all number till n is",output1)



# WHAT AND AHY???
# Same process were repeated againn and again
# So we use function
# Functions are the blocks of reusable code that performs a specific tasks.

'''
###   TYPE OF FUNCTIONS
1.  Built-in functions
2.  User defined functions

    Keyword         function_name       parameter
   -> def          -> Function_name    -> (parameters):

    # statement

    Return expression
   -> FUNCTION return

   CALLING A FUNCTIONS
    Syntax:

    function_name(argument_1, argument_2, argument_3 ...)
'''
print("=============")

# Write a function that prints Hello World

#Define function
def hello_world_function():

#body of function
    print("This is print of Hello World Function")

# Calling function
hello_world_function()

print("=============")

"""
Types Of Arguments
1.  Default argument
2.  Keyword arguments(named arguments)
3.  Positional arguments
4.  Arbitary arguments(variable-length arguments * args and **kwargs)

"""

# Function which takes 2 numbers as  input and returns their sum

def add(n1,n2):
    print("n1:",n1)
    print("n2:",n2)
    sum = n1+n2
    return sum
#Positional arguments
print("The sum is:",add(3,4))

print("=============")

def sub(n1,n2):
    print("n1:",n1)
    print("n2:",n2)
    sub = n1 - n2
    return sub
# Keyword argument (Named arguments)
print("The subtraction is:",sub(n2 = 4,n1 = 9))

print("=============")

def mul(n1,n2=5):
    print("n1:",n1)
    print("n2:",n2)
    mul = n1 * n2
    return mul
# Default argument
print("The multiplication is:",mul(9))

# Arbitrary arguments (variable-length arguments *args and **kwargs)

def add_all_num(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum
output = add_all_num(1,2,5,3,2,65,3)
print("The arbitrary sum is:",output)

# Keyworded arguments (**kwargs)
def studentInfo(**kwargs):
    for x , y in kwargs.items():
        print(x,"is",y)
studentInfo(name="Ashu",age="32",city="kathmandu",fab_song="summer of 69'")
studentInfo(name="Aba",age="22",city="Pokhara",fab_song="symphony of destruction")
studentInfo(name="Ruie",age="25",city="Butwal",fab_song="Mayako dorele")
studentInfo(name="Julie",age="20",city="Mustang",fab_song="Sumnima")

print("========================")

def greet(name,dept):
    print(f"Hello {name}")
    print(f"Are you from {dept} department?")

# Positional arguments
# greet("CS","Anuj")
greet("Anuj","CS")

# keyword arguments, Reorder also supports
greet(dept="CS",name="Anuj")

# Positional and Keyword arguments
greet("Anuj",dept="CS")

print("========================")

# Default arguments

# SyntaxError: non-default argument follows default argument
# Provide all the non-default arguments first and lastly provide default argument
# def new_greet(name,subject="Python",dept):

def new_greet(name,dept,subject="Python"):
    print(f"Hi{name}")
    print(f"Are you from {dept} department?")
    print(f"Are you learning {subject}?")
new_greet("Anuj","CS")

# Override the default value
new_greet("Anuj","CS","Java")

print("========================")

# Arbitrary arguments, *args , 
def add(*numbers):
    c=0
    for i in numbers:
        c +=i
    print(f"Sum is {c}")
add(2,3,4,5)
add(1,2,3,4,5,6,7,8,9)

