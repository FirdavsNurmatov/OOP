class Employee :
    def __init__(self,id,name,surname,salary) :
        self.id = id
        self.name = name
        self.surname = surname
        self.salary = salary
    def get_id(self) :
        return self.id
    def get_name(self) :
        return self.name
    def get_surname(self) :
        return self.surname
    def get_fullname(self) :
        text = ''
        text = self.name + ' ' + self.surname
        return text
    def get_salary(self) :
        return self.salary
    def set_salary(self,settt_salary) :
        self.salary = settt_salary
        print(self.salary)
    def get_annualsalary(self) :
        return self.salary*12
    def raise_salary(self,inc_percent) :
        self.salary = self.salary + (self.salary//100 * inc_percent)
        return self.salary
    def to_string(self) :
        text = ""
        text = 'id= ' + str(self.id) + ', fullname: ' + self.get_fullname() + ', salary= ' + str(self.salary)
        return text

Id = int(input("id= "))
name = input('name: ')
surname = input('surname: ')
salary = int(input("salary= "))
person = Employee(Id,name,surname,salary)
print("Employee is id: ",person.get_id())
print("Employee is name: ",person.get_name())
print("Employee is surname: ",person.get_surname())
print("Employee is fullname: ",person.get_fullname())
print("Employee is salary: ",person.get_salary())
n = input("Do you want set salary? Then click 1 or don't wanna click 0 = ")
if int(n) :
    settt_salary = int(input('set salary sum= '))
    print("Employee is set: ",end = '')
    person.set_salary(settt_salary)
else :
    pass
print("Employee is annual salary: ",person.get_annualsalary())
n = input("Do you want raise salary? Then click 1 or don't wanna click 0 = ")
if int(n) :
    inc_percent = int(input("how much percent dou you wanna= "))
    print("Employee is raised salary: ",person.raise_salary(inc_percent))
else :
    pass
print(person.to_string())