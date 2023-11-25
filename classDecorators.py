"""
    Class decorators:
    -----------------
    a.  Class decorators strongly refer to function decorator, because they use the same syntax and implement the same concepts.
    b.  

Let's first creat a simple class to which the decorator will be applied.

class Name: Phone

class Phone:
    def __init__(self, number):
        print(f'A phone is created with number: {number}.')
        self.number = number

    def dial(self, number):
        print(f"{self.number} calling {number}...")

"""
   
"""
    It's common to decorate the methods of classes, which works exactly the same as decorating function. 
    Let's use the simple decorator to decorate the dial method of the Phone class.
    https://lynn-kwong.medium.com/how-to-decorate-classes-in-python-edf826196fbf

"""

from functools import wraps

def func_decorator(func):
    #print("Inside the decorator.")
    # The wraps decorator is used to preserve the properties of the original function.
    # Note the parameters are passed to wrapper.
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("In wrapper.")
        print("Do something before the function is executed.")
        #execute the function and ge the return value.
        value = func(*args, **kwargs)
        print("In wrapper.")
        print("Do something after the function is executed.")
        # we need to return the value explicitly
        return value
    # return the wrapper which is the decorated function
    return wrapper
"""
class Phone:

    def __init__(self, number):
        print(f"A phone is created with number {number}.")
        self.number = number

    @func_decorator
    def dial(self, number):
        print(f"{self.number} calling {number}...")
    
# Let's see how the function decorator works when it's applied to the dial method of the Phone class

phone = Phone("9071181166")
phone.dial("9148617744")
"""
# Now let's apply the function decorator to the class and see what happens:

@func_decorator
class Phone:
    def __init__(self, number):
        print('fA phone is created with number {number}.')
        self.number = number

    def dial(self, number):
        print(f"{self.number} calling {number}...")

phone = Phone("9071181166")
