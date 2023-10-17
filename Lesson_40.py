"""
    There are 2 types of errors:
        a.  Syntax errors - also known as parsing errors
        b.  Exceptions - Errors found during execution are known as exceptions. These are fatal
    
    Exceptions handling:
    --------------------
    Exceptions are handled using try - except block.
        First, the try clause (the statement(s) between the try and except keywords) is executed.

            a.  If no exception occurs, the except clause is skipped and execution of the try statement is 
                finished.

            b.  If an exception occurs during execution of the try clause, the rest of the clause is skipped. 
                Then, if its type matches the exception named after the except keyword, the except clause is 
                executed, and then execution continues after the try/except block.
            c.  If an exception occurs which does not match the exception named in the except clause, it is 
                passed on to outer try statements; if no handler is found, it is an unhandled exception and 
                execution stops with a message.
        for example, see below code
    """
"""
while True:
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("That was not a valid number. Try again...")
"""
"""
    a.  A try statement may have more than one except clause. i.e. in each except clause we specify a 
        different handler.
    b.  At most one handler will be executed
    c.  Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of 
        the same try statement.
    d.  An except clause may name multiple exceptions as a parenthesized tuple.
    e.  A class in an except clause is compatible with an exception if it is the same class or a base class as 
        shown below
    F.  So, when an exception is raised, an exception object is instantiated, and goes through all levels of 
        program execution , looking for except branch that is prepeared to deal with it.

"""

class B(Exception):
    pass

class C(B):
    pass
class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

"""
    Note that if the except clauses were reversed (with except B first) and observe the result.
"""

for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")

"""
    Deeper look into exceptions:
    ----------------------------
        a.  Exceptions are classes.
        b.  So, when an exception is raised:
                1.  an exception object is instantiated, and goes through all levels 
                    of program execution , looking for except branch that is prepeared to deal with it.
                2.  an exception may have associated values. These values are called exception's arguments.
                    The presence and type of the arguments depend on the exception type.
        C.  The except clause may specify a variable after exception name. The variable is bound to the
            exception instance. This exception instance has an 'args' attribute that stores the exception 
            arguments.
            For example, built-in 'Exception' type defines __str__() to print all the arguments without 
            accessing '.args'
        d.  All built-in python exceptions form a hierachy of classes. BaseException is the base class 
        e.  All built-in exceptions are extended from this BaseException class.
        f.  We can also build our own exception hierachy, but only thing is that we need to use BaseException
            as a base for user-built in exceptions.
            
"""

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))           # the exception type
    print(inst.args)            # prints the arguments stored in .args 
    print(inst)                 # __str__() allows args to be printed directly
    x, y = inst.args            # unpacking args
    print("x = ", x)
    print("y = ", y)
    
"""
    The below code snippet dumps all the predefined exception classes in the form of a tree-like prinout

"""
"""
print("Printing the dump of all predefined exception classes in the form a tree-like printout.")
def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("  |" * (nest - 1), end = "")
    if nest > 0:
        print("  +---", end = "")
    print(thisclass.__name__)
    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)

print_exception_tree(BaseException)
print("End of printing predefined exception classes.")
"""
"""
    Detailed anatomy of exceptions:

"""
print("printing the args property of BaseException: ")
"""
    The print_args() function print the contents of the args property in three different cases, 
    where the exception of the Exception class is raised in three different ways. 
    To make it more spectacular, we've also printed the object itself, along with the result of the __str__() 
    invocation.

    Case 1: There is just the name Exception after the raise keyword. This means that the object of this class has been
            created in a most routine way.
    Case2:  In the second raise statement, the constructor is invoked with one argument.
    Case3:  The third raise statement, the constructor is invoked with two argument.


"""
def print_args(args):
    pass

try:
    raise Exception
except Exception as e:
    print(e, e.__str__, sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=" : ", end=(" : "))
    print_args(e.args)

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__, sep=" : ", end=" : ")
    print_args(e.args)

print("End of printing the args property of BaseExeption class ")




