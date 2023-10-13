"""
    Let's summarize all the facts regarding the use of methods in Python:
        a.  method is a function embedded inside a class. 
        b.  One essential requirement - a method is obliged to have atleast one parameter. i.e there are no such 
            thing as parameterless methods - a method may be invoked without an argument, but not declared without 
            parameters). The first (or only) parameter is usually named self
        c.  The 'self' identifies the object for which the method is invoked.
        d.  if you're going to invoke a method, you mustn't pass the argument for the self parameter - Python will 
            set it for you.
        e.  If you want the method to accept parameters other than self, you should:
            i.  place them after self in the method's definition;
            ii. deliver them during invocation without specifying self (as previously)
        f.  The self parameter is used to obtain access to the object's instance and class variables.
"""
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)

obj = Classy()
obj.var = 3

print(obj.method())

"""
    Methods in detail:
    ------------------
    The constructor: __init__(): The constructor is
    -----------------------------
        a.  obliged to have the self parameter 
        b.  may have or may not have more parameters. 
        c.  can be used to set up the object, i.e., properly initialize its internal state, create instance variables, 
            instantiate any other objects if their existence is needed, etc.
        
    Note:   The constructor 
                a.  cannot return a value.
                b.  cannot be invoked directly either from the object or from inside the class.
"""
class Classy:
    def __init__(self, value):
        self.var = value

obj_1 = Classy("object")
print(obj_1.var)

"""
    Everything about the property name mangling applies to method names also. A method whose name starts with __ is 
    partially hidden.
"""       
class Classy:
    def visible(self):
        print("visible.")
    
    def __hidden(self):
        print("hidden.")

obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("Invisible")

obj._Classy__hidden()

"""
    The inner life cycle of classes and objects:
    --------------------------------------------
    Each Python class and each Python object is pre-equipped with a set of useful attributes which can be used to 
    examine its capabilities.
    We already know one of these - it's __dict__ property
"""
class Classy:
    varia = 1
    def __init__(self):
        self.var = 2
    
    def method(self):
        pass

    def __hidden(self):
        pass
print("The start of inner life cycle of objects.")
obj = Classy()
print("The end of inner life cycle of class object.")
for i in range(len(obj.__dict__)):
    print(obj.__dict__, '\n')
print("The end of inner life cycle of class objects.")
print("The start of inner life cycle of classes.")
for i in range(len(Classy.__dict__)):
    print(Classy.__dict__, '\n')
print("The end of inner life cycle of classes.")

"""
    The __name__ property is another built-in property and is a string.
    ------------------------------------------------------------------
    a. It exists only inside classes. and is absent from the object.
    b. If you want to find class of a particular object, you can use type() 

"""

class Classy:
    pass

print(Classy.__name__)
obj = Classy()
print(type(obj))
print(type(obj).__name__)

"""
    a.  The __module__ is also a string.
    b.  The __module__ contains the module name which contains the definition of the class.
"""
class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)

"""
    The __bases__ property:
    ------------------------
        a. It is a tuple.

"""