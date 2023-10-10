"""
                    Strings 
                    -------
    a. Python strings are immutable
    b. Python strings are sequences. 
    c. Python strings aren't lists, but you can treat them like lists in many particular cases.
    """

# Example 1

word = 'by'
print(len(word))


# Example 2

empty = ''
print(len(empty))


# Example 3

i_am = 'I\'m'
print(len(i_am))

# The multiline strings can be delimited by triple quotes,
multiline = '''Line #1
Line #2'''                  # the string spans into 2 lines

print(len(multiline))


"""
    String operations:
    ------------------
    a. string concatenation performed by +
    b. string replication performed by *
    c. Indexing
    d. slicing
    e. The in operator
    f. The not in operator

    Note:   The ability to use the same operator against completely different kinds of data (like numbers vs. strings) 
            is called overloading (as such an operator is overloaded with different duties).
    """

str1 = 'a'
str2 = 'b'

print(str1 + str2)      # string concatenation
print(str2 + str1)      # string concatenation
print(5 * 'a')          # string replication
print('b' * 4)          # string replication

# Demonstration of ord() and char() functions
char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))      # return ASCII/UNICODE code point value of a specific character here a's UNICODE is returned
print(ord(char_2))      # return ASCII/UNICODE code point value of a specific character here space's UNICODE is returned

# Demonstrating the chr() function.

print(chr(97))          # returns the character of a specific code point. here it returns character of code point 97
print(chr(945))          # returns the character of a specific code point. here it returns character of code point 945

"""
    Strings as sequences: indexing
    ------------------------------
    a.  Strings aren't lists, but you can treat them like lists in many particular cases.
    b.  characters in string can be accessed by using indexing.
"""

# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')
    
print()

# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

# The in operator
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("The in operator.")
print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)
print("The not in operator.")
print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)


"""     
    Python strings are immutable:
    -----------------------------------
    a. we can't use append(), insert() methods as strings are immutable.
    b. As a whole, the string can be deleted using del operator. But can't delete characters from a string

"""
"""
    String functions:
    -----------------
    1. min() - finds the minimum element of the sequence passed as an argument.
    2. max() - finds the maximum element of the sequence passed as an argument.
    3. index() -  returns the index of the first occurrence of the argument. Its absence will cause ValueError exception
    4.  list() -  creates a new list containing all the string's characters, one per list element.
    5. count() - returns the counts all occurrences of the element inside the sequence 


"""
# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Demonstrating the list() function:
print(list("abcabc"))

# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))

"""
    string methods:
    ---------------
    a. capitalize() -   if the first character inside the string is a letter (note: the first character is an 
                        element with an index equal to 0, not just the first visible character), it will be 
                        converted to upper-case; all remaining letters from the string will be converted to 
                        lower-case.
            Note:   
            ----    the original string (from which the method is invoked) is not changed in any way (a string's 
                    immutability must be obeyed without reservation)
                    the modified (capitalized in this case) string is returned as a result - if you don't use it 
                    in any way (assign it to a variable, or pass it to a function/method) it will disappear without 
                    a trace.
    
    b. center()     -   centers the string by adding some spaces before and after the string.
    c. endswith()   -   checks if the given string ends with the specified argument and returns True or False, 
                        depending on the check result.
    d.  find()      -   it looks for a substring and returns the index of first occurrence of this substring, 

    e.  isalnum()   -   checks if the string contains only digits or alphabetical characters (letters), and 
                        returns
    
"""
# Demonstrating the capitalize() method:
print("capitalize() method")
print('aBcD'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

# Demonstrating the center() method:
print("center() method")
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')

# Demonstrating the endswith() method:
print("endswith() method")
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

# Demonstrating the find() method:
print("find() method")
print("Eta".find("ta"))
print("Eta".find("mma"))

# Demonstrating the isalnum() method:
print("isalnum() method")
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

# Demonstrating the isalpha() method:
print("isalpha() method")

print("Moooo".isalpha())
print('Mu40'.isalpha())

# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())

















