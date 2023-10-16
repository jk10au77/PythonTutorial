"""
    Multiple Inheritance in Python:
    -------------------------------
        a.  Multiple inheritance occurs when a class has more than one super class.
        b.  Multiple inheritance is presented as a comma-separated list of superclasses put inside 
            parentheses after the new class name
    The below code snippet illustrates the multiple inheritance
    ------------------------------------------------------------
    The Sub class has two superclasses: SuperA and SuperB. This means that the Sub class inherits all the 
    goods offered by both SuperA and SuperB.
"""

class SuperA:
    var_a = 10
    
    def fun_a(self):
        return 11

class SuperB:
    var_b = 20

    def fun_b(self):
        return 21

class Sub(SuperA, SuperB):
    pass

obj = Sub()

print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())