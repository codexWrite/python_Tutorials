# Creating tuples
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 2)
Tuple2 = ('python', 'geek', 'python', 
          'for', 'java', 'python')

# count the appearance of 3
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

# count the appearance of python
res = Tuple2.count('python')
print('Count of Python in Tuple2 is:', res)



# Creating tuples
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)

# getting the index of 3
res = Tuple.index(3)
print('First occurrence of 3 is', res)

# getting the index of 3 after 4th
# index
res = Tuple.index(3, 4)
print('First occurrence of 3 after 4th index is:', res)