# Python3 code to demonstrate working of
# Extract Unique values dictionary values
# initializing dictionary
test_dict = {'gfg' : [5, 6, 7, 8],
            'is' : [10, 11, 7, 5],
            'best' : [6, 12, 10, 8],
            'for' : [1, 2, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

x=list(test_dict.values())
y=[]
res=[]
for i in x:
    y.extend(i)
for i in y:
    if i not in res:
        res.append(i)
res.sort()

# printing result
print("The unique values list is : " + str(res))