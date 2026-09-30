# Given a dictionary in the python , write a python program to find the sum of all items in the dictionary.
"""
input:{'a':100,'b':200,'c':300}
output: 600

input:{'x':25,'y':18,'z':45}
output: 88
"""

dic1 = {
    'a':100,
    'b':200,
    'c':300
    }
print(dic1)

print(sum(dic1.values()))

dic2 ={
    'x':25,
    'y':18,
    'z':45
    }
print(dic2.values())
print(sum(dic2.values()))

"""
Given a string and a number N, we need to mirror the characters from the N-th position upto the length of the string in alphabetical order. In mirror operation, we change'a' to 'z','b' to 'y',and so on.
Input:  N = 3
        paradox
Output: paizwlc

Input:  N = 6
        pneumonia
Output: pneumlmrz
"""

input_string = input("Enter string:")
n = int(input("Enter n: "))

# Creating dictionary for mirror operation
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1] # [start:end:step]
print(reverse_alphabets)
dict1 = dict(zip(alphabets,reverse_alphabets))

# Finding the part of string on which we will do mirror operation
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

# Finding the mirror string
mirror = ""
for i in range(0,len(suffix)):
    mirror = mirror + dict1[suffix[i]]

# Creating the final string
result = prefix + mirror
print("The result is: ", result)