"""
    The lambda function or anonymous function:
    ------------------------------------------
    a.  Programmers use the lambda function to simplify the code, to make it clearer and easier to understand.
    b.  A lambda function is a function without a name. It is also called anonymous function.
    c.  The declaration of the lambda function doesn't resemble a normal function declaration in any way
            
            lambda parameters: expression
        Such a clause returns the value of the expression when taking into account the current value of the 
        current lambda argument.

"""

two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y : x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)

