#string
name = "Anuj"
print(type(name))

# integer
roll_num = 12
print(type(roll_num))

#floating number
percentage = 98.22
print(type(percentage))

# boolean
is_student = True
print(type(is_student))

print(name,roll_num,percentage,is_student)

#variable is updated
percentage = 88
print(name,roll_num,percentage,is_student)

print("My name is", name,"and my roll number is",roll_num)
#  can only concatenate str (not int)
print("<y name is"+ name+ "My roll number is",roll_num)
# printing using f
print(f"My name is {name}, and my roll number is {roll_num} and i scored {percentage} in exam")

# print with seperator
print(name,roll_num,percentage,is_student,sep="-")

x=1
y=2
z=3
print(x,y,z,sep="->")