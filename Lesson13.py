"""
    a.  Lists (and many other complex Python entities) are stored in different ways than ordinary (scalar) variables.
        i.e. We could say that:
            1.  the name of an ordinary variable is the name of its content;
            2.  the name of a list is the name of a memory location where the list is stored.

"""

list_1 = [1]             
print(list_1[0])
list_2 = list_1         # assigns the memory location of the list_1 to list_2, content in the list_1 is not copied.
print(list_2[0])           # list_1 and list_2 identify the same location in the computer memory
list_1[0] = 3                        
print(list_2[0])           # modifying one affects the other.

# Then how do we copy?
