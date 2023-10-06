"""
    Dictionary:
    ------------
    1. Dictionary is another Python datastructures.
    2. It's not a sequence type.
    3. It is a mutable.
    4. Dictionary is set of key-value pair.

    Note:
    ------
    1.  each key must be unique - it's not possible to have more than one key of the same value;
    2.  a key may be any immutable type of object: it can be a number (integer or float), or even a string, 
        but not a list;
    3.  a dictionary is not a list - a list contains a set of numbered values, while a dictionary holds pairs 
        of values;
    4.  the len() function works for dictionaries, too - it returns the numbers of key-value elements in the 
        dictionary;
    5.  a dictionary is a one-way tool - if you have an English-French dictionary, you can look for French 
        equivalents of English terms, but not vice versa.

"""

dictionary = {"cat": "chat", "dog": "chien", "horse":"cheval" }
words = ["cat", "dog", "horse"]

for word in words:
    if word in dictionary:
        print(word, "----->", dictionary[word])
    else:
        print(word, "is not in dictionary.")


keys = [key for key in dictionary]       # foor loop can be used
print(keys)
values = [dictionary[key] for key in dictionary]
print(values)


"""
    Dictionay methods:
    --------------------
    a. items() - returns tuples where each tuple is a key-value pair.
    b. keys() - returns keys of a dictionary
    c. values() - returns values of a dictionary

"""
keys_new = [key for key in dictionary.keys()]
value_new = [value for value in dictionary.values()]
print(keys_new)
print(value_new)

"""
    modifying and adding values
    ----------------------------------
"""

dictionary["cat"] = "minow"         # replacing cat value with minow
print(dictionary)

dictionary["swan"] = "cygne"        # adding a swan as new element in the dictionary
print(dictionary)

# removing a key will always remove the associated value. Values cannot exist without key

del dictionary['dog']           # removes dog from dictionary
print(dictionary)

"""
    Tuples and dictionaries can work together:
    --------------------------------------------
    Problem definition:
    -------------------
        a.  you need a program to evaluate the students' average scores;
        b.  the program should ask for the student's name, followed by her/his single score;
        c.  the names may be entered in any order;
        d.  entering an empty name finishes the inputting of the data (note 1: entering an empty score will raise 
            the ValueError exception, but don't worry about that now, you'll see how to handle such cases when we 
            talk about exceptions in the second part of the Python Essentials course series)
        e   a list of all names, together with the evaluated average score, should be then emitted.
"""
school_class = {}
while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

