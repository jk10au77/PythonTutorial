"""
    Decorators:
    -----------
    a.  A decorator is one of ther design patterns that describes the structure of related objects.
    b.  Python is able to decorate function, methods, and classes.
    c.  The decorator's operator is based on on wrapping the original function with another function. This is done by passing the original 
        function (i.e. the decorated function) to the decorating function so that the decorating function can call the original function. 
        The decorating function returns a function that can be called later.
    d.  The decorating function does more, because it can take the parameters of the decorated function and perform additional actions and 
        that make it a real decorating function.
    
        Note:   The same principle is applicable when we decorate classes.
    e.  Decorators are used to perform operations before and after a call to a wrapped object or even to prevent it's execution. As a result,
        we can change the operation of the packaged object without modifying it.
    
        Application of decorator:
        -------------------------
        a.  for validating arguments.
        b.  modifying arguments.
        c.  modifying the returned objects.
        d.  measurement of execution time.
        e.  message logging.
        f.  thread synchronization.
        g.  code refactorization.
        h.  caching.
"""

"""
    Function decorators:
    --------------------

"""
# create a simple function simple_hello() 

def simple_hello():
    print("Hello from simple function!")

# create another function - simple_decorator()

def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function

decorated = simple_decorator(simple_hello)
decorated()

"""
    In the above, we have created a simple decorator - a function which accepts another function as its only argument, prints some details,
    return a funtion or other callable
    The above code can be literally decorated with @simple_decorator as shown in the below code snippet.
    This means that:

        a.  operations are performed on object names
        b.  the name of the simple_function object ceases to indicate the object representing our simple_function() and from that moment on 
            it indicates the object returned by the decorator, the simple_decorator.
Note:   It should be mentioned that decorators are very useful for refactoring or debugging the code.

"""
def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function


@simple_decorator
def simple_hell():
    print("Hello from a simple function")

simple_hello()
