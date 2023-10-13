"""
    class variables : continued
    ------------------------------
    The difference between the '__dict__' variable of class varaible and '__dict__' variable of instance variable
    
"""
class ExampleClass:
    varia = 1

    def __init__(self, val):
        ExampleClass.varia = val
    
print("Contenets of __dict__ variable of class: ", ExampleClass.__dict__)
example_object = ExampleClass(2)

print("Contenets of __dict__ variable of class: ", ExampleClass.__dict__)
print("Contenets of __dict__ variable of object: ", example_object.__dict__)

"""
    checking the existence of attribute.
    -----------------------------------------
    In contrast to other programming languages, you may not expect that all objects of the same class have the same sets 
    of properties. See the below code

"""
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)
