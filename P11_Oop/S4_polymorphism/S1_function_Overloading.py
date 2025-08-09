class arithmetic:
    def add(self, a: int, b: int) -> int:
        return a + b

    def add(self, a: float, b: float) -> float:
        return a + b

    def add(self, a: str, b: str) -> str:
        return a + b

a = arithmetic()
# Testing the add method with different types
print(a.add(5, 10))          # Integer addition
print(a.add(5.5, 10.2))      # Float addition
print(a.add("Hello, ", "World!"))  # String concatenation