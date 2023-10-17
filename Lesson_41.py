"""
    ------------------------------------------------------------------------------------------------
                                    User defined Exceptions
    ------------------------------------------------------------------------------------------------
    a.  Users may define their own exceptions.
    b.  All user defined exceptions must be derived as subclasses from the predefined 
        classes.

    Note:
    ----
    a.  If you want to create an exception which will be utilized as a specialized case of any 
        built-in exception, derive it from just this one. If you want to build your own hierarchy.
    b.  If you don't want it to be closely connected to Python's exception tree, derive it from any of the 
        top exception classes, like Exception

"""
"""
# Case a:

    1.  We've defined our own exception, named MyZeroDivisionError, derived from the built-in 
        ZeroDivisionError
    2.  The do_the_division() function raises either a MyZeroDivisionError or ZeroDivisionError exception, 
        depending on the argument's value.
"""

class MyZeroDivisionError(ZeroDivisionError):	
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:		
        raise ZeroDivisionError("some bad news")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')

"""
    a.  When you're going to build a completely new universe filled with completely new creatures that have 
        nothing in common with all the familiar things, you may want to build your own exception structure.

        For example, if you work on a large simulation system which is intended to model the activities of 
        a pizza restaurant, it can be desirable to form a separate hierarchy of exceptions.

    b.  You can start building it by defining a general exception as a new base class for any other 
        specialized exception.
"""

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza
    
class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)

class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v
    
for x in I():
    print(x, end='')


class A:
    def __init__(self, v=1):
        self.v = v
    
    def set(self, v):
        self.v = v
        return v
    
a = A()
print(a.set(a.v + 1))


class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.args = (msg, )
    
try:
    raise Ex('ex')
except Ex as e:
    print(e)
except Exception as e:
    print(e)