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

