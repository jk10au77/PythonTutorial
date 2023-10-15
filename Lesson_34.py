"""         
    Reflection and Introspection:
    ------------------------------
    Introspection:  is the ability of a program to examine the type or properties of an object at runtime
    Reflection:     is the ability of a program to manipulate the values, values, properties and /or functions
                    of an object at runtime.

    What does the above properties mean?
    You don't need to know a complete class/object definition to manipulate the objects because the object and its 
    class contain the metadata allowing you to recognize its features during program execution.                
    """
"""
    Investigting classes:
    ---------------------
    What can you find out about classes in Python? The answer is simple - everything.

    Both Relection and Introspection enable a programmer to do anything with any object, no matter where it comes from.
"""
"""
    The function named incIntsI() gets an object of any class, scans its contents in order to find all integer attributes
    with names starting with i, and increments them by one.
"""

class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

"""
    Exercise_1:
    -----------
    The declaration of the Snake class is given below. Enrich the class with a method named increment(), adding 1 to 
    the victims property.

    class Snake:
    def __init__(self):
        self.victims = 0
    
    Answer:
    -------
    def increment(self):
        self.victims += 1

    Exercise_2:
    -----------
    Redefine the Snake class constructor so that is has a parameter to initialize the victims field with a value passed 
    to the object during construction.
    Answer:
    --------
    class Snake:
        def __init__(self, victims):
            self.victims = victims

    Exercise_3:
    ------------
    predict the output of the following code:

    class Snake:
        pass
    
    class Python(Snake):
        pass
        
    print(Python.__name__, 'is a ', Snake.__name__)                         # Python is a Snake
    print(Python.__bases__[0].__name__, 'can be a ', Python.__name__)       # Snake can be a Python
    

"""