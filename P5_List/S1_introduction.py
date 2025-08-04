# Creating a Python list with different data types
a = [10, 20, "GfG", 40, True]
print(a)

# Accessing elements using indexing
print(a[0])  # 10
print(a[1])  # 20
print(a[2])  # "GfG"
print(a[3])  # 40
print(a[4])  # True

# Checking types of elements
print(type(a[2]))  # str
print(type(a[4]))  # bool
print(a)

# Iterating over the list
print("Printing List : ")
for item in a:
    print(item)

# Slicing
li = [1,2,3,4,5,6]
print(li[1:3])
print(li[:3])
print(li[2:])
