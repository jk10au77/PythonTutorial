"""
    Checking an existence of an object's attribute.
    -----------------------------------------------
    In Python,  you may not expect that all objects of the same class have the same sets of properties.
    i.e. Objects of the same class may or may not have the same set of properties.
    Go through the below code

"""
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1  
        else:
            self.b = 1

example_object = ExampleClass(1)
print(example_object.a)
#print(example_object.b)

"""
    On running the above code, you will get an AttributeError and the Traceback is shown below:
    Traceback (most recent call last):
  File ".main.py", line 11, in 
    print(example_object.b)
AttributeError: 'ExampleClass' object has no attribute 'b'

i.e accessing an non-existing object (class) attribute causes an AttributeError exception.

Using the try-except instruction we can avoid the halt of execution.

"""

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1  
        else:
            self.b = 1

example_object = ExampleClass(1)
print(example_object.a)
try:
    print(example_object.b)
except AttributeError:
    print("raised attribute error.")

"""
    There is one more way to check for attribute existence.
    hasattr(): Python function checks the atrribute's existence. It expects two two arguments:
    ------------------------------------------------------------
        a.  The class or the object to be checked
        b.  the attribute whose existence is to be checked.
    The hasattr() function returns True or False based on the attribute's existence.
"""
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1  
        else:
            self.b = 1

example_object = ExampleClass(1)
print(hasattr(example_object, 'a'))
print(hasattr(example_object, 'b'))

"""
    Note:
    -----
    a.  The hasattr() can operate on classes also.
    b.  It can be used to find out if a class varaible is available
    c.  The function returns True if the specified class contains a given attribute, and False otherwise.

"""

class ExampleClass:
    attr = 1


print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))

"""
    Exercise_1: Which of the Python class properties are instance variables and which are class variables? 
                Which of them are private?

   class Python:
    population = 1
    victims = 0
    def __init__(self):
        self.length_ft = 3
        self.__venomous = False


    Exercise_2: Write an expression which checks if the version_2 object contains an instance property named constrictor (yes, constrictor!).

    hasattr(version_2, 'constrictor')


"""
