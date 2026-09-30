# Tuples
    # -> It is used to store multiple items in a variable
    # 
# Tuple Items
    # Ordered
    # Immutable
    # Duplicates allowed
    # Any datatypes
    # Mix of different data types

# Creating a tuple
colours = ("blue","green","red","black","orange")
print(len(colours)) # counting the tuple size

# Creating a tuple with 1 item, Comma is mandatory in tuple
fruit = ("Mango",)

# Check type of tuple
print(type(fruit))
fruit = tuple(("apple"))
print(type(fruit))

#Accessing items in tuple
print(colours[3]) # This is positive indexing
print(colours[-1]) # This is negative indexing

print(colours[1:3]) # This is range indexing in positive indexing
print(colours[-3:-1]) # This is range indexing in negative indexing

# check if an item exists in tuple
if "black" in colours:
    print("Black is a part of tuple")

#Traverse the tuple

for i in colours:
    print(i)

#Concatinate 2 tuples

more_colours = ("purple","shimrik")
colours = colours + more_colours
print(colours)

# Unpacking a tuple
colour1, colour2, colour3,colour4,colour5,colour6,colour7 = colours
print(colour1, colour2, colour3,colour4,colour5,colour6,colour7)
