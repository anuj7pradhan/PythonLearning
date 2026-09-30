# __inti__ function
# Constructor
# All classes have a function called __init__(), which is always executed when the object is being initiated.

# Creating calss:

class Student:
    def __init__(self,fullname):
        self.name = fullname
        
# Creating object:

s1 = Student("Anuj")
print(s1.name)