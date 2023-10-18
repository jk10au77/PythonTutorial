loc = 10

def f():
    print(loc)      # functions can access variables outside the function scope

f()

print(loc)

def g():
    loc = 20
    print(loc)
g()
print("Printing after invoking g(): ", loc)

"""
    Closures:
    -------------
        a.  Closure is a technique which allows the storing of values in spite of the fact that the context 
            in which they have been created does not exist anymore
        b.  Closure in Python is an inner function object. 
        C.  Everything in Python is object. i.e. function also behaves like an object. So it remembers and has
            has access access to variables in the local scope in which it was created even after the outer
            function has finished executing
        d.  It can also be defined as a means of binding data to a function (linking / attaching the data with 
            the function so that they are together), without passing it as a parameter.
        e.  Even if values in enclosing scopes are not present in memory, a closure is a function object that 
            remembers those values.
        f.  A python closure isn't like a plain function. It allows the function to access those captured 
            variables through the closure's copies of their values or references, even if the function is 
            invoked outside their scope.
        g.  Objects can be described as data with methods attached, while closures are functions with data 
            attached.
        h.  A closure has to be invoked in exactly the same in which it has been declared.
"""
# A closure has to be invoked in exactly the same in which it has been declared.
def outer(par):
    loc = par
    
    def inner():
        return loc
    return inner
var = 1
fun = outer(var)    
print(fun())    #the inner() function is parameterless, so we have to invoke it without arguments.

# we can also declare a closure with an arbitrary number of parameters as shown below

def make_closure(par):
    loc = par 

    def power(p):
        return p ** loc
    return power

fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))