# While Loop
# No. of iterations..
# Runs till the condition is true
# Before every iteration, it checks of consition is still true
i = 1
while i <=  10: #condition
    print("This is while loop",i)
    i+=1

i = 2
while i < 100:
    print(i)
    i += 2

#Predict the output

# ex 1
j = 0
while j <= 10:
    print("This is j",j)
    j = j + 1

# ex 2
x = 1
while x ==1:
    x = x-1
    print("This is x",x)

# ex 3
y = 10
while y ==20: #Condition doesen't meet the initialization
    print("Computer buff!")

# ex 4
x = 4
y = 0
while x >= 0:
    x -= 1
    y += 1
    if x == y:
        continue
    else:
        print("Ex. 4:",x , y)  

# ex 5
x = 4
y = 0
while x >= 0:
    if x == y:
        break
    else:
        print("Ex. 5:",x , y)
    x -= 1
    y += 1

#Let's now solve pattern printing questions.
 # Print the given pattern
'''

for n = 1
*****
For n = 2
*****
*****
For n = 3
*****
*****
*****

'''

'''

rows
columns
what to print

'''

n = int(input("Enter n: "))

for _ in range(n):
    print("*"  * 5)


# Print the given pattern
'''
For n = 4
1234
1234
1234
1234

For
n = 6
123456
123456
123456
123456
123456
123456

'''
n = int(input("Enter n: "))

for i in range(n): #Loop for row
    for j in range(1, n + 1): # Loop for column
        print(j,end="")
    print()

# Print the given pattern

'''
For n = 4
1
12
123
1234
'''

n = int(input("Enter number: "))
for i in range(1,n+1):#Loop for rows
    for j in range(1,i+1):#Loop for columns
        print(j,end="")
    print()
    
# Print for ABCD
n = int(input("Enter Abc num: "))
for i in range(1,n+1):#Loop for rows
    for j in range(1,i+1):#Loop for columns
        print(chr(j + 64), end="")
    print()
  

  # Print the given pattern

'''
   1
  123
 12345
1234567

'''

n = int(input("Enter num: "))
for i in range(1,n+1):
    #print spaces
    print(" " * (n - i),end="")
    
    # printing digits
    for j in range(1,2*i):
        print(j,end="")
    print()


