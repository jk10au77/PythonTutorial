"""         Python core syntax
        ---------------------------
a.   Python core syntax - an ability to perform specific operations on different data types, when operations 
    are formulated using the same operators or instructions, or even functions.

b.   Python core syntax covers:

        a.  operators like '+', '-', '*', '/', '%' and many others;
        b.  operators like '==', '<', '>', '<=', 'in' and many others;
        c.  indexing, slicing, subscripting;
        d.  built-in functions like str(), len()
        e.  reflexion - isinstance(), issubclass()
    and a few more elements.

c.  Python allows us to employ operators when applied to our objects, so we can use core operators on our 
    objects.

d.  When called, functions and operators that state the core syntax are translated into magic methods 
    delivered by specific classes.

e.  These special functions are called magic functions, or dunder methods. The name of each magic method is 
    surrounded by double underscores (Pythonistas would say “dunder” for double underscores, as it's a shorter 
    and more convenient phrase).

f.  Dunder methods are not called directly, but called in a process of expression evaluation, according to 
    Python core syntax rules.

g.  The '+' operator is converted into __add__() method and the len() function is converted into __len__() 
    method.

h.  These dunder methods must be implemented by a class to perform the appropriate action.

Note:
----
    When you design and implement your own classes and you want to make use of Python core syntax to operate 
    on those class objects, you can easily achieve this by implementing the appropriate magic methods.

"""

class Person:

    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary
   
    def __add__(self, other):
        return self.weight + other.weight

p1 = Person(30, 40, 50)
p2 = Person(35, 45, 55)

print(p1 + p2)
print('-------------------------------------------------------------------------------------')
print("Printing dunder methods available in core python.")
ser_number = 0
for i in dir(10):
    if i.startswith('__') and i.endswith('__'):
        ser_number += 1
        print(f'S.No: {ser_number}: {i}')

"""
Scenario:
----------
a.  Create a class representing a time interval;
b.  The class should implement its own method for addition, subtraction on time interval class objects;
c.  The class should implement its own method for multiplication of time interval class objects by an 
    integer-type value;
d.  The __init__ method should be based on keywords to allow accurate and convenient object initialization, 
    but limit it to hours, minutes, and seconds parameters;
e.  The __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and 
    SS represents the seconds attributes of the time interval object;
f.  check the argument type, and in case of a mismatch, raise a TypeError exception.
"""

