class Student:
    def __init__(self,name, grade) -> None:
        self.name = name
        self.grade = grade
    def get_info(self):
        return f"Name is {self.name} and grade is {self.grade}"
    def is_passed(self):
        if self.grade >=60:
            return True
        else:
            return False
        
        
# Object

s1 = Student(name= "Anuj", grade = 8)
s2 = Student(name= "Prati", grade = 58)
s3 = Student(name= "Anjal", grade = 75)

print(s1.get_info())
print(s2.get_info())
print(s3.get_info())