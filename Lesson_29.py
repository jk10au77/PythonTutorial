""" 
    class variables:
    ----------------
    a.  Class variable is a property which exists in just one copy
    b.  It is stored outside any object.
    
    Note:   
    ----
        a.  No instance variable exists if there is no object; a class variable exists in one copy even if there is no 
            objects in the class.
        b. Class variables are created differently to their instance variables.
"""
class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1
    
example_object_1 = ExampleClass(1)
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(3)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

"""
    Observations:
        a.  There is an assignment in the first line of the class definition - it sets the variable named counter to 0; 
            initializing the variable inside the class but outside any of its methods makes the variable a class variable;
        b.  accessing such a variable looks the same as accessing any instance attribute - you can see it in the 
            constructor body; as you can see, the constructor increments the variable by one; in effect, the variable 
            counts all the created objects.
        c.  class variables aren't shown in an object's __dict__ (this is natural as class variables aren't parts of an 
            object) but you can always try to look into the variable of the same name, but at the class level - we'll 
            show you this very soon;
        d. class variable always presents the same value in all class instances (objects)
"""