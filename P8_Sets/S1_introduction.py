"""Python set is an unordered collection of multiple items having different datatypes. In Python, sets are mutable, unindexed and do not contain duplicates. The order of elements in a set is not preserved and can change."""

# Creating a set
my_set = {1, 2, 3, 4, 5}
# Displaying the set
print("Original Set:", my_set)

# using the set constructor
set1 = set("GeeksForGeeks")
print(set1)

set1 = set(["Geeks", "For", "Geeks."])

# Accessing element using For loop
for i in set1:
    print(i, end=" ")