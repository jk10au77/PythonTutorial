"""
def simple_decorator(function):
    print("We are about to call '{}'".format(function.__name__))
    return function

@simple_decorator
def simple_hello():
    print("Hello from simple function!")

simple_hello()

"""

"""
    Decorators should be universal: Decorators, which should be universal, must support any function, regardless of the number and type of 
                                    arguments passed.
    Decorating function that accepts arguments 

"""
"""
def simple_decorator(own_function):

    def internal_wrapper(*args, **kwargs):
        print('"{}" was called with the following arguments'.format(own_function.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        own_function(*args, **kwargs)
        print("Decorator is still operating")

    return internal_wrapper

@simple_decorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)

combiner('a', 'b', exec='yes')
"""
"""
In the above example:
    Arguments passed to the decorated function are available to the decorator. So, the decorator can print them.
    A nested function (internal_wrapper) could reference an object (own_function) in its enclosing scope thanks
    to the closure.

"""

"""
    Decorators can accept their own attributes:

"""
"""
"""
print("---------------------------------------------")
print("Decorator can accept their own attributes")
print("---------------------------------------------")
def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
            our_function(args)
            print()
        return internal_wrapper
    return wrapper

@warehouse_decorator('kraft')
def pack_books(*args):
    print("We will pack books:", args)

@warehouse_decorator('foil')
def pack_toys(*args):
    print("We will pack toys:", args)

@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We will pack fruits:", args)

pack_books("Alice in Wonderland", "Winne in Pooh")
pack_toys("doll", "car")
pack_fruits("plum", "pear")

print("---------------------------------------------")
print("---------------------------------------------")
"""
"""
"""
Decorator stacking:
-------------------
a.  In Python, we can apply multiple decorators to a callable object (function, class, and method)
b.  The most important thing to remember is the order in which decorators are listed in your code, because it determines the order of the 
    execution of decorators.
c.  When your function is decorated with multiple decorators:

    @outer_decorator
    @inner_decorator
    def functio():
        pass

the call sequence will look like the following:

a.  the outer_decorator is called to call the inner_decorator, then the inner_decorator calls your function;
b.  when your function ends it execution, the inner_decorator takes over control, and after it finishes its execution, the outer_decorator is 
    able to finish its job.
"""
"""
def big_container(collective_material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> The whole order would be packed with', collective_material)
            print()
        return internal_wrapper
    
    return wrapper


def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
        return internal_wrapper
    return wrapper

@big_container('plain cardboard')
@warehouse_decorator('bubble foil')
def pack_books(*args):
    print("We will pack books:", args)

@big_container('colourful card board')
@warehouse_decorator('foil')
def pack_toys(*args):
    print("We will pack toys: ", args)

@big_container('strong cardboard')
@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("we will pack fruits: ", args)

pack_books("Alice in Wonderland", "Winne in Pooh")
pack_toys("doll", "car")
pack_fruits("plum", "pear")

"""

"""
Decorating functions with class:
--------------------------------
a.  In Python, decorators can be either function or classes. In both cases, decorating adds functionality to existing function.
b.  When we decorate a function with a class, the function becomes an instance of the class. When we define methods in the decorating class,
    we can add functionality to the function. This can be achieved without modifying the original function source code.
c.  Here we demostrate two cases:
    1.  Decorating a function with a class that accepts no arguments.
    2.  Decorating a function with a class that accepts arguments.

"""



"""
    a.  To decorate a function with a class, we must use the @ syntax followed by the class name above the function definiton. 
    b.  When we decorate a function with a class, the function is automatically passed as a first arguments to the init constructor. We set this
        function as an attribute in our object. Now if we print multiply_together, we can see it as an instance of the power class.
    c.  In order to define a class as a decorator, we have to use a __call__ special class method.
    d.  When a user needs to create an object that acts as a function (i.e., it is callable) then the function decorator needs to return an 
        object that is callable, so the __call__ special method will be very useful.

    Class definition:
    ------------------

    a.  class name: SimpleDecorator
    b.  class methods:
        1.  __init__(self)
        2.  __call__(self)
    
    Function definition:
    --------------------
a.  function name:  combiner()  with variable positional and keyword arguments
  
"""

class SimpleDecorator:
    """
    A short explaination of special methods:

        a.  the __init__ method assigns a decorated function reference to the self attribute for later use.
        b.  the __call__ method is responsible for supporting a case when an object is called. calls a previously referenced function.

    Note:   
    ------
    a.  The advantage of this approach, when compared to decorators expressed with functions, is:
        classes bring all the subsidiarity they can offer, like inheritance and the ability to create dedicated supportive methods.

"""

    def __init__(self, own_function):
        self.func = own_function

    def __call__(self, *args, **kwargs):
        print('"{}" was called with the following arguments'.format(self.func.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        self.func(*args, **kwargs)
        print('Decorator is still operating')


@SimpleDecorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)

combiner('a', 'b', exec='yes')

"""
    class decorators with arguments:

"""

class WarehouseDecorators:

    def __init__(self, material):
        self.material = material
    
    def __call__(self, own_function):
        def internal_wrapper(*args, **kwargs):
            print('<strong>*</strong> Wrapping with items from {} with {}'.format(own_function.__name__, self.material))
            own_function(*args, **kwargs)
            print()
        return internal_wrapper

@WarehouseDecorators('Kraft')
def pack_books(*args):
    print("We will pack books: ", args)

@WarehouseDecorators('foil')
def pack_toys(*args):
    print("we will pack toys: ", args)

@WarehouseDecorators('cardboard')
def pack_fruits(*args):
    print("We will pack fruits: ", args)

pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
