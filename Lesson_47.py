"""
                            Processing Files:
                        -------------------------
    a.  Every developer needs to know how to process data stored in files.
    b.  Python accesses and processes files using a set of objects.

    Files:
    ------
    a.  Different OS treat files in different ways.
    b.  Any program written in Python (and not only in Python, because that convention applies to virtually 
        all programming languages) does not communicate with the files directly, but through some abstract 
        entities that are named differently in different languages or environments - the most-used terms are 
        'HANDLES' or 'STREAMS' (we'll use them as synonyms here).
    C.  The programmer, having a more- or less-rich set of functions/methods, is able to perform certain 
        operations on the stream, which affect the real files using mechanisms contained in the operating 
        system kernel.
    d.  In this way, you can implement the process of accessing any file, even when the name of the file is 
        unknown at the time of writing the program.
    e.  The operations performed with the abstract stream reflect the activities related to the physical file.
    f.  To connect (bind) the stream with the file, it's necessary to perform an explicit operation.
        1.  opening file:   The operation of connecting the stream with a file is called opening the file.
        2.  closing file:   Disconnecting the stream with a file is called closing file.
        Note:   The conclusion is that the very first operation performed on the stream is always open and the 
                last one is close.

    File streams:
    -------------
    a.  The opening of file streams is not only associated with file, but also to the open mode. 
    b.  The manner in which the stream is processed is declared as an open mode.
    
    Stream Operations - There are 2 basic operations performed on the stream:
        1.  Read from the stream - portions of data are retieved from files and placed in a memory area managed 
            by the program (e.g. variables)
        2.  Write to the stream - portions of data from the memory (e.g. variable) are transferred to the file
    Basic modes used to open Stream - There are three modes used to open the stream:
        1.  Read mode -     A stream opened in read mode allows read operations only.  trying to write to the stream will cause an exception 
            (the exception is named UnsupportedOperation, which inherits OSError and ValueError, and comes from the io module); 
        2.  Write mode -    A  stream opened in this mode allows read operations only.  a stream opened in this mode allows read operations only
        3.  Update mode -   A stream opened in update mode allows both read and write operations.

    File Handles:
    -------------
    a.  Every file is an object of a class.
    b.  When a file is opened, an object of an adequate class is created
    c.  When a file is closed, object previous created at the time of opening operation is killed.
    d.  Between these two events, you can use the object to specify what operations should be performed on a particular stream.

    Based on the contents of stream, all streams are divided into two type
        a. Text streams       The text streams ones are structured in lines;
        b. Binary streams

        Text streams  
        ------------
        a   The text streams ones are structured in lines;
        b.  This file is written (or read) mostly character by character, or line by line.

        Binary streams:
        ---------------
        a.  The binary streams don't contain text but a sequence of bytes of any value. This sequence can be, for example, an executable 
            program, an image, an audio or a video clip, a database file, etc
        b.  Because these files don't contain lines, the reads and writes relate to portions of data of any size. Hence the data is 
            read/written byte by byte, or block by block, where the size of the block usually ranges from one to an arbitrarily chosen value.
        Note:
        -----
        a.  In Unix/Linux systems, the line ends are marked by a single character named LF (ASCII code 10) designated in Python programs as \n.
        b.  In windows systems, the end of line is marked by a pair of characters, CR and LF (ASCII codes 13 and 10) which can be encoded as 
            \r\n.

        Portable program: 
            a.  The trait of the program allowing execution in different environments is called portability. 
            b.  A program endowed with such a trait is called a portable program.
        Note:
        ----
            To make program portable, i.e. abiltiy to use the program in different OS, it was done at the level of classes. In the following manner
                a.  when the stream is open and it's advised that the data in the associated file will be processed as text (or there is no 
                such advisory at all), it is switched into text mode;
                b.  during reading/writing of lines from/to the associated file, nothing special occurs in the Unix environment, 
                    but when the same operations are performed in the Windows environment, a process called a translation of newline characters 
                    occurs: 
                        a.  when you read a line from the file, every pair of \r\n characters is replaced with a single \n character, and 
                            vice versa; 
                        b.  during write operations, every \n character is replaced with a pair of \r\n characters;
        
        Opening the streams:
        --------------------
        a.  open() function performs the stream opening operation as shown below

                stream = open(file_name, mode='r/w/u', encoding = None)

                a.  if the opening is successful, the function returns a stream object; otherwise, an exception is raised 
                    (e.g., FileNotFoundError if the file you're going to read doesn't exist);
                b.  the first parameter of the function (file) specifies the name of the file to be associated with the stream;
                c.  the second parameter (mode) specifies the open mode used for the stream
                d.  the third parameter (encoding) specifies the encoding type (e.g., UTF-8 when working with text files)
                e.  the opening must be the very first operation performed on the stream.

            Opening the streams: modes
            --------------------------
                a.  read mode or 'r':
                    ----------------
                    1.  the stream will be opened in read mode.
                    2.  the file associated with the stream must exist and has to be readable, otherwise the open() function raises an exception.
                
                b.  w  open mode: write:
                    --------------------
                    1.  the stream will be opened in write mode.
                    2.  the file associated with the stream doesn't need to exist; if it doesn't exist it will be created; if it exists, it will
                        be truncated to the length of zero (erased); if the creation isn't possible (e.g., due to system permissions) the open()
                        function raises an exception.
                
                c.  a open mode: append:
                    ---------------------
                    1.  the stream will be opened in append mode;
                    2.  the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created; 
                        if it exists the virtual recording head will be set at the end of the file (the previous content of the file remains 
                        untouched.)
                d.  r+ open mode: read and update
                    -----------------------------
                    1.  The stream will be opened in read and update mode;
                    2.  The file associated with the stream must exist and has to be writeable, 
                        otherwise the open() function raises an exception; 
                    3.  Both read and write operations are allowed for the stream.
                
                e.  w+ open mode: write and update
                    -------------------------------
                    1.  The stream will be opened in read and update mode;
                    2.  The file associated with the stream must exist and has to be writeable, otherwise the open() function raises an 
                        exception;
                    3.  Both read and write operations are allowed for the stream.

            Selecting text and binary modes:
            --------------------------------
                a.  If there is a letter b at the end of the mode string it means that the stream is to be opened in the binary mode.
                b.  If the mode string ends with a letter t the stream is opened in the text mode.Text mode is the default one
            
            Note:   Finally, the successful opening of the file will set the current file position (the virtual reading/writing head) before 
                    the first byte of the file if the mode is not a and after the last byte of file if the mode is set to a.
            
                    -------------------------------------
                    Text mode	Binary mode	Description
                    -------------------------------------

                1.      rt	        rb	    read
                2.      wt	        wb	    write
                3.      at	        ab	    append
                4.      r+t	        r+b	    read and update
                5.      w+t	        w+b	    write and update

            Note:   You can also open a file for its exclusive creation. You can do this using the x open mode. If the file already exists, 
                    the open() function will raise an exception.

"""
