class grandParent:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name : {self.name}\nAge : {self.age}")

class parent(grandParent):
    def __init__(self, name, age,contact):
        super().__init__(name, age)
        self.contact = contact
    def display(self):
        super().display()
        print(f"Contact : {self.contact}")

class child(parent):
    def __init__(self, name, age, contact,email):
        super().__init__(name, age, contact)
        self.email = email
    def display(self):
        super().display()
        print(f"E-mail : {self.email}")

c = child("John", 30, 1234567890, "john374@gmail.com")
c.display()
