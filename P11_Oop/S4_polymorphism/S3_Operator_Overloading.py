class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # This method overloads the '+' operator
    def __add__(self, other):
        if isinstance(other, Vector):
            # If the other object is also a Vector, add their components
            return Vector(self.x + other.x, self.y + other.y)
        else:
            # Otherwise, raise a TypeError
            raise TypeError("unsupported operand type(s) for +: 'Vector' and '{}'".format(type(other).__name__))

# Create two Vector objects
v1 = Vector(2, 3)
v2 = Vector(5, 7)

# Now you can use the '+' operator to add them
v3 = v1 + v2

print(v3)  # Output: Vector(7, 10)