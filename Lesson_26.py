"""
    The basic concepts of the object-oriented approach: Object programming is the art of defining and expanding classes. 

    class:  A class is a model of a very specific part of reality, reflecting properties and activities found in the real 
            world.
    ---------------------------------------------------
    1.  Python is a universal tool for both object and procedural programming. It may be successfully utilized in both 
        spheres.    
    
    Procedural vs. the object-oriented approach
    -------------------------------------------
    In the procedural approach, it's possible to distinguish two different and completely separate worlds: 
        a.  the world of data, and 
        b.  the world of code. 
        The world of data is populated with variables of different kinds, while the world of code is inhabited by 
        code grouped into modules and functions.
        Functions are able to use data, but not vice versa. Furthermore, functions are able to abuse data, i.e., to 
        use the value in an unauthorized manner (e.g., when the sine function gets a bank account balance as a parameter).
    
    In object approach, The data and the code are enclosed together in the same world, divided into classes.
        a.  Every class is like a recipe which can be used to create a useful object. You may produce as many 
            objects as you need to solve your problem.
        b.  Every object has a set of traits (they are called properties or attributes - we'll use both words synonymously) 
            and is able to perform a set of activities (which are called methods).
        c.  The recipes (classes) may be modified if they are inadequate for specific purposes and, in effect, 
            new classes may be created. These new classes inherit properties and methods from the originals, 
            and usually add some new ones, creating new, more specific tools.

    Objects: 
    --------
        a.  Objects are incarnations of ideas expressed in classes.
        b.  Objects interact with eachother, exchanging data or activating their methods.
        c.  A properly constructed class (and thus, its objects) are able to protect the sensible data and hide it from 
            unauthorized modifications.  
    Note:   There is no clear border between data and code: they live as one in objects.

    """
"""
    Class hierarchies:
    ------------------
    a.  Hierachy grows from top to bottom
    b.  The top most class is called Super class, while its descendants located below are called subclasses.
    c.  The top level class (super class) does not have parents.
    
    Examples of classes:
    ---------------------
        a.  vehicles
                i.  Land Vehicles
                    a.  Wheeled Vehicles
                    b.  Tracked Vehicles
                    c.  Hovercrafts
                ii. Water Vehicles
                iii.Air vehicles
                iv. Space Vehicles    

        b.  animals
            i.  mammals
                a.  Wild mammals
                b.  Domestic mammals
            ii. reptiles
            iii.birds
            iv. fish
            v.  amphibians

"""
"""
    Object: 
    -------
        a.  An object is an incarnation of the requirements, traits, and qualities assigned to a specific class.
        b.  An object belonging to a specific class belongs to all the superclasses at the same time. It may also 
            mean that any object belonging to a superclass may not belong to any of its subclasses.
        C.  Each subclass is more specialized (or more specific) than its superclass. Each subclass is more specialized 
            (or more specific) than its superclass.
"""

"""
    Inheritance:
    ------------
    Any object bound to a specific level of a class hierarchy inherits all the traits (as well as the requirements 
    and qualities) defined inside any of the superclasses.
"""
"""
    What does an object have?
    -------------------------
    Every object may have three group of attributes:
        a.  Every object has a name that uniquely identifies within its homespace.
        b.  Every object has a set of properties which make it original, unique, or outstanding (although it's possible 
            that some objects may have no properties at all)
        c.  an object has a set of abilities to perform specific activities, able to change the object itself, or 
            some of the other objects.
        Note:
        ----
            a.  noun        - you probably define the object's name;
            b.  adjective   - you probably define the object's property;
            c.  verb        - you probably define the object's activity.
"""