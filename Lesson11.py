"""
    List: 
    ------
    a. collection of data
    b. list is assigned to one variable
    c. elements in the list are accessed using the index, first element has a index of 0.
    d. So list of n element has length of n

    Change history:
    ----------------
    S.No    Version     Description
    -------------------------------------
    1.          1.0     List definitions, length, and indexing

    
"""

my_list = []                                # empty list definition  
boys = ['Jaya', 'Dheeru', 'Raja']           # list with string value
numbers = [10, 5, 7, 2, 1]                  # list of numbers

# accessing elements in boys list
print(boys[0])                  #individual accessing and printing oth element of boys list
print(boys[2])                  # accessing and printing last element of boys list

# we can also access elements of a list iteratively by using for loop

for boy in boys:
    print(boy)  

print(len(boys))            # len() function returns the number of elements in boys list

# another way of accessing individual elements of a list
for i in range(len(numbers)):
    print(numbers[i])  