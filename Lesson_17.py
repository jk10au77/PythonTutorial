"""
        -----------------------------------------------
                Functions and Scope
        -----------------------------------------------
        a. The scope of a name (e.g., a variable name) is the part of a code where the name is properly recognizable.
  """
"""
# The program will fail when run. The error message will read:
# NameError: name 'x' is not defined
def scopeTest():
    x = 123

scopeTest()
print(x)
"""
# Example_1
def my_function():
    print("Do I know that variable?", var)  # a variable existing outside a function has a scope inside the functions' bodies.


var = 1
my_function()
print(var)

# Example_2
var = 2

def mult_by_var(x):
    return x * var
print(mult_by_var(7))

# Example_3

a = 1

def fun():
    a = 2
    print(a)

fun()
print(a)

# Example_4
a = 1
def fun():
    global a
    a = 2
    print(a)

fun()
a = 3
print(a)

"""
    We are given three numbers. We are required to determine whether these numbers form a triangle or not

"""

def is_a_triangle(a, b, c):
    if (a + b <= c ) or (b + c <= a) or (c + a <= b):
        return False
    else:
        return True
    

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))