# Conditionals and Loops

# Control Statements

# They allow us to control the flow of our programs.

'''
Conditional Statements

1. if, if-else, elif
2. nested
3. Else if ladder
4. Ternary
5. switch

'''

'''

if condition:
    //Statement 1
else:
    //Statement 2
    
'''

raining = False
if raining == True:
    print("Take Umbrella")
else:
    print("Do not take umbrella")

print("==============")

number = int(input("Enter a number:"))
if number % 2 == 0:
    print("The number is positive")
else:
    print("The number is negative")

print("==============")

# Question: Take positive integer input and tell if it is even or odd.

num = int(input("Enter a positive number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

'''

if condition 1:
    //Statement 1

elif condition 2:
    //Statement 2

else:
    //Statement 3
    
'''

'''
If cost price and selling price of an item is input through the keyboard, 
write a program to determine whether the seller has made profit or 
incurred loss or no profit no loss. 
And determine how much profit he made or loss he incurred.
'''

cost_price = int(input("Enter the cost price: "))
sell_price = int(input("Enter the selling price: "))

# if sp > cp -> profit
if sell_price > cost_price:
    profit = sell_price - cost_price
    print("The seller made a profit of Rs.", profit)

# if cp > sp -> loss
elif sell_price < cost_price:
    loss = cost_price - sell_price
    print("The seller made a loss of Rs.",loss)

# cp = sp
else:
    print("The seller made no profit no loss.")

'''
Take input percentage ofa student and print the Grade according to marks:
a. 81 - 100 Very Good
b. 61 - 80 Good
c. 41 - 60 Average
d. <= 40 Fail 
'''

percentage = float(input("Enter percentage: "))

'''
if 81 >= percentage <= 100:
    print("Very Good")
elif 61 >= percentage <= 80:
    print("Good")
elif 41 >= percentage <= 60:
    print("Average")
else:
    print("Fail")
'''

if percentage > 80:
        print("Very Good")
elif percentage > 60:
        print("Good")
elif percentage > 40:
         print("Average")
else:
     print("Fail")