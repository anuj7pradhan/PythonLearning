'''
Pass by reference
Pass by value
    -> immutable on=bjects - strings, integers, float, tuple)
    -> When passed to function, a copy of the object is created and assigned to local variable inn the function
    -> Any change made to them inside function do not affect the original object outside function

Pass by Reference
    -> Mutable object - list, dictionaries
    -> A reference to actual object is passed to functions
    -> Changes inside the functionns will affect the original object.
    '''
# Pass by value
def addOne(x):
    x = x + 1
    print("Inside function:",x)
x = 5
addOne(x)
print("Outside funnction:",x)

print("========================")

# Pass by Reference
def modifyList(list):
    list.append(4)
    list.pop(0)
    print("Inside functions: ",list)
list = [1,2,3]
modifyList(list)
print("Outside functions: ",list)

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

