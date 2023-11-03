"""     Working with class and instance data - instance variables
        ---------------------------------------------------------
In Python, we can define varibles at two levels namely 
    a.  instance level - varaibles defined at instance level 
    b.  class level - variables defined at class level

Instance variables:
------------------
a.  Instance variables exists when and only when the instance (object) is explicitly created.
b.  Instance variables are added to objects during it's initialization. We know that object initialization is
    done by the __init__() special methods.
c.  Furthermore, any existing property can be removed at any time.
d.  Instance variables are accessed using the dot operator

"""

class Demo:
    def __init__(self, value):
        self.instance_var = value
    
d1 = Demo(10)
d2 = Demo(20)
print("d1's instance variable is equal to: ", d1.instance_var)
print("d2's instance variable is equal to: ", d2.instance_var)

""" a.  Instance variables can be created during any moment of an object's life. 
    b.  Moreover, it lists the contents of each object, using the built-in __dict__ property that is present 
        for every Python object.
"""

d1.another_var = "Another variable in the object."
print(d1.__dict__)
print(d2.__dict__)

"""     Class variables:
        ----------------
        a.  Class variables are defined within the class construction.
        b.  Class variables are available before any class instances are created.
        c.  To get access to a class variable, simply access it using the class name, and then provide the 
            variable name.
        d.  class variables are shown in class's __dict__ dictionary
        e.  class variables are used to store meta data relevant to the class, rather than instance:
                1.  fixed information like description, configuration, or identification values;
                2.  mutable information like the number of instances created (if we add a code to increment 
                    the value of a designated variable every time we create a class instance)
        f.  class variable is a class property that exists in one copy.
        g.  class variable is stored outside any class instance.
        h.  class variable is defined outside the object, it is not listed in object's __dict__.

    Note: 
    -----
    a.  When you want to read class variable value, you can use class or class instance to access it.
    b.  When you want to set or change the value of class variable, you should access it using class name, 
        but not class instance.
    c.  When you try to set a value for the class variable using the object (a variable referring to the 
        object or self keyword) but not the class, you are creating an instance variable that holds the same 
        name as the class variable. 
    d.  Class variables and instance variables are often utilized at the same time, but for different purposes.
        As mentioned before, class variables can refer to some meta information or common information shared 
        amongst instances of the same class.  
"""
print('------------------------------------------------------')
class Demo:
    class_var = "Shared variable."

d1 = Demo()
d2 = Demo()

# both instances allow access to the class variable
print(d1.class_var)
print(d2.class_var)
print('.' * 20)

# d1 object has no instance variable
print("contents of d1 are: ", d1.__dict__)
print('.' * 20)

# d1 object receives an instance variable named class_var
d1.class_var = "I'm messing with the class variable."

# d1 object owns the variable named 'class_var' which holds a different value than the class variable named in the same way
print("contents of d1 are: ", d1.__dict__)
print(d1.class_var)
print('.' * 20)

# illustration for point number d
class Duck:
    counter = 0         # class variable
    species = 'duck'    # again a class variable

    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex
        Duck.counter += 1

    def walk(self):
        pass

    def quack(self):
        print('quacks')

class Chicken:
    species = 'chicken'

    def walk(self):
        pass

    def cluck(self):
        print('clucks')

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")
chicken = Chicken()

print('So many ducks were born:', Duck.counter)

for poultry in [duckling, drake, hen, chicken]:
    print(poultry.species, end=' ')
    if poultry.species == 'duck':
        poultry.quack()
    elif poultry.species == 'chicken':
        poultry.cluck()

"""
     a class variable of a super class can be used to count the number of all objects created from the 
     descendant classes (subclasses

"""

class Phone:
    counter = 0

    def __init__(self, number):
        self.number = number
        Phone.counter += 1

    def call(self, number):
        message = 'Calling {} using own number {}'.format(number, self.number)
        return message


class FixedPhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        FixedPhone.last_SN += 1
        self.SN = 'FP-{}'.format(FixedPhone.last_SN)


class MobilePhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        MobilePhone.last_SN += 1
        self.SN = 'MP-{}'.format(MobilePhone.last_SN)


print('Total number of phone devices created:', Phone.counter)
print('Creating 2 devices')
fphone = FixedPhone('555-2368')
mphone = MobilePhone('01632-960004')

print('Total number of phone devices created:', Phone.counter)
print('Total number of mobile phones created:', MobilePhone.last_SN)

print(fphone.call('01632-960004'))
print('Fixed phone received "{}" serial number'.format(fphone.SN))
print('Mobile phone received "{}" serial number'.format(mphone.SN))