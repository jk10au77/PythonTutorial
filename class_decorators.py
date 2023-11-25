"""
    Class Decorators:
    -------------------
    a.  Class decorators refer to function decorators, because they use the same syntax and implement the same concept.
    b.  Instead of wrapping individual methods with function decorators, class decorators are ways to manage classes or special methods calls
        into additional logic that manages or extends instances that are created.
    c.  class decorators appear just before the 'class' instructions that begin class definition (similar to function decorators, they appear 
        just before the function definitions).
    d.  The simplest example is shown below

        def my_decorator(A):
            function instructions go here


        @my_decorator
        class MyClass:
            class instructions go here
        
        obj = MyClass()        

    e.  Like function decorators, the new (decorated) class is available under the name 'MyClass' and is used to create an instance. 
    f.  The original class named 'MyClass' is no longer available in your name space. The callable object returned by the class decorator 
        creates and returns a new instance of the original class, extended in some way.

"""

# Now let's create a function that will decorate class car with a method that issues alerts whenever the 'mileage' attribute is read.

def object_counter(class_):     # this line defines a decorating function that accepts one parameter 'class_' (note the underscore)
    class_.__getattr__orig = class_.__getattribute__    # the decorator makes a copy of the reference to the __getattribute__ special method. This method is responsible for returning the attribute values. The reference to this original method will be used in a modified method;

    def new_getattr(self, name):  # a definition of the method playing the role of the new __getattribute__ method starts here. This method accepts an attribute name – it’s a string;
        if name == 'mileage':   # in case some code asks for the 'mileage' attribute, the next line will be executed;
            print('We noticed that the mileage attribute was read.')     #  a simple alert is issued;
        return class_.__getattr__orig(self, name)   # the original method __getattribute__ referenced by class.__getattr__orig is called. This ends the 'new_getattr' function definition;

    class_.__getattribute__ = new_getattr   # now the 'new_getattr' is defined, so it can now be referenced as the new '__getattribute__' method by a decorated class;
    return class_   # every well behaved and developed decorator should return the decorated object – in our case it is a decorated class.


# class decorated with function
# creating a simple class car
# each object should own two attributes:    mileage and VIN

@object_counter
class Car:
    def __init__(self, VIN):
        self.mileage = 0
        self.VIN = VIN

# creating a car object\
car = Car('ABC123')
print("The mileage is: ", car.mileage)
print("The VIN is: ", car.VIN)
print('---------------------------------')


"""
    Decorators - summary:
    ---------------------
    a.  A decorator is a very powerful and useful tool in Python, because it allows programmers to modify the behavior of a function, method, 
        or class.
    b.  Decorators allow us to wrap another callable object in order to extend its behavior.
    c.  Decorators rely heavily on closures and *args and **kwargs.

Note:   the idea of decorators was described in two documents – PEP 318 and PEP 3129.

"""