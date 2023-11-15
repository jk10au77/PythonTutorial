"""
    In Python, functions are first class objects which means that functions in python can be used or passed as an 
    arguments.

    Properties of first class functions:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    a.  A function is an instance of the Object type.
    b.  We can store the function in a variable.
    c.  We can pass function as a parameter to another function.
    d.  we return the function from a function.
    e.  We can store function in datastructures such as lists, hash tables, 

"""

def parent():
    print("Printing from the parent() function")

    def first_child():
        print("printing from the first_child() function")
    
    def second_child():
        print("printing from the second_child) function")
    
    second_child()
    first_child()

parent()

# Returning functions from functions

def parent(num):
    def first_child():
        return "Hi, I am Emma"
    
    def second_child():
        return "Call me Liam"
    
    if num == 1:
        return first_child
    else:
        return second_child

var_1 = parent(1)
var_2 = parent(2)

print(var_1)
print(var_2)