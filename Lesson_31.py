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