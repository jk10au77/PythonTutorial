"""-----------------Module-----------------------
In this lesson, you will learn about:
    a. importing and using Python modules.
    b. using some of the most useful Python standard modules.
    c. Constructing and using Python modules.
    d. PIP (Python Installation Package) and how to use PIP to install and uninstall ready-to-use from PyPI
"""
"""
If you want such a software project to be completed successfully, you have to have the means allowing you to:
    a.  divide all the tasks among the developers;
    b.  join all the created parts into one working whole.

For example, a certain project can be divided into two main parts:
    a.  the user interface (the part that communicates with the user using widgets and a graphical screen)
    b.  the logic (the part processing data and producing results)

Each of these parts can be (most likely) divided into smaller ones, and so on. Such a process is often called 
decomposition.
How do you divide a piece of software into separate but cooperating parts? 
This is the question. Modules are the answer.

"""
"""
Module: is a file containing Python definitions and statements, which can later imported and used when necessay.
        Few examples include datetime module, Math module, Pandas module, NumPy module etc

The handling of modules consists of two different issues:
    a. users - who uses the existing modules
    b. suppliers - who creates modules

a.  Modules are identified by its name.
b.  All these modules, along with the built-in functions, form the Python standard library
c.  Each module consists of entities. These entities can be constants, variables, functions, classes, and objects.
d.  To make a module usable, you have to import it. using the below syntax
    import  module_name

Namespace:  is a space (understood in a non-physical context) in which some names exists and 
the names donot conflict with eachother.
"""

import math         # import math module

def sin(x):
    if 2 * x == pi:
        return 0.999999999
    else:
        return None

pi = 3.14           # defined our own pi
print(sin(pi/2))
print(math.sin(math.pi/2))  # uses pi defined in math module

""" 
    Key takeaways:
    ---------------
    a.  If you want to import a module as a whole, you can do it using the import module_name statement. 
        You are allowed to import more than one module at once using a comma-separated lis
    b.  If a module is imported in the above manner and you want to access any of its entities, you need 
        to prefix the entity's name using dot notation.
    c.  You are allowed not only to import a module as a whole, but to import only individual entities from it. 
        In this case, the imported entities must not be prefixed when used.
"""
"""
    dir() - gives all the entities in a module
    Working with standard modules:
    ------------------------------


"""
for name in dir(math):
    print(name, end='\n')
print('--------------------------------------')
print('End of printing math module entities.')
print('--------------------------------------')

"""
    Few modules:
    ---------------
    a.  platform - we can access underlying platform's data like hardware, operating system, and interpretor's 
        version 
    b.  math -  contain basic mathematical functions
    c.  random - random module
    d.  builtins - provides direct access to all ‘built-in’ identifiers of Python;
"""

import platform
for name in dir(platform):
    print(name, " : ", type(name))

"""
    Key takeaways:
    --------------
    a. dir() function 
    b. math module
    c. random module
    d. platform module
    e. python module index

    Module:
    a. module is a kind of container filled with functions - you can pack as many functions as you want into 
       one module and distribute it across the world;
    b. of course, it's generally a good idea not to mix functions with different application areas within 
       one module (just like in a library - nobody expects scientific works to be put among comic books), 
       so group your functions carefully and name the module containing them in a clear and intuitive way 
       (e.g., don't give the name arcade_games to a module containing functions intended to partition and 
       format hard disks)
    c. making many modules may cause a little mess - sooner or later you'll want to group your modules exactly 
       in the same way as you've previously grouped functions - is there a more general container than a module?
    d. yes, there is - it's a package; in the world of modules, a package plays a similar role to a 
       folder/directory in the world of files.
"""
"""
    =======================================================================================================
                                        Package:    
    =======================================================================================================
    Description: 
    ------------
    We usually organize our files in different folders and subfolders based on some criteria, so that they 
    can be managed easily and efficiently. We usually organize our files in different folders and subfolders 
    based on some criteria, so that they can be managed easily and efficiently. 
    
    Definition:
    -----------
    Package in Python is a folder that contains various modules as files.

    Your first module - step1: create an empty file called module.py
    your first module - step2: create anothe empty file called main.py. Now import module.py in this file.
                                save the file.
    Note: Both files must be located in the same file.
    Now run the main.py file. You should see nothing. This means that Python has successfully imported the 
    contents of the module.py file
    Now take a look into the folder in which both files exist.
    A new subfolder has appeared - can you see it? Its name is __pycache__. Take a look inside
            

"""


   


