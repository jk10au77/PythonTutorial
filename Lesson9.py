"""
    The for loop performs the following:
        a.  count the "turns" of the loop than to check the conditions.
        b.  browse" large collections of data item by item.

    Change history:
    --------------
        Version Number  Description
        --------------  -------------------------------------------------------------------------
            1.01        Added code to print various pyramids

"""

# Take a look at the snippet below. 
# Here the loop executes 10 times starting from 0 to the last control 9.

#Start of initial commit version 

"""    
for i in range(10):
    print("The value of i is ", i)

'''
    More about for loop.
        a. The range() function may accept three arguments as range(2, 8, 3)
            the third argument is an increment starting from 2
'''
for count in range(2, 8, 3):
    print("The value of count is ", count)
"""
# End of intial commit

# Start of version 1.01
'''
row_number = int(input("Enter the number of rows to be printed with *: "))
for i in range(1, row_number+1):
    for j in range(i, i+1):
        print_row = '*' * j 
        print(print_row, end = ' ')
    print('\n')
'''

# printing pyramid with numbers

row_number = int(input("Enter the number of rows: "))
for i in range(1, row_number + 1):
    for j in range(1, i+1):
        print(j, end = '')
    print('\n')
#End of version 1.01