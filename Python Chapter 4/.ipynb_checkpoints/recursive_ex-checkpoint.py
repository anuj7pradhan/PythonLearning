"""Write a  program to print  numbers  from n to 1.
input
n = 5

output
5
4
3
2
1
"""


def funct(n):
    # Base case
    if n ==0:
        return
    print(n)
    # Recursive case
    funct(n - 1)
funct(9)

print("=====================")

def funct(n):
    # Base case
    if n ==0:
        return
    # Recursive case
    funct(n - 1)
    print(n)
funct(9)







