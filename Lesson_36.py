"""
    How Python finds properties and methods: i.e. How Python deals with inheriting methods.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Note: As there is no __str__() method within the Sub class, the printed string is to be produced 
    within the Super class. This means that the __str__() method has been inherited by the Sub class.
"""
"""
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My Name is " + self.name + "."
    
class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)

obj = Sub("Jaya")
print(obj)
"""
"""
    Note:
    ------
        a.  The super() function creates a context in which you don't have to (moreover, you mustn't) pass 
            the self argument to the method being invoked - this is why it's possible to activate the 
            superclass constructor using only one argument.
        b.  you can use this mechanism not only to invoke the superclass constructor, but also to get access 
            to any of the resources available inside the superclass.

"""

"""
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")

print(obj)
"""

"""
    In the below code snippet, the Super class defines one class variable named supVar, and the Sub class 
    defines another class variable called subVar
    Both these class variables are visible inside the object of class Sub
"""
"""
class Super:
    supVar = 1

class Sub(Super):
    subVar = 2

obj = Sub()

print(obj.subVar, obj.supVar)
"""

"""
    How Python finds properties and methods:
"""
"""
class Super:
    def __init__(self):
        self.supVar = 1

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 2

obj = Sub()
print(obj.subVar)
print(obj.supVar)
"""

"""
    General statement describing Python's behaviour:
    ------------------------------------------------
    When you try to access any object's entity, Python will try to (in this order):

        a.  find it inside the object itself;
        b.  find it in all classes involved in the object's inheritance line from bottom to top;
    If both of the above fail, an exception (AttributeError) is raised.
    Observe the below code 

    Note: 
    ------
        a.  All the comments we've made so far are related to single inheritance, when a subclass has exactly 
            one superclass. This is the most common situation (and the recommended one, too).
"""

class Level_1:
    variable_1 = 100
    
    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102

class Level_2(Level_1):
    variable_2 = 200
    
    def __init__(self):
        super().__init__()
        self.var_2 = 201

    def fun_2(self):
        return 202


class Level_3(Level_2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301
    
    def fun_3(self):
        return 302
    
obj = Level_3()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())