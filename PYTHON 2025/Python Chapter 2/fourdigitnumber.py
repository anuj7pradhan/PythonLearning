#Take a positive integer input and tell it is a four digit number or not.

num = int(input("Enter number: "))

if num >= 1000 and num <= 9999:
    print("It is a four digit number.")
else:
    print("Not a four digit number")


print("====================")

# Take a 3 positive integer input and print the greatest of them

n1 = int(input("Enter first positive number: "))
n2 = int(input("Enter second positive number: "))
n3 = int(input("Enter third positive number: "))

# if n1 is the greatest
if n1 > n2 and n1 > n3:
    print(n1 ,"is greatest.")

# if n2 is the greatest
elif n2 > n1 and n2 > n3:
    print(n2 ,"is greatest.")

# if n3 is the greatest
else:
    print(n3 ,"is greatest")   