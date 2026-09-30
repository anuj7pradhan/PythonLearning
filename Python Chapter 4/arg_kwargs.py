"""
*args           = allows us to pass multiple non-key arguments.
**kwargs        = allows you to pass multiple keyword-arguments.
                * unpacking operator
                1. positional  2. default 3. keyword 4. Arbitrary
"""

def add(a,b):
    return a+b
print(add(1,2))

def add(*args):
    print(type(args))
    total = 0
    for arg in args:
        total +=arg
    return total
print(add(1,2,3,4,5))


def add(*nums):
    print(type(nums))
    total = 0
    for num in nums:
        total +=num
    return total
print(add(1,2,3))

def display_name(*args):
    for arg in args:
        print(arg,end=" ")
display_name("Samba","Ramba","Lammba","Hamba","Kamba")


