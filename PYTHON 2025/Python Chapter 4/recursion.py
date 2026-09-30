"""
Characteristics of Recursive Functions

What is Recursion??
    -> 
          
    Factorial of n  = n!
                    = n * n-1 * n-2 * n-3 ...... * 1

            (n-1)!  = n-1 * n-2 * n-3 ...... * 1
            
            THEN,
            
                n!  = n * (n-1)!
"""


'''
if n! -> is a problem
then (n-1)! ->  is a sub problem
'''


'''
def  recurse(): 
    ...         # Recursive call
    recurse()
    ...
recurse()
'''


def factorial(n=3):
    if n == 0: # Base case
        return 1
    ans =  n * factorial(n-1) # Recursive case
    return ans
print(factorial())

print("=====================")

def fact(n):
    
    # base case
    if n == 0:
        return 1
    
    # Recursive case
    ans = n  * fact(n - 1)
    return ans

n = int(input("Enter n: "))
print(fact(n))
print("=====================")
