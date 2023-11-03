class time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __eq__(self, value):
        return self.hour * 3600 + self.minute * 60 + self.second == value.hour * 3600 + value.minute * 60 + value.second
    

    def __ge__(self, value):
        return self.hour * 3600 + self.minute * 60 + self.second >= value.hour * 3600 + value.minute * 60 + value.second
    
    def __gt__(self, value):
        return self.hour * 3600 + self.minute * 60 + self.second > value.hour * 3600 + value.minute * 60 + value.second 
    
    def __le__(self, value):
        return self.hour * 3600 + self.minute * 60 + self.second <= value.hour * 3600 + value.minute * 60 + value.second
    
    def __lt__(self, value):
        return self.hour * 3600 + self.minute * 60 + self.second < value.hour * 3600 + value.minute * 60 + value.second
    
    def __ne__(self, value):
        return self.hour * 3600 + self.minute * 60 + self.second != value.hour * 3600 + value.minute * 60 + value.second
    
    def isoformat(self):
        return f'{self.hour}:{self.minute}:{self.second}'
    


time_1  = time(10, 23, 24)
time_2  = time(11,12,9)
print(time_1 == time_2)
print(time_1 > time_2)
print(time_1 < time_2)
print(time_2 != time_1)
print(time_1.isoformat())