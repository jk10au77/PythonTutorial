"""
    Extended Function arguments:
    ---------------------------
    a.  some functions can be invoked without arguments;
    b.  functions may require a specific number of arguments with no exclusions; we have to pass a required number of arguments in an imposed 
        order to follow function definition;
    c.  functions might have already defined default values for some parameters, so we do not have to pass all arguments as missing arguments, 
        complete with defaults; parameters with default values are presented as keyword parameters;
    d.  we can pass arguments in any order if we are assigning keywords to all argument values, otherwise positional ones are the first ones 
        on the arguments list.
"""

"""
    Now let’s get familiar with the functions that can accept any arbitrary number of positional arguments and keyword arguments.

    The *args and **kwargs identifiers:
    ------------------------------------
    a.  The *args and **kwargs identifiers should be put as the last two parameters in a functiond definition.
    b.  Their names could be changed becxause it is just convention to name them as args and kwargs
    c.  These two special parameters are responsible for handling any number of arguments ((placed next after the expected arguments) passed to 
        a called function:
            1.  *args - refers to a tuple of all additional, not explicitly expected positional arguments, so arguments passed without keywords 
                and passed next after the expected arguments. In other words, *args collects all unmatched positional arguments;
            2.  **kwargs (keyword arguments) – refers to a dictionary of all unexpected arguments that were passed in the form of keyword=value 
                pairs. Likewise, **kwargs collects all unmatched keyword arguments.
    d.  In Python, asterisks are used to denote that args and kwargs parameters are not ordinary parameters and should be unpacked, as they 
        carry multiple items.
    
"""
def combiners(a, b, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))

combiners(10, '20', 40, 60, 30, argument1 = 50, argument2= '66')

"""
    Extended function argument syntax - forwarding arguments to other functions
    ---------------------------------------------------------------------------

"""
def super_combiner(my_args, my_kwargs):
    print("'my_args: ", my_args)
    print("my_kwargs: ", my_kwargs)

def combiner(a, b, *args, **kwargs):
    super_combiner(*args, **kwargs)

combiners(10, '20', 40, 60, 30, argument1 = 50, argument2= '66')

"""
    The following example shows how to combine *args, a key word, and **kwargs in one definition.
"""
def my_super_combiner(my_c, *my_args, **my_kwrgs):
    print("my_args: ", my_args)
    print("my_c: ", my_c)
    print("my_kwargs: ", my_kwrgs)


def my_combiner(a, b, *args, c=20, **kwargs):
    my_super_combiner(c, *args, **kwargs)

my_combiner(1, '1', 1, c=2, argument_1 = 1, argument_2 = '1')