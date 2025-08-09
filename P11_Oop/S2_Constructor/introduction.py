class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age): # parameterize constructor
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
    def __init__(self): # default constructor
       """default constructor"""
       self.name = "Ruby"
       self.age = 7 

dog = Dog()
print(f"Name = {dog.name} \nAge = {dog.age}")