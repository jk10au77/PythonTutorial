"""
    Exceptions:
    ------------
    Causes of errors:
    ------------------
    a. Code itself is not working as per intensions
    b. Data might be wrong
    """
# Data itself is wrong

value = [i for i in range(-10, 1)]
print(value)
# i want to find the inverse of each element in value list
"""
for i in value:
    print(1 / i)        # you will get error when this code tries to divide 1 by 0
        """
"""
    Dealing the exceptions caused due to data
    -----------------------------------------
    a. Check the data before processing
    """
"""
for i in value:
    if i == 0:      # every iteration, we are checking data for 0
        continue    # if data is zero, we simply bypass the 0
    print(1 / i)
    """
"""
    In computer programming, its always better to handle an error when it happens than try to avoid it
    This can be done by using the try-exception branch.
    try - exception branch: 
    -----------------------
    The try-exception branch skeleton looks like below:
        try:
            # Place your code you suspect is risky and may be terminated in case of error.
            # Simply saying we are raising an exception
        exception:
            # Here we add code to handle the exception raised in the try statement.
    """
"""
print("Handling of exception errors using try-except method ")
try:
    for i in value:
        print("The reciprocal of", i, "is", 1/i)

except:
    print("I do not know how to divide a number by zero: ")
    """
"""
    The try-exception branch skeleton looks like below:
    ----------------------------------------------------------
    a.  any part of the code placed between try and except is executed in a very special way – any error which
        occurs here won't terminate program execution. Instead, the control will immediately jump to the first 
        line situated after the except keyword, and no other part of the try branch is executed;

    b.  the code in the except branch is activated only when an exception has been encountered inside the try block. 
        There is no way to get there by any other means;

    c.  when either the try block or the except block is executed successfully, the control returns to the normal 
        path of execution, and any code located beyond in the source file is executed as if nothing happened.
        """

"""
    Dealing with more than one exception:
    --------------------------------------
    The below code snippet deals with handling exception with multiple exceptions
  """ 

value.insert(0,'Python')        # append string to the list
print(value)
try:
    for i in value:
        print("The reciprocal of", i, "is", 1/i)
except ZeroDivisionError:
    print("Division by zero is not allowed in our universe.")
except TypeError:
    print("I do not know what to do.")
    
"""
    The default exception and how to use it:
    ------------------------------------------
    a.  The default except branch should be placed at the last. 
    b.  The default exception does not have a exception name
    c.  You can expect that when an exception is raised and there is no except branch dedicated to this exception, 
        it will be handled by the default branch.
    """
try:
    for i in value:
        print("The reciprocal of", i, "is", 1/i)

except TypeError:
    print("I do not know what to do.")
except ZeroDivisionError:
    print("Division by zero is not allowed in our universe.")
except:
    print("Something strange has happened here...Sorry.")

"""
    Some useful exceptions:
    -----------------------
    a. ZeroDivisionError
    b. ValueError
    c. TypeError
    d. AttributeError
    e. SyntaxError

"""
"""
what is the output of the following code?

dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']
for k in range(len(dictionary)):
    v = dictionary[v]
print(v)

what is the output of the following code?
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 
    
print(fun(fun(2)) + 1)

what is the output of the following code?

def any():
    print(var + 1, end='')

var = 1
any()
print(var)

# what is the output of the following code?
my_list = ['mary', 'had', 'a', 'little', 'lamb']

def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'

print(my_list(my_list))

what is the output of the following code?

def func_1(a):
    return a ** a

def func_2(a):
    return func_1(a) * func_1(a)

print(func_2(2))

what is the output of the following code?
"""
dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k)

