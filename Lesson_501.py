"""
    The __all__ in Python:
    ----------------------
    a.  The __all__ is a list of strings that define what variables have to be imported from a module or package
        to another module.
    b.  The variables which are declared in that list can only be used in another file after importing this 
        file, the rest variables if called will throw an error.
    
    Benefits of __all__ in python:
    ------------------------------
    a.  Security purpose:   While importing the data from one Python file to another, all the first file's 
        variables are usable in the second file. But for security purposes, we want the second file to use 
        only certain variables and not all the variables of the first file. Then, we can use the __all__ 
        function in the first Python file and define its usable variables.
    b.  Usage of the same variable name: Suppose we have declared one variable, ABC, in the first Python file, 
        and another Python file is calling the first Python file; then, all the variables of the first file 
        will be imported into the second file.

    Steps to create __all__ list in python:
    ---------------------------------------
    a.  First of all, define the values and declare them in the variables. create a list of the values which 
        you need to import into another file and declare them in the __all__ package.

    The __all__ in __init__.py:
    ---------------------------
    a.  The __init__.py files are required to make Python treat the directories as containing packages.

    b.  In the simplest case, __init__.py can be an empty file, but it can also execute the initialization 
        code for the package or set the __all__ variable.

    c.  A package is typically made up of modules that may import one another but are necessarily tied together
        with an __init__.py file.

    """

import datetime

print(datetime.__all__)
print('\n')
import calendar
for i in calendar.__all__:
    print(i)
