class Date :
    def __init__(self,day,month,year) :
        self.day = day
        self.month = month
        self.year = year
    def get_date(self) :
        return self.day,self.month,self.year
    def get_day(self) :
        return self.day
    def get_month(self) :
        return self.month
    def get_year(self) :
        return self.year
    def set_day(self,c_day) :
        i = 1
        while i :
            if 1 <= c_day <= 31 :
                i = 0
            else :
                print('Try again!')
                c_day = int(input('day= '))
        self.day = c_day
        print(self.day)
    def set_month(self,c_month) :
        i = 1
        while i :
            if 1 <= c_month <= 12 :
                i = 0
            else :
                print('Try again!')
                c_month = int(input('month= '))
        self.month = c_month
        print(self.month)
    def set_year(self,c_year) :
        i = 1
        while i :
            if 1900 <= c_year <= 9999 :
                i = 0
            else :
                print('Try again!')
                c_year = int(input('year= '))
        self.year = c_year
        print(self.year)
    def set_date(self,c_day,c_month,c_year) :
        i = 1
        while i :
            if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 9999 :
                i = 0
            else :
                print('Try again!')
                c_day = int(input('day= '))
                c_month = int(input('month= '))
                c_year = int(input('year='))        
        self.day,self.month,self.year = c_day,c_month,c_year
        print(self.day,self.month,self.year)
    def to_string(self) :
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

i = 1
while i :
    day = int(input('day= '))
    month = int(input('month= '))
    year = int(input('year='))
    if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 9999 :
        i = 0
    else :
        print('Try again!')

time = Date(day,month,year)
print("day =",time.get_day())
print("month =",time.get_month())
print("year =",time.get_year())
set_day = int(input('set day= '))
time.set_day(set_day)
time.to_string()
set_month = int(input('set month= '))
time.set_month(set_month)
time.to_string()
set_year = int(input('set year= '))
time.set_year(set_year)
time.to_string()
time.set_date(set_day,set_month,set_year)
time.to_string()