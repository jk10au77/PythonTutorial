"""
    The anatomy of exceptions:
-------------------------------------------
a.  Python 3 defines 63 built-in exceptions, and all of them for a tree-shaped hierarchy
b.  Some of the built-in exceptions are more general (i.e. they include other exceptions), while others are completely 
    are completely concrete (they represent themselves only)
Note: 
    a.  The closer to the root an exception is located, the more general (abstract) it is
    b.   In turn, the exceptions located at the branches' ends (we can call them leaves) are concrete.


"""

"""
    The 'raise' instruction: 
    ------------------------
        a.  The 'raise' is used to raise an exception by yourself. The syntax of raise statement is
                    raise   [expression[from another_expression]]
        b.  to throw (or raise) an exception, use the raise keyword.
        c.  You can define what kind of error to raise, and text to print to the user.
        
"""
"""
x = 1
if not (x < 0):
    raise Exception("Sorry, no numbers below zero")

     """

# raise a TypeError if x is not an integer
"""
x = 'hello'
if not type(x) is int:
    raise TypeError('Only integers are allowed.')
    
"""
"""
    raise   [expression[from another_expression]]
    ----------------------------------------------
    a.  The BaseException is the base class for all built-in exceptions.
    b.  The expression object in the raise syntax must return an instance of a class that derives from BaseException
    c.  The expression object can also return the exception class itself, in which case Python will automatically
        instantiate the class for you.

    Note:
    ----
        a.  expression can be any Python expression that returns an exception class or instance. as shown in the below 
            example

        b.  Here This exception_factory() takes exception class and an error message as arguments.
        c.  Then the function instantiate the input exception using the message as an argument.
        d.  Finally, it return the exception instance to the caller.
        e.  You can use this function as an argument to the raise keyword, as you do in the below example.
"""
"""
def exception_factory(exception, message):
    return exception(message)

raise exception_factory(ValueError, "Invalid value")
"""
"""
    Another example of how raise works:
    -----------------------------------
    Here you create a new instance of the Exception class:

"""
raise Exception("an error occured")

"""
    Also go through the pdf in the repo for advanced tutorial in exceptions.


"""

