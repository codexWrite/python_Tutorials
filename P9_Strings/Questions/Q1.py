str = "dad"
li = list(str)
li.reverse()
if str == ''.join(li):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
