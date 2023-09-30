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
    1.          1.01    List definitions, length, and indexing.
    2.          1.02    Difference between functions and methods.
    3.          1.03    List operations:
                        a. Adding elements to a list using append(), insert() methods
                        b. finding the number of elements in a list - len() method
    4.          1.10    Exercise on list
    5.          1.11    Key takeaways
    
"""

my_list = []                                # empty list definition  
boys = ['Jaya', 'Dheeru', 'Raja']           # list with string value
numbers = [10, 5, 7, 2, 1]                  # list of numbers

# accessing elements in boys list
print(boys[0])                  #individual accessing and printing oth element of boys list
print(boys[2])                  # accessing and printing last element of boys list
print('*************************************')
# we can also access elements of a list iteratively by using for loop

for boy in boys:
    print(boy)  

print(len(boys))            # len() function returns the number of elements in boys list
print('*************************************')
# another way of accessing individual elements of a list
for i in range(len(numbers)):
    print(numbers[i])  
print('*************************************')

#   Version 1.02 - Difference between functions and methods
"""
-----------------------------------------------------------------------------------------------------
    Functions Vs Methods:                            
-----------------------------------------------------------------------------------------------------
1. A function doesn't belong to any data whereas Methods is a specific kind of data.
2. A function is owned by the whole code whereas a method is owned by data it works for.
3. Function invocation looks like function_name(with arguments or without arguments)
   method invocation looks like data.method(with arguments or without arguments)
4. Method will behave like a function, but can do even more - it can change the internal state of 
   the data from which it has been invoked. 
                           
"""

"""
    Adding elements to a list:
    -------------------------------------------------------------------------------------------------------
    a. append() method --- adds element to end of a list. The list length is increased after the element is 
                           appended to a list.
    b. insert(location, value) --- inserts an element at location.
    c. len() method    --- gives the number of elements present in a list.

"""

# adding chaitanya to the end of boys list
boys.append('chaitanya')
print(boys)

# adding element using the insert() method
# insert() method - inserts an element anywhere in the list.
# insert(location, element_value) 

boys.insert(1, "sai")   # inserts sai at location 1 (index 1) 
print(boys)
print('*************************************')
print(len(boys))        # prints the length of a list
print('*************************************')
"""
    Making use of lists.

    The for loop has a special variant that process list effective
"""
# one way of accessing elements in a list.

for boy in boys:
    print(boy)              # prints the value in the boy variable

# another way of accessing elements in a list.
print('*************************************')
for i in range(len(boys)):
    print(boys[i])              # implements indexing for accessing element in a list
print('*************************************')

"""
    Version 1.10 - Exercise on list
    ----------------------------------------
    Scenario: The Beatles were one of the most popular music group of the 1960s, and 
    the best-selling band in history. Some people consider them to be the most influential 
    act of the rock era. Indeed, they were included in Time magazine's compilation of the 
    20th Century's 100 most influential people.

    The band underwent many line-up changes, culminating in 1962 with the line-up of John 
    Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).

    Write a program that reflects these changes and lets you practice with the concept of lists. 
    Your task is to:
        step_01:    create an empty list named beatles;
        step_02:    use the append() method to add the following members of the band to the list: 
                    John Lennon, Paul McCartney, and George Harrison
        step03:     use the for loop and the append() method to prompt the user to add the following 
                    members of the band to the list: Stu Sutcliffe, and Pete Best;
        step04:     print the beatles one element at a time
"""

beatles = []                        # step01
beatles.append('John Lennon')       # step02
beatles.append('Paul McCartney')    # step02
beatles.append('George Harrison')   # step02

for i in range(2):
    name = input("Enter the 'Stusutcliffe' and 'PeteBest' words seperately in two iterations:")
    beatles.append(name)
print('*************************************')
for guy in beatles:
    print(guy)

"""
    Version 1.11 - Key takeaways
    ----------------------------------
    1.  The list is a type of data in Python used to store multiple objects. It is an ordered and 
        mutable collection of comma-separated items between square brackets.
    2.  Lists can be indexed and updated.
    3.  Lists can be nested like my_list = [1, 'a', ["list", 64, [0, 1], False]]
    4.  List elements and lists can be deleted
    5.  Lists can be iterated through using the for loop
    6.  The len() function may be used to check the list's length
    7.  
"""