"""
    Overriding in Single Inheritance :
    ---------------------------
        a.  Both, Level1 and Level2 classes define a method named fun() and a property named var.
        b.  The entity defined later (in the inheritance sense) overrides the same entity defined earlier.
        c.  Python looks for an entity from bottom to top.

"""
class Level1:
    var = 100

    def fun(self):
        return 101
    

class Level2(Level1):
    var = 200

    def fun(self):
        return 201
    
class Level3(Level2):
    pass

obj = Level3()
print(obj.var, obj.fun())

"""
    Overriding in multiple Inheritance:
    ------------------------------------
        a.  In other words, what should you expect when a class emerges using multiple inheritance?
    
    In the below code snippet, The Sub class inherits goods from two superclasses, Left and Right

"""

class Left:
    var = "L"
    var_left = "LL"

    def fun(self):
        return "Left"
    
class Right:
    var = "R"
    var_right = "RR"

    def fun(self):
        return "Right"
    
class Sub(Left, Right):
    pass

obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())

"""
    Python looks for object components in the following order:
        a. inside the object itself
        b.  in its superclasses from bottom to top
        c.  if there is more than one class on a particular inheritance path, Python scans them from left 
            to right.
"""

class Sub1(Right, Left):
    pass

obj = Sub1()
print(obj.var, obj.var_left, obj.var_right, obj.fun())

class One:
    def do_it(self):
        print("Do it from One")

    def doanything(self):
        self.do_it()

class Two(One):
    def do_it(self):
        print("Do it from Two")

one = One()
two = Two()

one.doanything()
two.doanything()
