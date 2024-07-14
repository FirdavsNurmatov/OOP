class Time :
    def __init__(self,hour,minute,second) :
        self.hour = hour
        self.minute = minute
        self.second = second
    def time(self) :
        return self.hour,self.minute,self.second
    def get_hour(self) :
        return self.hour
    def get_minute(self) :
        return self.minute
    def get_second(self) :
        return self.second
    def set_hour(self,c_hour) :
        i = 1
        while i :
            if 0 <= c_hour <= 23 :
                i = 0
            else :
                print('Try again!')
                c_hour = int(input('hour= '))
        self.hour = c_hour
        print(self.hour)
    def set_minute(self,c_minute) :
        i = 1
        while i :
            if 0 <= c_minute <= 59 :
                i = 0
            else :
                print('Try again!')
                c_minute = int(input('minute= '))
        self.minute = c_minute
        print(self.minute)
    def set_second(self,c_second) :
        i = 1
        while i :
            if 0 <= c_second <= 59 :
                i = 0
            else :
                print('Try again!')
                c_second = int(input('second= '))
        self.second = c_second
        print(self.second)
    def set_time(self,c_hour,c_minute,c_second) :
        i = 1
        while i :
            hour = int(input('hour= '))
            minute = int(input('minute= '))
            second = int(input('second='))
            if 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59 :
                i = 0
            else :
                print('Try again!')
        self.hour,self.minute,self.second = c_hour,c_minute,c_second
        print(c_hour,c_minute,c_second)
    def to_string(self) :
        print(f"{self.hour:02d} : {self.minute:02d} : {self.second:02d}")
    def next_second(self) :
        self.second = (self.second + 1) % 60
        if self.second == 0 :
            self.minute = (self.minute + 1) % 60
            if self.minute == 0 :
                self.hour = (self.hour + 1) % 24
        print(f"{self.hour:02d} : {self.minute:02d} : {self.second:02d}")
    def pervious_second(self) :
        self.second-=1
        if self.second == -1 :
            self.second = 59
            self.minute-=1
            if self.minute == -1 :
                self.minute = 59
                self.hour-=1
                if self.hour == -1 :
                    self.hour = 0
        print(f"{self.hour:02d} : {self.minute:02d} : {self.second:02d}")

i = 1
while i :
    hour = int(input('hour= '))
    minute = int(input('minute= '))
    second = int(input('second='))
    if 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59 :
        i = 0
    else :
        print('Try again!')

t = Time(hour,minute,second)
t.pervious_second()
print("hour =",t.get_hour())
print("minujte =",t.get_minute())
print("second =",t.get_second())
set_hourby = 23
t.set_hour(set_hourby)
t.to_string()
set_minuteby = 59
t.set_minute(set_minuteby)
t.to_string()
set_secondby = 59
t.set_second(set_secondby)
t.to_string()
t.set_time(set_hourby,set_minuteby,set_secondby)
t.to_string()
t.next_second()