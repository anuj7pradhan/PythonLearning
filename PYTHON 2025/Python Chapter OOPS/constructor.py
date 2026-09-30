# class Constructor
    # Special function that gets invoked every time an object is created for that class

# Syntax:
# class ClassName:
# def __inti__(self,parameter1,parameter2,...):
    # initialize instance variables (attributes) here
    
    
class Rectangle:
    def __init__(self, height, width):
        print(f"A rectangle is created with the height: {height} and width: {width}")
       
        self.height = height
        self.width = width
        
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)
    
# Creating objects
rectangle1 = Rectangle(8,5)
rectangle2 = Rectangle(3,5)
rectangle3 = Rectangle(4,6)
