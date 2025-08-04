# function 1 : no argument no return. 
def add():
    n = 12
    m = 12
    print(f"Sum : {n + m}")

add()

# function 2 : with argument with return 
def add(n,m):
    return n + m

print(f"Sum with function 2 : {add(12,34)}")

# function 3 : with argument no return
def add(n,m):
    print(f"Sum in function 3 : {n+m}")

add(78,67)

# function 4 : no argument with return
def Pi():
    return 3.14

print(f"PI value : {Pi()}")
