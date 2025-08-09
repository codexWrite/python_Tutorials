class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name : {self.name}\nAge : {self.age}")

class employee:
    def __init__(self,empid):
        self.empid = empid

class manager(employee, person):
    def __init__(self, empid,name,age):
        person.__init__(self,name,age)
        employee.__init__(self,empid)
    def display(self):
        super().display()
        print(f"ID : {self.empid}")

s = manager(12,"rohit",22)
s.display()