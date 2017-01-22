# https://docs.python.org/3/library/exceptions.html

# Attribute error. Trying to access an attribute that the class doesn't have

class MyClass:
    def __init__(self):
        self.property = 5

x = MyClass()
x.other_property # error

# Import error
# importing a module that doesn't exist

# KeyError
dict = {'x':5, 'y':10}
dict['z'] # error

# RuntimeError

# TypeError
int([])

# ValueError
int("a")

# IOError
# file not found
