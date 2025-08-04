tup = ([5, 6], [6, 7, 8, 9], [3])
li = []
for sublist in tup:
    for item in sublist:
        li.append(item)
res = tuple(li)
print(res)