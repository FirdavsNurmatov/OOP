class Countries :
    def __init__(self,c_name,c_city,c_community,c_chegaros,c_prezident) :
        self.c_name = c_name
        self.c_city = c_city
        self.c_community = c_community
        self.c_chegaros = c_chegaros
        self.c_prezident = c_prezident
    def info(self) :
        print(f"{self.c_name},{self.c_city},{self.c_community},{self.c_chegaros},{self.c_prezident}")
   

lst = [Countries('Amerika','New-York',500000000,456,'Bayden'),
Countries('Kanada','New-York',10000000,356,'Trump'),
Countries('Braziliya','Rio-de-Janero',500000000,256,'Trump'),
Countries('Tojikiston','Bapesh',500000000,156,'Trump'),
Countries("O'zbekiston",'Toshkent',500000000,456,'Shavkat'),
Countries('Rossiya','Moskva',500000000,1096,'Putin'),
Countries('Moldova','Borusiya',340000000,256,'Trump'),
Countries('Ukraina','New-York',500000000,254,'Bilmiman'),
Countries('Polsha','Varshava',300000000,446,'Trump'),
Countries('Chexiya','Praga',40000000,126,'Trump')]
sorted(lst,key = lambda x:x+1)
for i in lst :
    i.info()