"""
    pprint module:
    -------------

"""
"""
from urllib import request
response = request.urlopen("https://jsonplaceholder.typicode.com/users")
json_response = response.read()

import json
users = json.loads(json_response)
print(users)    # prints the users in an awkward passion
print('-----------------------------------')
for user in users:
    print(user)
    print('+++++++++++++++++++++++++++++++++++++++++++')
print('------------------------------------')
"""

"""
    Working with pprint:
    --------------------
    
pprint:
-------
1.  pprint is Python module
2.  pprint is made to print data structures in a pretty way.
3.  Before using pprint, you need to import pprint() function from pprint module.

"""
"""
from pprint import pprint
print("Pretty printing user using pprint function.")
pprint(users)   # This function prints users—but in a new-and-improved pretty way
"""
"""
    Exploring Optional Parameters of pprint():
    ------------------------------------------
    pprint module defines one class:
    ++++++++++++++++++++++++++++++++++++++++

    class pprint.PrettyPrinter(indent=1,
                                width=80,
                                depth=None,
                                stream=None,
                                compact=False,
                                sort_dicts=True,
                                underscore_numbers=False)
    ---------------------------------------------------------------------------------------------
    a.  contruct a PrettyPrint instance. This construct understands several keyword parameters.
    b.  There are seven parameters that you can use to configure your Pythonic pretty printer.
            1.  depth:  
            2.  indent:
            3.  width:
            4.  stream: 
            5.  compact:
            6.  sort_dict:
            7.  underscore_numbers:

depth:
------
    a. controls number of nesting levels to be printed; 
    b. if the data structure to be printed is too deep, the next contained levels is replaced by ....
    c. By default, there is no constraint on the depth of the objects to be formatted.

width:  limits the line length
-----
    a.  default value is 80
    b.  specifies the number of characters to be printed per line in the output.

compact:    default is compact = False
---------
    a.  squeezes the sequences
    b.  if compact = False, then each item of a sequence will be formatted in a seperate line. 
    c.  if compact = True, then as many items as will fit within the width will be formatted on each line.

indent:
-------
    a.  indent = 1 is the default
    b.  specifies the amount of indentation added for each nesting level.

stream: direct the output to the specified destination
-------
    a.  (default is sys.stdout) is a file-like object. 
    b.  The output will be written by calling write() method. 

sort_dicts: 
-----------
    a.  sort_dicts = True is the default specifies to sort dictionaries with key sorted.
    b.  sort_dicts = False ==> displays diction in insertion order. i.e. prevents the dictionary sorting

underscore_numbers: prettifing your numbers with underscores.
-------------------
    a.  underscore_numbers = False is the default. ntegers will not be formatted with the _ character for a thousands separator,
    b.  underscore_numbers = True, integers will be formatted with the _ character for a thousands separator,

        
"""
# Example
"""
import pprint
import json
from urllib.request import urlopen

with urlopen('https://pypi.org/pypi/sampleproject/json') as resp:
    project_info = json.load(resp)['info']

pprint.pprint(project_info)

"""
"""
    Creating a custom PrettyPrinter object:
    ---------------------------------------

        a.  it is possible to create an instance of PrettyPrinter that has defaults you’ve defined.
        b.  Once you have this new instance of your custom PrettyPrinter object, you can use it by calling the .pprint() method on the 
            PrettyPrinter instance
"""

# creates a custom PrettyPrint object
import pprint
custom_printer = pprint.PrettyPrinter(indent=4,
                               width=100,
                               depth=2,
                               sort_dicts=True,
                               underscore_numbers=True,
                               compact=False)   


from urllib import request
import json

response = request.urlopen("https://jsonplaceholder.typicode.com/users")
json_response = response.read()


users = json.loads(json_response)
custom_printer.pprint(users[1])

number_list = [123456789, 10000000000000000000000000000]
custom_printer.pprint(number_list)