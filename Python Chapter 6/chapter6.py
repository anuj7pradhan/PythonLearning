#Chapter 6

# ------------- String -------------
# 1. Basics
# 2. Slicing
# 3. Modifying
# 4. Concentration
# 5. Format
# 6. Escape Character


#  Creating Strings

name1 = "Anuj"
name2 = "Hello Dear"
name3 ='''Boomerang  
Sept8''' #Use just single triple coats
print(name1,name2,name3)

print(type(name1))
print(type(name2))
print(type(name3))

# insdexing in a strings
#  Array-like indexing in strings
text = "Hello,  World!!!"

print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])

#  Negative indexing
print(text[-1])
print(text[-4])

print("=======================")
print("Using for loop")

for i in name1:
    print(i)

print("Using list comprehension")
list =  [char for char in name1]
for i in list:
    print(i)
    
# Find  the length of a string
print("Find  the length of a string")
print(len("Blablablablabla"))

# Find a char/substring in a string
print("Find a char/substring in a string")

#  find function  just  give the firstindex of a string
print(name3.find('o'))

# If a char is not present in the string then it returns -1
print("If a char is not present in the string then it give -1")
print(name3.find('c'))