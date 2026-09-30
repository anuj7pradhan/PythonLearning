'''
Operators
- arithematic
- assignment
- comparision
- logical
- identity
- membership
- bitwise
'''

'''
+, - , *,  /,  %,  **, //
'''
#Arithematic Operators
print("Sum: ",4 + 3)
print("difference: ",4 - 3)
print("product:  ",4 * 3)
print("division: ",4 / 3)
print("Floor division: ", 4//3)
print("Remainder: ",4 % 3)
print("Exponential: ", 4 ** 3)

'''
Assignment operators
=   Assignment operator
+=  n2 += n1 means  n2 = n2 + n1 
-=  n2 -= n1 means  n2 = n2 - n1 
*=  n2 *= n1 means  n2 = n2 * n1 
/=  n2 /= n1 means  n2 = n2 / n1 
%=  n2 %= n1 means  n2 = n2 % n1 
//= n2 //= n1 means  n2 = n2 // n1 
**= n2 **= n1 means  n2 = n2 ** n1 
&=  n2 &= n1 means  n2 = n2 & n1 
|=  n2 |= n1 means  n2 = n2 | n1 
^=  n2 ^= n1 means  n2 = n2 ^ n1 
>>= n2 >>= n1 means  n2 = n2>>+ n1 
<<= n2 <<= n1 means  n2 = n2 << n1 
'''
#Assignment Operators

n1 = 4
n2 = n1
print(n1, n2)
n2 += n1
print("n2 += n1: ",n1,n2)
n2 -= n1
print("n2 -= n1: ",n1,n2)

n2 *= n1
print(n1,n2)
n2 /= n1
print(n1,n2)
n2 %= n1
print(n1,n2)
n2 //= n1
print(n1,n2)
n2 **= n1
print(n1,n2)
'''n2 &= n1
print(n1,n2)
n2 |= n1
print(n1,n2)
n2 ^= n1
print(n1,n2)
n2 >>= n1
print(n1,n2)
n2 <<= n1
print(n1,n2)
'''

#Comparision Operators
# ==,!=,>,<,>=,<=

a1 = 4
a2 = 2
print("a1 is greater tha a2:",a1 > a2)

# Logical Operator

# and - Returns True if both statements are true
# or - Returns True if One of the statement is true
# not - Reverse the result, returns False if the result is True

print("=======")

exp1 = 21 > 10
exp2 = 51 < 14

print("exp1 and exp2:", exp1 and exp2)
print("exp1 or exp2:", exp1 or exp2)
print("not exp1:", not(exp1))
print("=======")

# IDENTITY OPERATORS

# is
# is not

x = 4
y =4
print("If x is y:", x is y)
print("If x is not y:", x is not y)

print("=======")
# Membership Operators
#in
#not in
fruits = ["apple","banana","orange"]
print("If banana is present in fruits:", "banana" in fruits)

print("If papaya is not present in fruits:", "papaya" not in fruits)
print("=======")

#Bitwise Operators
# & = AND
# | = OR
# ^ = XOR
# ~ = NOT
# << = Zero fill left shift
# > = Signed right shift

a = 5
b = 3
print(" a & b: ", a & b)
print(" a | b: ", a | b)
print(" a xor b: ", a ^ b)

# Operators Precedence
# BODMAS rules
# () / * + -

# Order of precedence
# (), **, {/,//}, *, +, -, %

print("Solve it: ",3+2**4/2*5-8//2)
