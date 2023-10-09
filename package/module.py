"""
print("I like to be a module.")
print(__name__)
"""
"""
if __name__ == "__main__":
    print("I prefer to be a module.")
else:
    print("I like to be a module.")
    """
"""
step9:

"""
__counter = 0

def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

if __name__ == "__main__":
    print("Introducing such a variable is absolutely correct, but may cause important side effects that you must be aware of.")
    my_list = [i + 1 for i in range(5)]
    
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)
