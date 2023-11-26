"""
    The static and class methods:   
    ------------------------------
    https://edube.org/learn/python-advanced-1/class-methods

    a.  The two other types of methods that can be used in Object Oriented Approach (OOP) are
        1.  class methods
        2.  static methods

    claSS methods:  The classmethod() is an inbuilt function in Python, which returns a class method for a given function.
    --------------


    a.  Like class variables, class methods work on the class itself, and not on the Objects that are instantiated.
    b.  class methods are bound to the class, not to the object.
    c.  A class method can access or modify the class state.
    d.  class methods must have class as a parameter.
    e.  We use @classmethod decorator in Python to create a class method.

    Syntax: classmethod(function)
    ------
    1.  This function accepts the function name as a parameter.
    2.  This function returns the converted class method.

    when can class methods be useful?
    ----------------------------------
    There are several possibilities, here are the two most useful.

    a.  we control access to the class variables. e.g., to a class variable containing information about the number of created instances or 
        the serial number given to the last produced object, or we modify the state of the class variables;
    b.  we need to create a class instance in an alternative way, so the class method can be implemented by an alternative constructor.

    conventions:
    ------------
    a.  To be able to distinguish a class method from an instance method, the programmer signals it with the @classmethod decorator preceding 
        the class method definition.
    b.  Additionally, the first parameter of the class method is cls, which is used to refer to the class methods and class attributes.

    Note: As with self, cls was chosen arbitrarily (i.e., you can use a different name, but you must do it consistently).


"""
# Example 1
class Example:
    __internal_counter = 0

    def __init__(self, value):
        Example.__internal_counter += 1

    @classmethod          
    def get_internal(cls):          # is a class method. This has been signalled by using appropriate decorator. Also the method uses the cls parameter to access the class variable.
        return '# of objects created: {}'.format(cls.__internal_counter)
    
print(Example.get_internal())

example_1 = Example(10)
print(Example.get_internal())

example_2 = Example(99)
print(Example.get_internal())

print('-----------------------------------------------')
# Example_2

# the below code illustrates the use of class method as an alternate constructor, allowing you to handle an additional argument.

class Car:
    def __init__(self, vin):
        print("Ordinary __init__ was called for ", vin)
        self.vin = vin
        self.brand = ''

    @classmethod
    def including_brand(cls, vin, brand):   # is a classmethod, and expects a call with two parameter ('vin' and 'brand'). The first parameter is used to create an object using the standard __init__ method.
        print('Class method was called')
        _car = cls(vin)                     # In accordance with the convention, the creation of a class object (i.e., calling the __init__ method, among other things) is done using cls(vin).
        _car.brand = brand  #Then the class method performs an additional task – in this case, it supplements the brand instance variable and finally returns the newly created objec
        return _car
    
car_1 = Car('ABCD1234')
car_2 = Car.including_brand('DEF567', 'NewBrand')

print(car_1.vin, car_1.brand)
print(car_2.vin, car_2.brand)
print('-----------------------------------------------') 