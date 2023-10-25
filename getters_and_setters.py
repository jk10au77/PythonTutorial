class Student:
    def __init__(self, fName, lName):
        self.firstName = fName
        self.lastName = lName
        self.fullName = f"{fName.upper()} {lName.upper()}"

jaya = Student('Jaya Kumar', 'Tatipathi')
print('-----------printing ordinary way -----------------')
print(jaya.firstName)
print(jaya.lastName)
print(jaya.fullName)

jaya.fullName = "Tatipathi Jaya Kumar"
print(jaya.fullName)

class Student:
    def __init__(self, fName, lName):
        self.set_firstName(fName)
        self.set_lastName(lName)
        self.set_fullName(fName, lName)

    def set_firstName(self, fName):
        self.set_firstName = fName
    
    def get_firstName(self):
        return self._firstName
        
    def set_lastName(self, lName):
        self._lastName = lName
    
    def get_lastName(self):
        return self._lastName
    
    def set_fullName(self, fName, lName):
        self._fullName = f"{fName} {lName}"
    
jaya = Student('Jaya Kumar', 'Tatipathi')
print('--------------printing using setters and getters ----------------------')
print(jaya._lastName)
print(jaya._fullName)


"""
    Using properties instead of getters and setters:
    ------------------------------------------------
    a.  Properties pack together methods for getting, setting, deleting, and documenting the underlying data.
    b.  You can use properties in the same way that you use regular attributes.
    c.  When you access a property, its attached getter method is automatically called.
    d.  When you mutate the property, its setter method gets called.
    e.  Property provides the means to attach functionality to your attributes without introducing breaking 
        changes in your code's API.
"""

class Employee:
    def __init__(self, name, date_of_birth) -> None:
        self.name = name
        self.birth_date = date_of_birth
    
print('----------- property illustrations --------------------')
john = Employee('John', "2001-02-07")
print(john.name)
print(john.birth_date)

john.name = "John Doe"
print(john.name)

"""
    Now your project evolves and your new requirement is as below:
    a.  You need to store employee name in upper case
    b.  turn the date of birth to date object

    Note:   To meet these requirement without breaking your API with getter and setter method for .name
            and .birth_date, youcan use properties.

"""
from datetime import date
class Employee:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.birth_date = date_of_birth

    @property
    def name(self):
        return self._name
    
    @property.setter
    def name(self, name):
        self._name = name.upper()
    
    @property
    def birth_date(self):
        return self._birth_date
    
    @property.setter
    def birth_date(self, date_of_birth):
        self._birth_date = date(date_of_birth)

"""
    In the above enhanced version of Employee class, 

        a.  we have turned .name and .birth_date into preoperties using the @property decorator.
        b.  Now each attribute has a getter and setter method named after the attribute itself.
        c.  Note that the setter of .name turns the input name into uppercase letters. 
        d.  Similarly, the setter of .birth_date automatically converts the input date into a date 
            object for you.
        e.  You must avoid breaking your user's code by introducing changes in your APIs. Python's @property 
            decorator is the Pythonic way to do that. 
        f.  Properties are officially recommended in PEP 8 as the right way to deal with attributes that need 
            functional behavior:
"""

"""
    Python's properties have a lot of potential use cases: For example, 
    
    a.  you can use properties to create read-only, read-write, and write only attributes in an elegant 
        and straightforward manner.
    b.  Propeties allow you to delete and document the underlying attributes.
    c.  properties allow you to make regular attributes behave like managed attributes with attached behavior 
        without changing the way you work with them.
    

"""
