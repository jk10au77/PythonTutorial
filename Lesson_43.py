
"""
    Generator:
    ----------
    a.  Generator is also a function.
    b.  In generator we use yield statement whereas in Function we use return statment.
    c.  Generator returns one value at a time.
"""
def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v)