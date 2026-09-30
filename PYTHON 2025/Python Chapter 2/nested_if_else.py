# Find the greatest of three numbers

n1 = int(input("Enter first positive number: "))
n2 = int(input("Enter second positive number: "))
n3 = int(input("Enter third positive number: "))

if n1 > n2:
    #either n1 or n3 is greatest
    if n1 > n3:
        print(n1," is the greatest")
    else:
        print(n3,"is greatest")
else:
    #either n2 or n3 is greatest
    if n2 > n3:
        print(n2,"is greatest")
    else:
        print(n3,"is greatest")



#Take a positive integer input and tell it is divisible by 5 or 3 but not divisible by 15

num = int(input("Enter a positive integer:"))

# Checking whether it is divisible by 15
if num % 15 == 0:
    print("The number is divisible by 15.")

else:
    # Checking if divisible by 3 or 5
    if num % 3 == 0 or num % 5 == 0:
        print("The number is not divisible by 15 but divisible by 3 or 5.")
    else:
        print("The number is neither divisible by 3 nor by 5.")