"""
    Writng content to text file
    ---------------------------
    a.  write("string_to_be_transferred") - writes the string_to_be_transferred to an open file.
    b.  No newline character is added to the write()'s argument. So we have to add 
    Note:   Writing a file opened in the read mode raises an error


"""

from os import strerror

try:
    fo = open("C:\\Users\\tatip\\OneDrive\\Desktop\\write.txt", 'wt')   # a new file (write.txt) is created.
    for i in range(10):
        s = "line #" + str(i + 0) + "\n"
        for ch in s:
            fo.write(ch)
    fo.close()
except IOError as e:
    print("IOError occured: ", strerror(e.errno))

# we have opened the above created write file to view its contents.
try:
    cnt = 0
    s = open('C:\\Users\\tatip\\OneDrive\\Desktop\\write.txt', 'rt')
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nTotal characters in file: ", cnt)
except IOError as e:
    
    print("I/O error occured: ", strerror(e.errno))