# Try this
# Write a Python class named Rectangle to represent a rectangle shape.
# The class should have the following functionalities:
    # A method named set_dimensions that takes two parameters width and height and sets the attributes of the rectangle object accordingly.
    # A method named area that calculates and returns the area of the rectangle
    # A method named perimeter that calculates and returns the perimeter of the rectanngle
# Use this to create objects of the class and print the width, height, area, and perimeter.

class Rectangle:
    def set_dimension(self, height, width):
        self.height = height
        self.width = width
        
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)
    
# Creating objects
rectangle1 = Rectangle()
rectangle1.set_dimension(int(input("Enter num1.")),5)

# Printing the output
print("The height and width area: ", rectangle1.height, ",",rectangle1.width)
print("The area of the give height and width is",rectangle1.area())
print("The perimeter of the give height and width is", rectangle1.perimeter())