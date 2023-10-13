"""
    Instance Variables - continued:
    ----------------------------------

    Accessing private instance variables from outside the class definition
"""

class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val
    
    def set_second(self, val = 2):
        self.__second = val
    
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_2.set_second = 3

example_object_3 = ExampleClass(4)
example_object_3.__third = 5

print("The instance variables of example_object_1: ", example_object_1.__dict__)
print("The instance variables of example_object_2: ", example_object_2.__dict__)
print("The instance variables of example_object_3: ", example_object_3.__dict__)

"""
    When Python sees that you want to add an instance variable to an object and you're going to do it inside any of 
    the object's methods, it mangles the operation in the following way:

    a.  it puts a class name before your name;
    b.  it puts an additional underscore at the beginning.

    This is why the __first becomes _ExampleClass__first.

The name is now fully accessible from outside the class. You can run a code like this:
    
"""
print("Accessing the private instance variables from outside the class definition using mangling process: ", example_object_1._ExampleClass__first)
