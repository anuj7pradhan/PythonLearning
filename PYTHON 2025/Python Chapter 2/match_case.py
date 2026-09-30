# Match Case

# Make a calculator to match the cases:

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Select one of these operator: +, -, *, /")
operator = input("Enter the operator: ")

match operator:
    case "+":
        print("The sum of two numbers is ", num1 + num2)
    case "-":
        print("The difference between two numbers is ", num1 - num2)
    case "*":
        print("The multiple of two numbers is ", num1 * num2)
    case "/":
        print("The division is ", num1 / num2)
    case _ :
        print("Enter the valid operator")