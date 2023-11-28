"""
1.  What is an Abstract class?
Ans.    An Abstract class should be considered as a blueprint for other classes. . It is a kind ofcontract between class designer and 
    a programmer.

    a.  the class designer sets requirements regarding methods that must be implemented bu just declaring them. but not defining them in detail.
        Such methods are called abstract methods.
    b.  The programmer has to deliver all method definitions and the completeness would be validated by another, dedicated module. The 
        programmer delivers the method definitions by overriding the method declarations received from the class designer.
    c.  This contract assures you that a child class, built upon your abstract class, will be equipped with a set of concrete methods imposed by
        the abstract class.

2.  Why do we want to use abstract classes?
Ans.    Because we want our code to be polymorphic. o all subclasses have to deliver a set of their own method implementations in order to call 
        them by using common method names.
        Furthermore, a class which contains one or more abstract methods is called an abstract class. This means that abstract classes are not 
        limited to containing only abstract methods - some of the methods can already be defined, but if any of the methods is an abstract one, 
        then the class becomes abstract.

        

3.  What is an abstract method?
Ans. An abstract method is a method that has a declaration, but does not have any implementation. 

Note:  
----
a.  It is not possible to instantiate an Abstract class.
b.  It needs subclasses to provide implementations for those abstract methods which are declared in the abstract classes. This behaviour is a 
    test performed by a dedicated Python module to validate if developer has implemented a subclass that overrides all abstract methods.
c.  When we are designing large functional units, in the form of classes, we should use an abstract class.
d.  When we want to provide common implemented functionality for all implementations of the class, we could also use an abstract class, because 
    abstract classes partially allow us to implement classes by delivering concrete definitions for some of the methods, not only declarations.
e.  Abstract classes just provide the means by which to provide a common Application Program Interface (API) for a set of subclasses. This 
    capability is especially useful in situations where your team or third-party is going to provide implementations, such as with plugins in 
    an application, even after the main application development is finished.


"""

# Let's start with a typical class that can be instantiated.

class BluePrint:
    def hello(self):
        print('Nothing is Blue unless you need it!')
print('--------------------------------------------')
bp = BluePrint()
bp.hello()
print('--------------------------------------------')
# There’s nothing new for you here – it’s just an example of creating a class and instantiating it. 
# No errors, no doubts, and it gives a clear output:
# Output: Nothing is Blue unless you need it

"""
    Abstract Base Classes:
    ----------------------
    a.  Python has come up with a module which provides the helper class for defining Abstract Base Classes (ABC) and that module is abc.
    b.  The ABC allows you to mark classes as Abstract ones and distinguish which methods of the base abstract are Abstract.
    c.  A method becomes abstract by being decorated with an '@abstractmethod' decorator.

    To start with ABC, you should:

        a. import abc module
        b. make your base class inherit the helper class ABC, which is delivered by the abc module.
        c. decorate abstract methods with @abstractmethod decorator, which is delivered by the abc module.
            
"""

# creating abstract classes

import abc

class BluePrint(abc.ABC):

    @abc.abstractmethod
    def hello(self):
        pass

class GreenField(BluePrint):
    def hello(self):
        print('Welcome to Green Field!')

gf = GreenField()
gf.hello()
print('--------------------------------------------')

# Now let us try to instantiate the BluePrint class

#bp = BluePrint()        # you should get TyeError. So, we can't instantiate an Abstract class 

"""
Important Note on Abstarct classes:
------------------------------------
1.  Python raises a TypeError exception when we try to instantiate the Abstract Base class, because it contains an abstract method.
2.  If an Abstract Base Class contains more than one abstract methods, then all of them must be overriden in a subclass before subclass can be instantiated.

"""

# Now we will try to inherit the abstract class and forget about overriding the abstract method by creating RedField class.
# The RedField class does not override the hello method. See what happens

class RedField(BluePrint):
    def yellow(self):
        pass

#rf = RedField()     #you will get TypeError: Can't instantiate abstract class RedField with abstract methods hello

"""
indicates that:
    a.  it's possible to instantiate the GreenField class and call the hello method;
    b.  the RedField class is still recognized as an abstract one, because it inherits all elements of its super class, which is abstract, 
        and the RedField class does not override the abstract hello method.

Multiple inheritance:
    When you plan to implement a multiple inheritance from abstract classes, remember that an effective subclass should override all abstract 
    methods inherited from its super classes.

"""

"""
Summary:
--------
a.  Abstract Base Class (ABC) is a class that cannot be instantiated. Such a class is a base class for concrete classes;
b.  ABC can only be inherited from;
c.  we are forced to override all abstract methods by delivering concrete method implementations.

"""

"""
    LAB:
    ----

Objectives:
------------
a.  Creation of abstract classes and abstract methods;
b.  multiple inheritance of abstract classes;
c.  overriding abstract methods;
d.  delivering multiple child classes.

-----------------------------------------------------------

Scenario:
---------

    a.  You are about to create a multifunction device (MFD) that can scan and print documents;
    b.  the system consists of a scanner and a printer;
    c.  your task is to create blueprints for it and deliver the implementations;
    d.  create an abstract class representing a scanner that enforces the following methods:
        1.  scan_document - returns a string indicating that the document has been scanned;
        2.  get_scanner_status - returns information about the scanner (max. resolution, serial number)
    e.  Create an abstract class representing a printer that enforces the following methods:
        1.  print_document - returns a string indicating that the document has been printed;
        2.  get_printer_status - returns information about the printer (max. resolution, serial number)
    f.  Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible for scanning and printing:
        1.  MFD1 - should be a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) should be low;
        2.  MFD2 - should be a medium-priced device allowing additional operations like printing operation history, and the resolution is 
            better than the lower-priced device;
        3.  MFD3 - should be a premium device allowing additional operations like printing operation history and fax machine.
    g. Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices should be capable of serving generic feature sets.

"""

class Scanner(abc.ABC):

    @abc.abstractmethod
    def scan_document(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass

class Printer(abc.ABC):

    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass

class MFD_1(Scanner):

    def __init__(self, resolution = 20, number = 2000):
        self.max_resolution = resolution
        self.serial_number = number
    
    def scan_document(self):
        return f'The document has been scanned.'

    def get_scanner_status(self):
        return f"The Scanner's serial number is {self.serial_number} with {self.max_resolution} maximum resolution. "

class MFD_2(Printer):

    def __init__(self, resolution = 10, number = 1000):
        self.max_resolution = resolution
        self.serial_number = number

    def print_document(self):
        return 'The document has been printed.'

    def get_printer_status(self):
        return f"The Printer's serial number is {self.serial_number} with maximum resolution {self.max_resolution}."

class MFD_3(Scanner, Printer):
    pass


mfd_1 = MFD_1()
mfd_2 = MFD_2()

for task in mfd_1.scan_document(), mfd_1.get_scanner_status():
    print(task)


