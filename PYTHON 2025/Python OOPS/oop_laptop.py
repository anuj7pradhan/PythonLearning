# class Laptop:
#     def __init__(self,id,name,ram) -> None:
#        self.id = id
#        self.name = name
#        self.ram = ram
#     def get_info(self):
#         return f"Laptop id is {self.id}, Name is {self.name} and RAM is {self.ram}"
#     def is_passed(self):
#         if self.ram>=8:
#             return True
#         else:
#             return False
    
#     l1 = Laptop(id = 1001,name = "Anuj", ram = "8gb")
#     print(l1.get_info())


class Laptop:
    def __init__(self,id,name,ram) -> None:
       self.id = id
       self.name = name
       self.ram = ram
    def get_info(self):
        return f"Laptop id is {self.id}, Name is {self.name} and RAM is {self.ram}"
    def is_passed(self):
        if self.grade >=60:
            return True
        else:
            return False
        
        
# Object

l1 = Laptop(id = 1001,name = "Anuj", ram = "8gb")
print(l1.get_info())
