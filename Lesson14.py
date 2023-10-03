"""
    List slicing:
    ------------
    a. Slicing is used to make new copy of list, or parts of list
    b. It actually copies the list's contents, not the list name

    Syntax:
    -------
    list_name[start: end]

        Notation:
        ----------
        a. start : is the index of the first element included in the slice
        b. end: is the index of the first element not included in the slice. not to end but to (end - 1). 
            end is the first element which does not take part in the slicing.
        c. The new list will have (start - end) elements

"""

list_1 = [1]
list_2 = list_1[:]          #   copies the entire list elements to a new list
print(list_1)               #   prints the original list
print(list_2)               #   prints the new list
print('Copying some part of the list')
my_list = [10,8,6,4,2]
new_list = my_list[1:3]     # Copies second element to the third element.
print(my_list)
print(new_list)

print("Slices - negative indices")
new_list = my_list[1:-1]
print(new_list)

"""
    Negative slicing:
    -----------------
    1. If the start specifies an element lying further than the one described by the end 
        (from the list's beginning point of view), the slice will be empty
"""
new_list = my_list[-1: 1]
print(new_list)

"""
    If you omit the start in your slice, it is assumed that you want to get a slice beginning 
    at the element with index
    my_list[0:end]
"""
new_list = my_list[:5]
print(new_list)

"""
    a. The 'in' operator: checks whether the element is in the list or not 
        i.e. checks the membership of an element in the list. If the element is in the list, you will get True
        else False
    b. The "not in' operator: just opposite to the 'in' operator. You will get True if the element is not in the 
        list, else you will get False
"""

my_list = [0, 3, 5, 12, 8, 2]
print(5 in my_list)
print('5' in my_list)
 
print(5 not in my_list)
print('5' not in my_list)

"""
    Lists - some simple programs

"""
print('Code to find the largest number in the list')
print('one way of finding the largest number in a list using for loop')
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest_number = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > largest_number:
        largest_number = my_list[i]
print(largest_number)
largest_number = my_list[0]
print('Second way of finding the largest number in a list using for loop')
for i in my_list[1:]:       # using slicing concept
    if largest_number < i:
        largest_number = i
print(largest_number)

"""
    Lists - again some simple programs
"""
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)
