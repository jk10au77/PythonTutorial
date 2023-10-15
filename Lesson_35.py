class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

sun = Star("Sun", "Milky Way")
print(sun) 

"""
    The __str__() method:
    ---------------------
    a.  return string representation of an object.
"""

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy
    
sun = Star("Sun", "Milky Way")
print("-------------------------------------------------------------------------------")
print(sun)

"""
    Inheritance is a common practice of passing attributes and methods from super class to it's subclass.
    In other words, Inheritance is a way of building a new class, not from scratch, but by using an already 
    defined repertoire of traits.
    The new subclass inheritance all the already existing attributes and methods in the super class, but is 
    able to add new attributes and methods.

"""

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackVehicle(LandVehicle):
    pass

"""
    issubclass(class_1, class_2) function: 
    --------------------------------------
        a.  identifies whether class_1 is a sub class of class_2
        b.  return True if class_1 is a subclass to class_2. Otherwise returns False
        Note:   Each class is considered as a subclass to itself.
"""
print("-------------------------------------------------------------------------------")
print("Printing the relationship between Vehicle, LandVehicle, TrackVehicle classes")
print("-------------------------------------------------------------------------------")

for cls1 in [Vehicle, LandVehicle, TrackVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackVehicle]:
        print(issubclass(cls1, cls2), end = '\t')
    print()
print("-------------------------------------------------------------------------------")

"""
    isinstance(objectName, ClassName) function:
    -------------------------------------------
        a.  return True if objectName is an object of ClassName class. Otherwise returns False
"""

my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_track_vehicle = TrackVehicle()
print("Printing whether the object is an instance of which class")
print("-------------------------------------------------------------------------------")
for obj in [my_vehicle, my_land_vehicle, my_track_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackVehicle]:
        print(isinstance(obj, cls), end='\t')
    print()
print("-------------------------------------------------------------------------------")

"""
    The is operator:    object_1 is object_2
    ------------------
        a.  checks whether object_1 and object_2 refer to the same object.
        b.  returns True if object_1 and object_2 refer to the same object.
            otherwise, resturn False.
        Note:   
        -----   
            a.  variables don't store the objects themselves, but only the handles pointing to the internal 
                Python memory.
"""

class SimpleClass:
    def __init__(self, val):
        self.val = val

object_1 = SimpleClass(0)
object_2 = SimpleClass(2)
object_3 = object_1
object_3.val += 1
print("--------------------------The 'is' operator illustration----------------------")
print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)



