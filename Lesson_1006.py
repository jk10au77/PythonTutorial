"""       Inheritance and polymorphism — Inheritance is a pillar of OOP
        -----------------------------------------------------------------
a.  Inheritance is one of the fundamental concepts of Object Oriented Programming.
b.  It expresses the fundamental relationship between classes: super classes (parents) and their subclasses (descendants)
c.  Inheritance creates a class hierarchy.
d.  Any object bound to a specific level of class hierarchy inherits all the traits (methods and attributes) defined inside any of the 
    superclasses.
e.  This means that inheritance is a way of building a new class, not from scratch, but by using an already defined repertoire of traits. 
    The new class inherits (and this is the key) all the already existing equipment, but is able to add some new features if needed.
f.  Each subclass is more specialized (or more specific) than its superclass. Conversely, each superclass is more general (more abstract) 
    than any of its subclasses.

"""

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

"""
    All the presented classes are empty for now. We can say that:
        a.  the Vehicle class is the superclass for both the LandVehicle and TrackedVehicle classes;
        b.  the LandVehicle class is a subclass of Vehicle and a superclass of TrackedVehicle at the same time;
        c.  the TrackedVehicle class is a subclass of both the Vehicle and LandVehicle classes.
"""

"""
    Inheritance and polymorphism — Single inheritance vs. multiple inheritance
    ---------------------------------------------------------------------------
    a.  Multiple inheritance: deriving any new class from more than one previously defined class is called multiple inheritance.
    b.  But multiple inheritance should be used with more prudence than single inheritance because:
            1.  a single inheritance class is always simpler, safer, and easier to understand and maintain;
            2.  multiple inheritance may make method overriding somewhat tricky; moreover, using the super() function can lead to ambiguity;
            3.  it is highly probable that by implementing multiple inheritance you are violating the single responsibility principle;

"""
""" 
    MRO - Method Resolution Order
    -----------------------------
"""

class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(B,C):
    pass

print('-' * 20)
D().info()      
print('.' * 20)

class A:
    def info(self):
        print('Class A')

class B(A):
    pass

class C(A):
    def info(self):
        print('Class C')

class D(B,C):
    pass

D().info()      
print('.' * 20)

class A:
    def info(self):
        print('Class A')
    
class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

D().info()      
print('.' * 20)

class A:
    def info(self):
        print('Class A')
    
class B(A):
    pass

class C(A):
    pass

class D(B,C):
    def info(self):
        print('Class D')

D().info()      
B().info()
C().info()
A().info()
print('.' * 20)

"""
    Exercise:
    ---------
        Scenario
        --------
        a.  Your task is to build a multifunction device (MFD) class consisting of methods responsible for document scanning, printing, and 
            sending via fax.
        b.  The methods are delivered by the following classes:
                1.  scan(), delivered by the Scanner class;
                2.  print(), delivered by the Printer class;
                3.  send() and print(), delivered by the Fax class.
            Each method should print a message indicating its purpose and origin, like:
                1.  'print() method from Printer class'
                2.  'send() method from Fax class'
                3.  create an MFD_SPF class ('SPF' means 'Scanner', 'Printer', 'Fax'), then instantiate it;
                4.  create an MFD_SFP class ('SFP' means 'Scanner', 'Fax', 'Printer'), then instantiate it;
                5.  on each object call the methods: scan(), print(), send();
                6.  observe the output differences. Was the Printer class utilized each time?
"""

class Scanner:
    def scan(self):
        print('scanning document.')

class Printer:
    def myprint(self):
        print('printing document')

class  Fax:
    def send(self):
        print('sending document.')

class MFD_SPF(Scanner, Printer, Fax):
    pass

class MFD_SFP(Scanner,Fax, Printer):
    pass

"""
        Inheritance and polymorphism — duck typing
        ------------------------------------------
    
    a.  Duck typing is a name for the term describing an application of the duck test: If it walks like a 
        duck and it quacks like a duck, then it must be a duck
    b.  Duck typing determines whether an object can be used for a particular purpose. 
    c.  An object's suitability is determined by the presence of certain attributes, rather than by the type 
        of the object itself.
    d.  Duck typing is another way of achieving polymorphism, and represents a more general approach than 
        polymorphism achieved by inheritance.
    e.  In duck typing, we believe that objects own the methods that are called. If they do not own them, then 
        we should be prepared to handle exceptions.
    f.  Let's talk about two things that share conceptually similar methods, but represent totally different 
        things, like cheese and wax. Both can melt, and we use the melted forms for different purposes.

"""
class Wax:
    def melt(self):
        print("Wax can be used to form a tool.")

class Cheese:
    def melt(self):
        print("Cheese can be eaten.")

class Wood:
    def fire(self):
        print("A fire has been started.")

for element in Wax(), Cheese(), Wood():
    try:
        element.melt()
    except AttributeError:
        print("No melt() method")
        
"""
    Both the Wax and Cheese classes own melt() methods, but there is no relation between the two. Thanks to 
    duck typing, we can call the melt() method. Unfortunatelly, the Wood class is not equipped with this 
    method, so an AttributeError exception occurs
"""

"""
    Summary:
    --------
    a.  polymorphism is used when different class objects share conceptually similar methods (but are not 
        always inherited)
    b.  polymorphism leverages clarity and expressiveness of the application design and development;
    c.  When polymorphism is assumed, it is wise to handle exceptions that could pop up.
"""
