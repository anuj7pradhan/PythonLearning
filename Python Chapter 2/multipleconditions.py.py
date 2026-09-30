# Multiple Conditions Using 'and' and 'or'

#Logical operators helps us in combining the result of 2 conditions

eng_marks = int(input("Enter eng marks:"))
math_marks = int(input("Enter math marks:"))

#If both are more than 80, print A Grade
if eng_marks > 80 and math_marks > 80:
    print("A Grade")

# If eitherof marks are morethan80,print B Grade
elif eng_marks > 80 or math_marks > 80:
    print("B Grade")

# if neither of marks are more than 80: 
else:
    print("C Grade")


