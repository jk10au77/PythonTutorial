"""
        Iterators:
        -------------------
        Iterator protocol:
        -------------------
        a.  Iterator protocol is a way in which an object should behave to conform to the rules imposed by
            context of the 'for' and 'in' statements
        b.  An object conforming to the iterator protocol is called an iterator.
        
        An iterator must provide two methods:
            a.  __iter__() - should return the object itself. It is invoked only once. It is needed for Python
                to successfully start the iteration process.
            b.  __next__() - returns the next value of the desired series. It will be invoked by 'for' 
                statement and 'in' statement.
                If there are no more values to provide, the method should raise the StopIteration exception.
    """

class Fib:
    def __init__(self, nn):
 #       print("__init__")
        self.__n = nn           # stores the series limit
        self.__i = 0            # tracks the current fibonacci number to provide
        self.__p1 = self.__p2 =  1   # saves the two previous numbers.

    def __iter__(self):
#        print("__iter__")
        return self
    
    def __next__(self):         # here you place your logic for next element
#        print("__next__")				
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret
"""    
for i in Fib(10):
    print(i)

fib_ser = [i for i in Fib(10)]          # list comprehension
print(fib_ser)
"""

class Class:
    def __init__(self, n):
        self.__iter = Fib(n)
    
    def __iter__(self):
        print("Class iter")
        return self.__iter

    
object = Class(8)
for i in object:
    print(i)

# Exercise_1:   What is the expected output of the following code?
class Vowels:
    def __init__(self):
        self.vow = 'aeiouy'         ## Yes, we know that y is not always considered a vowel.
        self.pos = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]

vowels = Vowels()
for v in vowels:
    print(v, end=' ')

    



