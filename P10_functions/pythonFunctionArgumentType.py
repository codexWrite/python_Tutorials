# Default argument
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

# keyword argument
def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')

# Arbitrary Keyword  Arguments
    # *args in Python (Non-Keyword Arguments)
def myFun1(*argv):
    for arg in argv:
        print(arg)

myFun1('Hello', 'Welcome', 'to', 'GeeksforGeeks')

    # **kwargs in Python (Keyword Arguments)
def myFun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} == {value}")


myFun(first='Geeks', mid='for', last='Geeks')

