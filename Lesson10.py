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
"""

word = input("Enter a word: ")
user_word = word.upper()
for letter in user_word:
    if letter in ['A', 'E', 'I', 'O', 'U']:
       continue
    else:
        print(letter)


