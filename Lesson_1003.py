"""         Classes, Instances, Attributes, Methods — what is a class?
            ----------------------------------------------------------
What is class?
    a.  expresses an idea. 
    b.  it's a blueprint, or recipe for an instance;
    c.  Classes describe attributes and functionalities together to represent an idea as accurately as possible.
    d.  You can build a class from scratch or, something that is more interesting and useful, employ 
        inheritance to get a more specialized class based on another class.
    e.  Additionally, your classes could be used as superclasses for newly derived classes (subclasses).
    f.  A class is a place which binds data with the code.

What is an instance?
    a.  An instance is one particular physical instantiation of a class that occupies memory and has data 
        elements. This is what 'self' refers to when we deal with class instances.

    b.  An object is everything in Python that you can operate on, like a class, instance, list, or dictionary
    c.  The term instance is very often used interchangeably with the term object, because object refers to a 
        particular instance of a class. It's a bit of a simplification, because the term object is more general
        than instance.
    d.  The relation between instances and classes is quite simple: we have one class of a given type and an 
        unlimited number of instances of a given class.
    e.  Each instance has its own, individual state (expressed as variables, so objects again) and shares its 
        behavior (expressed as methods, so objects again).
    f.  To create instances, we have to instantiate the class
"""

class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex
    
    def walk(self):
        pass

    def quack(self):
        return print('Quack')
    
duckling = Duck(height=10, weight=3.4, sex='male')
drake = Duck(height=25, weight=3.7, sex='male')
hen = Duck(height=20, weight=3.4, sex='female')

"""
    An attribute refers to two kinds of class traits:
        a.  variables:  
            ----------
            1.  contains information about the class itself or class instance; 
            2.  Class and class instances can own many variables.
        b.  methods:  
            --------
            1.  methods are formulated as Python functions
            2.  methods represent a behaviour that could be applied to the objects.
            3.  methods are callable attributes of python objects
            4.  methods are called on behalf of an object.
            5.  methods are executed on object data.

    Class attributes are most often addressed with 'dot' notation, i.e., <class>dot<attribute>. 
    The other way to access attributes (variables) it to use the getattr() and setattr() functions.

    Note:
    -----
    a.  Each python object has its own individual set of attributes.
    b.  We can extend that set of attributes by adding new attributes to the existing objects, change them
        or control access to those attributes.
"""
drake.quack()
print(duckling.height)

"""
    type:
    ----
    a.  is one of the most fundamental and abstract terms of python.
    b.  it is the foremost type that any class can be inherited from;
    c.  as a result, if you're looking for the type of class, then type is returned;
    d.  in all other cases, it refers to the class that was used to instantiate the object; it's a general 
        term describing the type/kind of any object;
    e.  it's the name of a very handy Python function that returns the class information about the objects 
        passed as arguments to that function;
    f.  it returns a new type object when type() is called with three arguments; we'll talk about this in the 
        'metaclass' section.
"""
print('---------------------------')
print(type)
print(type(Duck))
print(type(duckling))
print('---------------------------')

for att in dir(Duck):
    print(att, '\n')

print('-----------------------------------------------')
print(Duck.__class__)                   # returns <class 'type'>
print(duckling.__class__)               # returns <class '__main__.Duck'>
print(duckling.height.__class__)        # returns <class 'int'>
print(duckling.weight.__class__)        # returns <class 'int'>
print(duckling.sex.__class__)           # returns <class 'str'>
print(duckling.quack.__class__)         # returns <class 'method'>       
print('-----------------------------------------------')

"""
    Exercise:
    ---------
    Problem definition:
    -------------------
    a.  create a class representing a mobile phone;
    b.  your class should implement the following methods:
            a.  __init__ expects a number to be passed as an argument; this method stores the number in an 
                instance variable self.number
            b.  turn_on() should return the message 'mobile phone {number} is turned on'. 
                Curly brackets are used to mark the place to insert the object's number variable;
            c.  turn_off() should return the message 'mobile phone is turned off';
            d.  call(number) should return the message 'calling {number}'. Curly brackets are used to mark 
                the place to insert the object's number variable;
            e.  create two objects representing two different mobile phones; assign any random phone numbers 
                to them;
            f.  implement a sequence of method calls on the objects to turn them on, call any number. 
                Print the methods' outcomes; turn off both mobiles.

"""

class MobilePhone:
    def __init__(self, number):
        self.number = number
    
    def turn_on(self):
        return 'mobile phone number ' + str(self.number) + ' is turned on.'
    
    def turn_off(self):
        return 'mobile phone number ' + str(self.number) + ' is turned off.'

    def call(self, number):
        if self.number == number.number:
            return 'calling a number to itself is not allowed.'
        return str(self.number) + ' is calling ' + str(number.number) + '.'
    
cell_1 = MobilePhone(9071181166)
cell_2 = MobilePhone(9148617744)
cell_1.turn_on()
cell_2.turn_on()
print(cell_1.call(cell_2))
print(cell_1.turn_off())
print(cell_2.turn_off())
print('-----------------------------------------------')