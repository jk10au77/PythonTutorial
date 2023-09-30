"""
    The bubble sort:
    -----------------
"""

import random       # random generator module 

user_count = int(input("Enter the total number of numbers in a list: "))
my_list = []
swapped = True
# list generation using the random generator
for i in range(user_count):
    number = random.randint(100, 1000)
    my_list.append(number)

print(my_list)
print('********************************************************************************************************')
# to sort the my_list by implementing the bubble sort
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):                                   # we need n - 1 comparsions
        if my_list[i] > my_list[i + 1]:                                 # compare adjacent elements
            swapped = True                                              # a swap occured
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]     # # compare adjacent elements
            print(my_list)
print(my_list)
print('*******************************************************************************************************')