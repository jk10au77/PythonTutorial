"""
    a.  Amorphous data: is data which have no specific shape or form. They are just a series of bytes.
    b.  Phyton uses one of the specialized classes to store amorphous data.
    c.  Amorphous data cannot be stored using any of the previously presented means - they are neither 
        strings nor lists.
    d.  There should be a special container able to handle such data.
    e.  Python has more than one such container - one of them is a specialized class name bytearray - 
    f.  bytearray - it's an array containing (amorphous) bytes.
    f. 

"""

# creating a bytearray object
data = bytearray(10)    # creates a bytearray object to store 10 bytes. Python has more than one such container - one of them is a specialized class name bytearray - as the name suggests, it's an array containing (amorphous) bytes.
for i in data:
    print(i)
print("--------------------------------")
for i in range(len(data)):
    data[i] = 10 - i
for b in data:
    print(b )
    print(hex(b))
print("--------------------------------")

"""         characteristics of bytearray object
            -----------------------------------
    Bytearray objects resemblem list in many aspects.
        a.  Bytearrays are mutable.
        b.  Conventional indexing can be used to access any element of bytearray object
        c.  We can use len() function to find the length of a bytearray object
        d.  We must not set any byte array element with a value other than integer. 
            violating this rule will cause a TypeError exception
        e.  you're not allowed to assign a value that doesn't come from the range 0 to 255 inclusive
        f.  treat any byte array elements as integer values 
"""

"""
            how to write a byte array to a binary file 
            ------------------------------------------
a.  first, we initialize bytearray with subsequent values starting from 10; 
    if you want the file's contents to be clearly readable, replace 10 with something like ord('a') -
    this will produce bytes containing values corresponding to the alphabetical part of the ASCII code 
b.  then, we create the binary file using the open() function - the only difference compared to the previous 
    variants is the open mode containing the b flag;
c.  the write() method takes its argument (bytearray) and sends it (as a whole) to the file;
d.  the stream is then closed in a routine way.
The write() method returns a number of successfully written bytes.

"""

from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + 1

try:
    bf = open("C:\\Users\\tatip\\OneDrive\\Desktop\\file.bin", "wb")
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O Error occured: ", strerror(e.errno))

"""
            How to read bytes from a stream
            -------------------------------
    readinto() - read from a binary file 
"""