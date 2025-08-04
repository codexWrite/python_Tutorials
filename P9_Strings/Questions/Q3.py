s = "geeksforgeeks"

seen = set() # track unique characters
res = ""     # result string

for char in s:
    if char not in seen:
        seen.add(char)
        res += char
print(res)