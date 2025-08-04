tup = (1,2,3,4)
li =[]
for i in tup:
    li.append(i**3)
    print(li)
tup = tuple(li)
print(tup)