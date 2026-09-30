# Write a python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.


# fact of n = n!
#           = n * n-1 * n-2 ...

# Function for calculating factorial of a number

def factorial(n):
    ans = 1
    if n == 0:
        ans = 1
    else:
        for i in range(1,n+1):
            ans *= i
    return ans


n = int(input("Enter n: "))
output = factorial(n)
print("The factorial is: ", output)


#   1. What will be the poutput of the following????
x = 50
def func(x):
    x=2
func (x)
print("x is now:",x)

#   a. x is now: 50 ........Ans pass by value
#   b. x is now: 2
#   c. x is now: 100
#   d. None

#   2. What will be the poutput of the following????

def say(message, times = 1):
    print(message * times)
say('Hello')
say('World',5)
say('World',15)

#   a. Hello
#       WorldWorldWorldWorldWorld .........Ans
#   b. Hello
#       World 5
#   c. Hello
#       World,World,World,World,World
#   d. Hello
#       HelloHelloHelloHelloHEllo