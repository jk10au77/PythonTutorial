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
    f. lower()      -   makes a copy of a source string, replaces all upper-case letters with their lower-case 
                        counterparts, and returns the string as the result. Again, the source string remains untouched.
                        If the string doesn't contain any upper-case characters, the method returns the original string.
                        If the string doesn't contain any upper-case characters, the method returns the original string.
    g.  lstrip()    -   removes all leading whitespaces and returns a newly created string

    h.  rstrip()    -   removes all trailing whitespaces and returns a newly created string

    i.  replace()   -   returns a copy of the original string in which all occurrences of the first argument have been 
                        replaced by the second argument.
                        If the second argument is an empty string, replacing is actually removing the first argument's 
                        string.
                        The three-parameter replace() variant uses the third argument (a number) to limit the number of 
                        replacements.     
    j.  split()     -   lits the string and builds a list of all detected substrings.
                        The method assumes that the substrings are delimited by whitespaces.
    k   startswith() -   return True if a given string starts with the specified substring. else returns False


    l   endswith()  -   return True if a given string ends with the specified substring. else returns False

    m   strip()     -   combines the effects caused by rstrip() and lstrip() - 
                        it makes a new string removing all the leading and trailing whitespaces.
    n   swapcase()  -   makes a new string by swapping the case of all letters within the source string: 
                        lower-case characters become upper-case, and vice versa.
                        All other characters remain untouched.
    o   title()     -   changes every first letter of every word to upper case a,d turns all other characters to 
                        lower-case
    
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

# Demonstrating the lower() method:
print("*******************************lower() method.***************************")
print("SiGmA=60".lower())

# Demonstrating the lstrip() method:
print("*******************************The lstrip() method.**********************")
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))

# Demonstrating the rstrip() method:
print("******************rstrip() method. **************************************")
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

# Demonstrating the strip() method:
print("****************** strip() method. **************************************")
print("[" + "   aleph   ".strip() + "]")

# Demonstrating the swapcase() method:
print("******************* swapcase() method. ***********************************")
print("I know that I know nothing.".swapcase())

print()

# Demonstrating the title() method:
print("******************* title() method. ***********************************")
print("I know that I know nothing. Part 1.".title())

print()


# Demonstrating the replace() method:
print("************************The replace() method.****************************")
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

# Demonstrating the split() method:
print("************************The split() method.****************************")
print("phi       chi\npsi".split())

# Demonstrating the startswith() method:
print("************************ The startswith() method. **********************")
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

# Demonstrating the endswith() method:
print("************************ The endswith() method. **********************")
print("omega".startswith("ga"))
print("omega".startswith("om"))

print()

"""
    The join() method:
    ------------------
    a.  The join() method performs a join - it expects one argument as list and the elements of list must be string only.
        Otherwise, it will raise a TypeError exception.
    b.  All the list elements will be joined into one list but the string from which the method has been invoked is used 
        as a seperator, put among the strings.
    c.  The newly created string is returned as a result.
"""

# Demonstrating the join() method:
print("******************************The join() method.****************************")
print(",".join(["omicron", "pi", "rho"]))   # returns omicron,pi,rho

"""
    Key takeaways:
    --------------
    1. Some of the methods offered by strings are:

    a.  capitalize()-   changes all string letters to capitals;
    b.  center()    -   centers the string inside the field of a known length;
    c.  count()     -   counts the occurrences of a given character;
    d.  join()      -   joins all items of a tuple/list into one string;
    e.  lower()     -   converts all the string's letters into lower-case letters;
    f.  lstrip()    -   removes the white characters from the beginning of the string;
    g.  replace()   -   replaces a given substring with another;
    h.  rfind()     -   finds a substring starting from the end of the string;
    i.  rstrip()    -   removes the trailing white spaces from the end of the string;
    j.  split()     -   splits the string into a substring using a given delimiter;
    k.  strip()     -   removes the leading and trailing white spaces;
    l.  swapcase()  -   swaps the letters' cases (lower to upper and vice versa)
    m.  title()     -   makes the first letter in each word upper-case;
    n.  upper()     -   converts all the string's letter into upper-case letters.

    2. String content can be determined using the following methods (all of them return Boolean values):

    a.  endswith()  -  does the string end with a given substring?
    b.  isalnum()   -  does the string consist only of letters and digits?
    c.  isalpha()   -  does the string consist only of letters?
    d.  islower()   -  does the string consists only of lower-case letters?
    e.  isspace()   -  does the string consists only of white spaces?
    f.  isupper()   -  does the string consists only of upper-case letters?
    g.  startswith() - does the string begin with a given substring?

"""

"""
    Exercises:  What is the expected output of the following snippet code?
"""
print("******************** Exercises_1. **********************************")
for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')

print("******************** Exercises_2. **********************************")

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2[-2])

print("******************** Exercises_3. **********************************")

the_list = ['Where', 'are', 'the', 'snows']
s = '*'.join(the_list)
print(s)

print("******************** Exercises_4. **********************************")
s = "It is either easy or impossible."
s = s.replace('easy', 'hard').replace('im', '')
print(s)

"""
    comparing strings:
    -------------------
    Python's strings can be compared using the same set of operators which are in use in relation to numbers.
        1.  == (equal to)
        2.  !=  (not equal to)
        3.  >   (greater than)
        4.  >=  (lgreater than or equal to)
        5.  <   (less than)
        6.  <=  (less than or equal to)
    
    Note:   The results of such comparisons may sometimes be a bit surprising. Don't forget that Python is not aware 
            (it cannot be in any way) of subtle linguistic issues - it just compares code point values, character by 
            character.
            Two strings are equal when they consist of the same characters in the same order.
            The final relation between strings is determined by comparing the first different character in both strings 
            (keep ASCII/UNICODE code points in mind at all times.)
            When you compare two strings of different lengths and the shorter one is identical to the longer one's 
            beginning, the longer string is considered greater.
            String comparison is always case-sensitive (upper-case letters are taken as lesser than lower-case).
"""
# Even if a string contains digits only, it's still not a number. 
print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')


















