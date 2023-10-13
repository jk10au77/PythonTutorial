"""
    In general, a class can be equipped with two different kinds of data to form a class's properties.
        a. Instance variable:   Data or properties defined inside the __init__() (i.e a constructor). 
        b. Class variable:      Data or properties defined out side the constructor.

    Instance variable: Instance variables are closely connected to the objects (which are class instance).
    -----------------
    Instance variables are closely connected to the objects (which are class instance). Instance variable are not 
    connected to classes themselves.
    a.  If the value of a variable varies from object to object, then such variable are called instance variables.
    b.  For every object, a seperate copy of the instance variable will be created.
    c.  Instance variables are not shared by by objects.
    d.  Every object has its own copy of the instance attribute. This means that for each object of a class, the 
        instance variable value is different.
    Note:
    -----
    modifying an instance variable of any object has no impact on all the remaining objects. Instance variables 
    are perfectly isolated from each other.
    

    Note:
    ----
    a.  When we create an object, we passed the values to the instance variables using a constructor.
    b.  Each object contains different instance variables because we passed different values to a constructor to 
        initialize an object.
    c.  Variables defined outside the __init__() i.e. constructor belong to class. They are shared by all instances.

    Ways to access Instance variables:
    ----------------------------------
    The instance variables can be accessed in two ways:
        a.  Within the class in instance method by using the Object reference (self)
        b.  Using the getattr() method.

""" 

"""
    Small primer to objects:
    ------------------------
    When an object is created, it posseses
        a.  its own properties, and methods.
        b.  pre-defined properties and methods. These predefined properties and methods are assigned to object by Python 
            itself. 
        c.  One of the predefined variable is __dict__. This variable contains the names and values of all properties
            (variables) of the object currently having.
"""

class ExampleClass:
    def __init__(self, val = 0):
        self.first = val
    
    def set_second(self, val):
        self.second = val

example_object_1 = ExampleClass(1)
example_object_2 =ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print("The instance variables of example_object_1: ", example_object_1.__dict__)
print("The instance variables of example_object_2: ", example_object_2.__dict__)
print("The instance variables of example_object_3: ", example_object_3.__dict__)

