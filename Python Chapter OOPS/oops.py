class Student:
    
    def set_name(self,name):
        self.name = name
        
    def get_name(self):
        return self.name
    
student1 = Student()
student1.set_name("Anuj")
print(student1.get_name())
#  10:21:38

student2 = Student()
student2.set_name("Anjal")
print(student2.get_name())