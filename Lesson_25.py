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
        a.  The 'raise' is used to raise an exception
        b.  to throw (or raise) an exception, use the raise keyword.
        c.  You can define what kind of error to raise, and text to print to the user.
        
"""
"""
x = 1
if not (x < 0):
    raise Exception("Sorry, no numbers below zero")
    """

# raise a TypeError if x is not an integer
x = 'hello'
if not type(x) is int:
    raise TypeError('Only integers are allowed.')