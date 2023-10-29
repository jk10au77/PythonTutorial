"""
    Some topics:
    -------------
    a.  map() function
    b.  filter() function
    c.  reduce() function


"""

"""
    The map() function:
    -------------------
    a.  It is a built-in fucntion.
    b.  map function is used to process all items in an iterable without using an explicit for loop. This 
        technique is known as mapping
    c.  It is useful when you need to apply a transformation function to each item in an iterable and 
        transform them into a new iterable.
    d.  The map() function is one of the tools that supports a functional programming style in Python

    Syntax:
    ---------
    map(function_Object, iterable[, iterable_1, iterable_2, ..., iterable_N])

    map() returns a map object, which is an iterator that yields items.

"""

def square(number):
    return number ** 2

number = [i for i in range(1, 6)]
squared = map(square, number)
print(list(squared))

"""
Expalination: 
-------------
a.  square() is a transformation function that maps a number to its square value. 
b.  The call to map() applies square() to all of the values in numbers and returns an iterator 
    that yields square values. 
c.  Then you call list() on map() to create a list object containing the square values.

"""

# Another example. here you need to convert a string to an integer numebr.

str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
int_nums = map(int, str_nums)
print(list(int_nums))

"""
    Note:
    ----
    a.  You can use any kind of Python callable with map(). The only condition would be that the callable 
        takes an argument and returns a concrete and useful value. 
        For example, you can use classes, instances that implement a special method called __call__(), 
        instance methods, class methods, static methods, and functions.
    b.  You can use any built-in function with map(), provided that the function takes an argument and 
        returns a value.
    c.  
    
"""
words = ["Welcome", "to", "Real", "Python"]

words_len = list(map(len, words))
print(words_len)

"""
    Transforming iterables of string objects with Python's map() function:
    ----------------------------------------------------------------------
    If you're dealing with iterables of strings and need to apply the same transformation to each string, 
    then you can use map() along with various string methods:

"""
string_it = ["processing", "strings", "with", "map", "function"]

str_capitalize = map(str.capitalize, string_it)
print(list(str_capitalize))
str_upper = map(str.upper, string_it)
print(list(str_upper))


"""
    Combining map() function with Other functional Tools:
    -----------------------------------------------------
    If you're dealing with iterables of strings and need to apply the same transformation to each string, 
    then you can use map() along with various string methods:
"""

"""
    coding with pythonic style: replacing map()
    -------------------------------------------
    a.  Functional programming tools like map(), filter(), and reduce() have been around for a long time. 
        However, list comprehensions and generator expressions have become a natural replacement for them 
        almost in every use case.
    b.  For example, the functionality provided by map() is almost always better expressed using a list 
        comprehension or a generator expression. 

# Generating a list with map
list(map(function, iterable))

# Generating a list with a list comprehension
[function(x) for x in iterable]

The list comprehension almost always reads more clearly than the call to map(). Since list comprehensions 
are quite popular among Python developers, it’s common to find them everywhere. So, replacing a call to 
map() with a list comprehension will make your code look more familiar to other Python developers.

"""

# Transformation function

def square(number):
    return number ** 2

numbers = [1,2,3,4,5,6,7,8,9]

# using map()
print(list(map(square, numbers)))

# using a list comprehension
print([square(num) for num in numbers])


"""
    Using generator expressions:
    ----------------------------
    a.  we know map() returns a map object, which is an iterator that yield items on demand. So, the natural
        replacement for map() is a generator expression because generator expressions return generator 
        objects, which are also iterators that yield items on demand.
    b.  Python iterators are known to be quite efficient in terms of memory consumption. This is the reason 
        why map() now returns an iterator instead of a list.
    c.  difference between a list comprehension and a generator expression. 
        1.  List comprehension uses a pair of square brackets to delimit the expression.
        2.  The generator expression uses a pair of parenthesis ()
        3.  So, to turn a list comprehension into a generator expression, you just need to replace the square 
            brackets with parentheses.

"""

# You can use generator expressions to write code that reads clearer than code that uses map(). 

gen_exp = (square(x) for x in numbers)
print(list(gen_exp))

