class date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    

class time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


class datetime(date, time):
    def __init__(self, year, month, day, hour, minute, second):
        super().__init__(year, month, day)
        super().__init__(hour, minute, second)

my_date = date(2023, 10, 24)
my_time = time(10, 23, 56)
my_datetime = datetime(2022, 9, 23, 9, 22, 55)

for att in my_datetime.__dict__:
    print(my_datetime.__doc__[att])
    
