class Person :

    def __init__ (self,name,surname,birthday) :
        self.name = name
        self.surname = surname
        self.birthday = birthday

    def get_age(self) :
        return 2024-self.birthday
    
    def getName(self) :
        return self.name.capitalize(),self.surname.capitalize()

user = Person('firdavs','Nurmatov',2008)
print(user.get_age())
print(user.getName())