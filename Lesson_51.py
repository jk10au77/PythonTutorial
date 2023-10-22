"""
                the datetime module:
                --------------------
    a.  Some of the applications of datetime module are given below:
        1.  event logging
        2.  tracking changes in databases
        3.  data validation
        4.  storing important information.
    b.  The datetime module provides classes for working with date and time.
    c.  date and time have countless uses. It's probably hard to find any production application that doesnot
        use them.
    d.  The following code snippet provides the all the entities of datetime module.
    e.  The commonly used classes in datetime module are:
        1.  time class
        2.  date class
        3.  datetime class
        4.  timedelta class
        Note: Objects of these classes are immutable.
    
    f.  The entities of datetime module include:
        1.  Constants:
        ---------------
            a.  datetime.MINYEAR    -   The smallest year number allowed in a date or datetime object. MINYEAR is 1.
            b.  datetime.MAXYEAR    -   The largest year number allowed in a date or datetime object. MAXYEAR is 9999.
            c.  datetime.UTC        -   Alias for the UTC timezone singleton datetime.timezone.utc.
        
        2.  Available classes or types:
        --------------------------------
            a.  class   datetime.date
            b.  class   datetime.time
            c.  class   datetime.datetime
            d.  class   datetime.timedelta
            e.  class   datetime.tzinfo
            f.  class   datetime.timezone

    g.  Common features of date, time, datetime, and timezone types :
        ------------------------------------------------------------
        a.  objects of these types are immutable
        b.  Objects of these types are hashable, meaning that they can be used as dictionary keys
        c.  Objects of these types support efficient pickling via the pickle module.
    
    h.  Determining if an object is Aware or Naive
        ------------------------------------------
        a.  Objects of date type are always Naive.
        b.  Objects of time and datetime type may be Naive or Aware.
        c.  An Object 'd' of datetime type is Aware if both of the following hold:
            1.  d.tzinfo is not None
            2.  d.tzinfo.utcoffset(d) does not return None
            Otherwise, d is Naive
        
        d.  A time Object 't' is aware if both of the following hold:
            1.  t.tzinfo is not None
            2.  t.tzinfo.utcoffset(t) doesnot return None
            Otherwise, t is Naive
        
Note:   The distinction between aware and naive doesn’t apply to timedelta objects.



import datetime                 # importing datetime module

for entity in dir(datetime):
    print(entity)               # prints all the entities in the datetime modules
"""
"""
    The datetime.time class:
    ------------------------
    a.  A 'datetime.time' object represents time of day.
    
        class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold =0)
        ---------------------------------------------------------------------------
            a.  all arguments are optional
            b.  tzinfo may be None or instance of 'txinfo' subclass
            c.  The remaining arguments must be integers if the following ranges:
                1.  0 <= hour < 24
                2.  0 <= minute < 60
                3.  0 <= second < 60
                4.  0 <= microsecond < 1000000
                5.  fold in [0,1]
            Note:  If an argument outside those ranges is given, ValueError is raised. All default to 0 except tzinfo, which defaults to None.
        
        class attributes:
        ----------------
        a. 

"""

from datetime import time

print('----------------------------------------------------------------')
print('printing entities in datetime.time class')
print('----------------------------------------------------------------')
for entity in dir(time):
    print(entity)
print('----------------------------------------------------------------')
print('end of printing entities in datetime.time class')
print('----------------------------------------------------------------')

a = time()              # time object with default values
print("a= ", a)

b = time(11, 34, 56)    # time object with hour = 11, minute = 34, and second = 56
print("b = ", b)

c = time(11, 34, 56, 234566)    # time object with hour = 11, minute = 34, second = 56, and microsecond = 234566
print("c: ", c)





























"""
    The datetime.timedelta class:
    -----------------------------
    a.  A timedelta Objects represents a duration, the difference between two dates or times

    class datetime.timedelta(days = 0, seconds = 0, microseconds = 0, milliseconds = 0, 
                             minutes = 0, seconds = 0, hours = 0, weeks = 0)
        
        1.  All arguments are optional and default to 0. 
        2.  Arguments may be integers or floats, and may be positive or negative
    Resource: https://docs.python.org/3/library/datetime.html

"""

from datetime import timedelta
time_delta = timedelta(days = 50,
                       seconds = 27,
                       microseconds=10,
                       milliseconds=29000,
                       minutes=5,
                       hours=8,
                       weeks=2)

































month_dict = {   '1': 'January', 
                 '2': 'February',
                 '3': 'March',
                 '4': 'April',
                 '5': 'May',
                 '6': 'June',
                 '7': 'July',
                 '8': 'August',
                 '9': 'September',
                '10': 'October',
                 '11': 'November',
                '12': 'December'}
day_dict =  {'1':   'Sunday',
             '2':   'Monday',
             '3':   'Tuesday',
             '4':   'Wednesday',
             '5':   'Thrusday',
             '6':   'Friday',
             '7':   'Saturday'}


