class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name : {self.name}\nAge : {self.age}")

class student(person):
    """child class form person"""

s = student("rohit",22)
s.display()