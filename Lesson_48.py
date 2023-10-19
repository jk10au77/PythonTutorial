"""     Working with real text files: Opening and reading a text file
        -----------------------------
If applied to a text file, the function is able to:
	a. read a desired number of characters (including just one) from the file, and return them as a string;
	b. read all the file contents, and return them as a string;
	c. if there is nothing more to read (the virtual reading head reaches the end of the file), the function returns an empty string.
"""

from os import strerror

try:
    cnt = 0
    s = open('C:\\Users\\tatip\\OneDrive\\Desktop\\test.txt', 'rt')
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nTotal characters in file: ", cnt)
except IOError as e:
    
    print("I/O error occured: ", strerror(e.errno))
    

"""
	Use readline() method if we want to treat the file contents as a set of lines.
    readline() - reads a complete line of text from the file. and returns line as a string 

"""
try:
    lccnt =lcnt = tccnt = 0					# cnt stores chr count whereas lcnt stores the line count
    s = open('C:\\Users\\tatip\\OneDrive\\Desktop\\test.txt', 'rt')	
    line = s.readline()
    
    while line != '':
        
        lcnt += 1
        for ch in line:
            lccnt += 1
        print("\nTotal number of characters in line", + lcnt, " :", lccnt)
        tccnt += lccnt
        lccnt -= lccnt            
        line = s.readline()
    s.close()
    print("\n\nTotal characters in file: ", tccnt)
    print("Total lines in file: ", lcnt)
except IOError as e:
    print("I/O Error occured: ", strerror(e.errno))
    
"""
	readlines() - read all the file contents, and returns a list of strings, one element per file line.

"""

try:
    ccnt = lcnt = 0
    s = open('C:\\Users\\tatip\\OneDrive\\Desktop\\test.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))