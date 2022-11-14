# creating a bank account class
class Account:

    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath,'r') as file:
            self.balance=int(file.read())
    
    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount  

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))  

# creating classes trough inheritance
class Checking(Account):
    """This class generates account objects"""

    type="checking"

    def __init__(self, filepath, fee):
        Account.__init__(self,filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance- amount- self.fee

# Checking class calling
# jacks checking account
jacks_checking=Checking("bank_account/jack.txt",1)
jacks_checking.transfer(100)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)

# johns checking account
johns_checking=Checking("bank_account/john.txt",1)
johns_checking.transfer(100)
print(johns_checking.balance)
johns_checking.commit()
print(johns_checking.type)

print(johns_checking.__doc__)

#Account class calling
# account=Account("bank_account/balance.txt")
# print(account.balance)
# account.deposit(200)
# print(account.balance)
# account.commit()