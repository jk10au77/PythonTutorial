"""     
                            Package Tutorial
                            ----------------
    Resources:
    ----------
    a.  https://www.scaler.com/topics/python/python-packages/
    Overview:   
    ---------
        We usually organize our files in different folders and subfolders based on some criteria, so that 
        they can be managed easily and efficiently. It's just like an organization of your person files in
        you laptop.

    Definition:
    -----------
    a.  Python packages contain several modules. In simpler terms, Package in Python is a folder that contains 
        various modules as files.
    b.  Packages do the work of organizing files in Python.
    c.  Physically a package is a folder containing sub-packages or one or more modules (or files).
    d.  Packages provide a well-organiztional hierarchy modules in Python. 
    e.  Packages usually are named such that their usage is apparent to the user. 
    f.  Python packages ensure modularity by dividing the packages into sub-packages, making the project easier 
        to manage and conceptually clear.
    g.  Every package in Python must contain an __init__.py file because it identifies the folder as a package. 
        It generally contains the initialization code but may also be left empty.
    
    ------------------------------------------------------------

    Your first module:
    --------------------------
    Step1:  Create an empty file. Let's create module.py file in the Package folder
    Step2:  Create another empty file called main.py in the same folder.
            Run the main.py folder. 
                a.  Observe the folder. You do not notice anything.
                b.  In the main.py file add the 'import module' statement. Save and run.
                c.  Observe that a new subfolder '__pycache__' has been created in the same folder.
                d.  Open the __pycache__ folder. You observe that 'module.cpython-311.pyc' file has been created.
                    The general nomenclature of the above file is  module.cpython-xy.pyc where x and y are 
                        its derived from your python version. Here our Python version is 3.11
                    The name of the file is same as your module's name (here module).
                    The part after the first dot says which Python implementation has created the file (CPython here) and 
                        its version number. 
                    The last part (pyc) comes from the words Python and compiled.
                    The content is completely unreadable to humans. It has to be like that, as the file is intended for 
                        Python's use only.
                    When Python imports a module for the first time, it translates its contents into a somewhat compiled 
                        shape.
                    The file doesn't contain machine code - it's internal Python semi-compiled code, ready to be executed 
                        by Python's interpreter.  
                    Python is able to check if the module's source file has been modified (in this case, the pyc file 
                        will be rebuilt) or not (when the pyc file may be run at once). As this process is fully automatic and transparent, 
                        you don't have to keep it in mind.  
    Step3:  Now let us modify the module.py file with some code. and run.
                print('I like to be a module.'). 
                After running, you should see 'I like to be a module.' , message in theterminal.
    Step4:  Now run the main.py file. and observe the output. Now in this run, you should see the below message:
                I like to be a module.
                What does it mean?
                -------------------
                    a.  When a module is imported, its content is implicitly executed by Python. It gives the module the 
                        chance to initialize some of its internal aspects.
                Note:   the initialization takes place only once, when the first import occurs, so the assignments done 
                        by the module aren't repeated unnecessarily.
              Python do much more. It also creates a variable called __name__.
                Note:   Moreover, each source file uses its own seperate version of the '__name__' variable. This 
                        variable isn't shared between modules.
    How to use the '__name__' variable:
    -----------------------------------
    step5:  Modify the 'module.py' a bit
            add print(__name__)
            Save and run the module.py file. The output would be:
                I like to be a module.
                __main__
            Now run the main.py file. The output would be:
                I like to be a module.
                module
            Observations:
            -------------
            We can say that:
                a.  When you run a file directly, it's '__name__' variable is set to __main__;
                b.  When a file is imported as a module, it's __name__ variable is set to the file's name (excluding .py)
    step6:  This is how you can make use of the __main__ variable in order to detect the context in which your code has 
            been activated:
            Open the module.py and include the below code:
                if __name__ == "__main__":
                    print('I prefer to be a module.')
                else:
                    print('I like to be a module.')
            and run. You should see the 'I prefer to be a module.' message.
    step7:  This module will contain two simple functions, and if you want to know how many times the functions have been 
            invoked, you need a counter initialized to zero when the module is being imported. Add the below code in the
            module.py file

                    counter = 0

                    if __name__ == "__main__":
                        print("I prefer to be a module.")
                    else:
                        print("I like to be a module.")
    step8:  Introducing such a variable is absolutely correct, but may cause important side effects that you must be aware
            of. Take a look at main.py file and add the 'print(module.counter)' statement

    step9:  Now add some brand new code and save it then run. You should see the result.
    step10: Now it is possible to use the updated module - this is one way. 
            Open the main.py module.
                from module import suml, prodl

                zeroes = [0 for i in range(5)]
                ones = [1 for i in range(5)]
                print(suml(zeroes))
                print(prodl(ones))

    step11: How Python searches for modules?
            so far we've assumed that the main Python file is located in the same folder/directory as the module to be 
            imported. Let's give up this assumption and conduct the following thought experiment:
    Ans:    There's a special variable (actually a list) storing all locations (folders/directories) that are searched 
            in order to find a module which has been requested by the import instruction.
            Python browses these folders in the order in which they are listed in the list - if the module cannot be 
            found in any of these directories, the import fails.
            Otherwise, the first folder containing a module with the desired name will be taken into consideration 
            (if any of the remaining folders contains a module of that name, it will be ignored).
            The variable is named path, and it's accessible through the module named sys

        """
"""
    Your first Package:
    -------------------
    1. First create a folder 'extra'.
    2. Now within the extra folder, create 'iota.py' module, and two subfolder namely, 'good', and 'ugly'
    3. With in the 'good' subfolder, create alpha.py module, beta.py module, and the best subfolder
    4. within the ugly sub folder, there are 'omega.py' and 'psi.py' modules

    Now the question is 
        a.  How do you transform  the above tree structure into a real Python package? (in other words, 
            how do you convince Python that such a tree is not just a bunch of junk files, but a set of modules)?
        b.  where do you put the subtree to make it accessible to Python? Answer is anywhere

        Note: packages, like modules, may require initialization.
        ----
            a.  The initialization of a module is done by an unbound code (not a part of any function) located 
                inside the module's file. As a package is not a file, this technique is useless for initializing 
                packages.
            b.  You need to use a different trick instead - Python expects that there is a file with a very unique 
                name inside the package's folder: __init__.py. 
                The content of the file is executed when any of the package's modules is imported. If you don't 
                want any special initializations, you can leave the file empty, but you mustn't omit it.
            c.  the presence of the __init.py__ file finally makes up the package.
            d.  it's not only the root folder that can contain __init.py__ file - you can put it inside any of its 
                subfolders (subpackages) too. It may be useful if some of the subpackages require individual treatment 
                and special kinds of initialization.
    
    """
"""
    modules and packages: key takeaways:
    --------------------------------------
    a.  While a module is designed to couple together some related entities (functions, variables, constants, etc.), 
        a package is a container which enables the coupling of several related modules under one common name. Such a 
        container can be distributed as-is (as a batch of files deployed in a directory sub-tree) or it can be packed 
        inside a zip file.
    b.  During the very first import of the actual module, Python translates its source code into the semi-compiled 
        format stored inside the pyc files, and deploys these files into the __pycache__ directory located in the 
        module's home directory.
    c.  If you want to instruct your module's user that a particular entity should be treated as private (i.e. not 
        to be explicitly used outside the module) you can mark its name with either the _ or __ prefix. Don't forget 
        that this is only a recommendation, not an order.
    d.  The names shabang, shebang, hasbang, poundbang, and hashpling describe the digraph written as #!, used to 
        instruct Unix-like OSs how the Python source file should be launched. This convention has no effect under 
        MS Windows.
    e. If you want convince Python that it should take into account a non-standard package's directory, its name 
        needs to be inserted/appended into/to the import directory list stored in the path variable contained in 
        the sys module.
    f. A Python file named __init__.py is implicitly run when a package containing it is subject to import, and is 
        used to initialize a package and/or its sub-packages (if any). The file may be empty, but must not be absent.



"""
