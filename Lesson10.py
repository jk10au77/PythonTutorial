"""
    Your task here is very special: you must design a vowel eater! Write a program that uses:
        a.  for loop
        b.  the concept of conditional execution (if-else-if)
        c.  the continue statement
    Your task here is very special: you must design a vowel eater! Write a program that uses:
        a.  ask the user to enter a wod
        b.  use user_word = user_word.upper() to convert the word entered by the user to upper case; 
            we'll talk about the so-called string methods and the upper() method
        c.  use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, 
            U from the inputted word;
        d.  print the uneaten letters to the screen, each one of them on a separate line.

    Change History:
        Version No:    Description
        a. 1.01        code to capture the uneaten word     



"""
word_without_vowels = ""                # Version 1.01
word = input("Enter a word: ")
user_word = word.upper()
for letter in user_word:
    if letter in ['A', 'E', 'I', 'O', 'U']:
       continue
    else:
        print(letter)
        word_without_vowels += letter   # Version 1.01
print("The end of printing the vowels. ")
print("Printing the word with out vowels: ", word_without_vowels)   # Version 1.01
print("***************************************************************")
print_without_vowels = "Printing the word without vowels: "         # Version 1.01
print(print_without_vowels, word_without_vowels)                    # Version 1.01



