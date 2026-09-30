def hello(): #Making the functions
    print("Hello Hello") #Print the functions
hello() #Calling the functions

# Positional arguments, pass as many as argumments, Here, we provide 4 arguments and their respective values too
def add(n1,n2,n3,n4):
    sum = n1 + n2 +n3 + n4
    return sum
print(add(23,2,12,456))

# Keyword arguments ( i.e the named arguments)
print(add(n1=12,n2=23,n3=2,n4=23))

#Default arguments, default value should be provided at the end of the arguments,here the default is n2 = 10
def add(n1,n2=10):
    sum = n1 + n2
    return sum
print(add(23))