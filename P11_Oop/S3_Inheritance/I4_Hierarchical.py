class person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def display(self):
        return f"Person: {self.name}\nAge: {self.age}"
    
class student(person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display(self):
        return f"{super().display()}\nStudent ID: {self.student_id}"

class teacher(person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        return f"{super().display()}\nSubject: {self.subject}"

s = student("Alice", 20, "S12345")
t = teacher("Bob", 40, "Mathematics")
print(s.display())
print(t.display())