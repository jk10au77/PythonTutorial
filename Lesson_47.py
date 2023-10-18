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
    
"""
