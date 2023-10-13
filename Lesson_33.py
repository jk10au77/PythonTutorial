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
       