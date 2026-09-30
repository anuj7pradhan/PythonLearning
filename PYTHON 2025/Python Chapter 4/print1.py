# 1. Write a program to print numbers from n to 1.

def print_n_to_1(n):

#   Base Case
    if n == 0:
        return
    print(n)

#    recursive case
    print_n_to_1(n-1)
print_n_to_1(7)

print('===================')

# 2. Write a program to print numbers from 1 to n.
def print_n_to_1(n):

#   Base Case
    if n == 0:
        return
    #print(n)

#    recursive case
    print_n_to_1(n-1)
    print(n)
print_n_to_1(7)

# Write a program to print  sum from 1 to n.

def sum_n(n):
    #Base case
    if n == 1:
        return 1
    # Recursive case
    ans = n + sum_n(n-1)
    return ans
n = int(input("Enter n: "))
print("The sum is",sum_n(n))

# 4. Make a function which calculates the factorial of n using recursion.

def recursion_fact(n):
    #Base case
    if n == 0:
        return 1
    
    #Recursive case
    ans = n * recursion_fact(n-1)
    return ans
n = int(input("Enter n: "))
print(recursion_fact(n))


# 5. Make a function which calculates 'a' raised to the power 'b' using rscursion.

def power(a,b):
    # Base case
    if b==0:
        return 1
    #Recursive case
    ans = a * power(a,b-1)
    return ans
a = int(input("enter a: "))
b = int(input("enter b: "))
print(power(a,b))

# 6. Make a function which calculates Fibonacci sequence using recursion.
# 0 1 1 2 3 5 8 13

def fibonacci(n):
    # Base case
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Recursive case
        return(fibonacci(n-1)+fibonacci(n-2))
n = int(input("Enter n: "))
print(fibonacci(n))

print("===============")

def fibonacci(n):
    # Base case
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Recursive case
        return(fibonacci(n-1)+fibonacci(n-2))
n = int(input("Enter n: "))
for i in range(1,n+1):
    print(fibonacci(i))


# 8:49:33 FINISH