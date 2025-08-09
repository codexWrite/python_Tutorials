class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

d = Dog("Buddy", "Golden Retriever", 5)
print(d.name)  # Accessing public attribute
print(d._breed)  # Accessing protected attribute
# Accessing private attribute will raise an error
print(d.__age)  # Uncommenting this line will raise an AttributeError