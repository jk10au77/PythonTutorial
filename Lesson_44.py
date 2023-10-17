"""
    List comprehensions:
    ----------------------
    a.  A simple and impressive way of creating lists and their contents
    
"""
list_1 = []

for ex in range(6):
    list_1.append(ex)

list_2 = [ex for ex in range(6)]        # list comprehension creating a list
print(list_1)
print(list_2)

"""
    b.  list comprehensions using a conditional expression
"""

the_list_1 = []
for x in range(10):
    the_list_1.append(1 if x % 2 == 0 else 0)
print(the_list_1)

the_list_2 = [1 if x % 2 == 0 else 0 for x in range(10)]  # list comprehension using conditional expressiom
print(the_list_2)

"""
    List comprehensions vs generators:
    ----------------------------------
    The bracket [] makes a list comprehesnions  whereas the parentheses () makes a generator
"""
the_list_3 = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
for v in the_list_1:
    print(v, end='')
print()
for v in the_generator:
    print(v, end='')