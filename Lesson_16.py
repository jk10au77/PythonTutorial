"""
    Function: A function is a block of code that performs a specific task when the function is called (invoked)

    In Python, there are four basic types of functions:
        a. built-in functions   example: input(), print()
        b. from preinstalled modules 
        c. user-defined functions
        d. lambda functions
    Functions sre defined by using a key word 'def'.
"""
"""
    parameterized function: functions defined with parameter are called parameterized functions
    a. A parameter is actually a variable.
    b. parameters exist only inside functions in which they have been defined, and the only place 
       where the parameter can be defined is a space between a pair of parentheses in the def statement;
    c. assigning a value to a parameter is done at the time of function's invocation.
    d. Parameters live inside functions
    e. arguments exist outside the function.    

"""
import random

def message(number):
    print("Enter a number: ", number)

message(10)

def introduce(first_name, last_name):
    print("Hello, my name is ", first_name, last_name)

introduce("Jaya", "Kumar")

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(a = 1,c = 2, b=3)        

"""
    the 'return' instruction: return the value of a function to its caller.

    return instruction is of two types:
        a. return without instruction: immediate termination of the function's execution, 
            and an instant return (hence the name) to the point of invocation.
        b. return with expression: return the value of a expression to its caller

"""
# terminate a function's activities on demandas shown below

def happy_new_year(wishes = True) :
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    print("Happy New Year: ")
happy_new_year()
# example for returninstruction with expression

def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
value = boring_function()
print("This lesson is boring...", value)

"""
    Write a function which takes one argument (a year) and returns
        a. True if the year is a leap year
        b. Flase if the year is not a leap year
    
        Note:   A year is said to be leap year if it is divided by 4 and If the year is a century year, 
                then it is a leap year if it divided by 4 and 100
"""

def isYearLeap(year):
    if (year % 4 == 0) or (year % 4 != 0 and year % 100 == 0):
        return True
    else:
        return False
print("Begin of leap year test: ")
test_data = []
for count in range(10):
    test_data.append(random.randint(1900, 2050))
result =[]
for year in test_data:
    result.append(isYearLeap(year))

print(test_data)
print(result)
print("End of leap year test.")