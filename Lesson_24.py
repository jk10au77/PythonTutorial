"""
    Errors - The programmer's bread
    ----------------------------------
    a. Anything that can go wrong, will go wrong.
"""

import math

x = float(input("Enter x: "))
y = math.sqrt(x)

print("The square root of", x, "equals to", y)
"""
In the above code snippet, there are atleast two possible ways it can go wrong.
    a.  As a user is able to enter a completely arbitrary string of characters, there is no guarantee that the 
        string can be converted into a float value - this is the first vulnerability of the code;
    b.  the second is that the sqrt() function fails if it gets a negative argument.

Can you protect yourself from such surprises? Of course you can. Moreover, you have to do it in order to be 
considered a good programmer.

    Exceptions:
    -----------
    a.  Each time your code tries to do something wrong/foolish/irresponsible/crazy/unenforceable, Python does two things:

            a.  it stops your program;
            b.  it creates a special kind of data, called an exception.

    b.  Both of these activities are called raising an exception. 
    c.  Python always raises an exception (or that an exception has been raised) when it has no idea what to do with your 
        code.
    
    Then, what next?
    ----------------
    a.  the raised exception expects somebody or something to notice it and take care of it;
    b.  if nothing happens to take care of the raised exception, the program will be forcibly terminated, and you will 
        see an error message sent to the console by Python;
    c.  otherwise, if the exception is taken care of and handled properly, the suspended program can be resumed and its 
        execution can continue.
    
    Python provides effective tools that allow you to observe exceptions, identify them and handle them efficiently. 
    This is possible due to the fact that all potential exceptions have their unambiguous names, so you can categorize 
    them and react appropriately.

On running the below code, Python terminates the execution because of the error
"""

value = 1
value = 1 / 0
"""
The traceback consists of the following details
-----------------------------------------------
    a.  File name: 
    b.  Line number: line number where exception is caused. It is 5o
    c.  Module name:  module name where a the statement is.
    d.  Exception name and brief description about the exception: Here it is ZeroDivisionDivision
    
"""
"""
    Then how will we handle exceptions:
        one way, is by using try and except block.
    For example, have a look at the below code snippet
    """
try:
    x = int(input("Enter a number: "))
    y = x ** -1

except  ZeroDivisionError:
        print("You can't divide by zero, sorry")
except  ValueError:
        print("You must enter an integer.")
except:
       print("Oh dear, something went wrong.")

print("THE END")

"""
    Don't forget that:
    -------------------

    a.  The except branches are searched in the same order in which they appear in the code;
    b.  You must not use more than one except branch with a certain exception name;
    C.  The number of different except branches is arbitrary - the only condition is that if you use try, you must put 
        at least one except (named or not) after it;
    d.  The except keyword must not be used without a preceding try;
    e.  If any of the except branches is executed, no other branches will be visited;
    f.  If none of the specified except branches matches the raised exception, the exception remains unhandled 
        (we'll discuss it soon)
    g.  If an unnamed except branch exists (one without an exception name), it has to be specified as the last.

"""



