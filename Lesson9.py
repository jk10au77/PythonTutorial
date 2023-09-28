"""
    The for loop performs the following:
        a.  count the "turns" of the loop than to check the conditions.
        b.  browse" large collections of data item by item.

"""

# Take a look at the snippet below. 
# Here the loop executes 10 times starting from 0 to the last control 9.
"""
for i in range(10):
    print("The value of i is ", i)
"""

"""
    More about for loop.
        a. The range() function may accept three arguments as range(2, 8, 3)
            the third argument is an increment starting from 2
"""
for count in range(2, 8, 3):
    print("The value of count is ", count)
    