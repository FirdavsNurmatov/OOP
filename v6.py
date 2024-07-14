class Account :
    def __init__(self,id,name,balance) :
        self.id = id
        self.name = name
        self.balance = balance
    def get_id(self) :
        return self.id
    def get_name(self) :
        return self.name
    def get_balance(self,credit=0,debit=0) :
        self.balance+=credit
        self.balance-=debit
        return self.balance

# 1-user
Id = 'Jama12'
name = 'Jamshid'
balance = 700
# You
Id2 = 'Aka1202'
name2 = 'Akmal'
balance2 = 200
user = Account(Id,name,balance)
user2= Account(Id2,name2,balance2)
print(f"""1-user
    id: {user.get_id()}
    name: {user.get_name()}
    balance: {user.get_balance()}
2-user
    id: {user2.get_id()}
    name: {user2.get_name()}
    balance: {user2.get_balance()}
""")
i = 1
while i :
    print("""Menu:
    1.Credit
    2.Debit
    3.Transfer to
    4.Tostring
    5.Exit
""")
    credit,debit = 0,0
    select = int(input('select number>>>>'))
    if select == 1 :
        credit = int(input('credit= '))
        print(f"""
    1-user is balance: {user.get_balance(credit,debit)}
    """)
    elif select == 2 :
        debit = int(input('debit= '))
        if debit <= balance :
            print(f"""
    1-user is balance: {user.get_balance(credit,debit)}
    """)
        else :
            print("""
    Amount exceeded balance
    """)
    elif select == 3:
        print("""
        Which user you choose to transfer? 1 or 2?""")
        n = int(input("""        Transfer to user: """))
        if n == 1 :
            transferto = int(input("""        Transfer to sum= """))
            if transferto <= user.balance :
                user.get_balance(credit,transferto)
                user2.get_balance(transferto,debit)
                print(f"""   
        Your transfer succesfully end!
        Your balance: {user.balance}
        2-user is balance: {user2.balance}""")
            else :
                print("""
        Amount exceeded balance
        """)
        elif n == 2 :
            transferto = int(input("Transfer to sum= "))
            if transferto <= user2.balance :
                user2.get_balance(credit,transferto)
                user.get_balance(transferto,debit)
                print(f"""   
        Your transfer succesfully end!
        Your balance: {user2.balance}
        1-user is balance: {user.balance}""")
            else :
                print("""
        Amount exceeded balance
        """)
        else :
            print("""
        There is no user
        """)
    elif select == 4:
        print(f"""
    1-user
        id: {user.get_id()}
        name: {user.get_name()}
        balance: {user.get_balance()}
    2-user
        id: {user2.get_id()}
        name: {user2.get_name()}
        balance: {user2.get_balance()}
    """)
    elif select == 5 :
        print("""
    Thank you for choosing us!
    """)
        i = 0
    else :
        print("""
    Try again
    """)