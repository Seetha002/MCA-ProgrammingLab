class bank:
    def __init__(self,acct_no,acct_name,acct_type,bal):
        self.acct_no=acct_no
        self.acct_name=acct_name
        self.acct_type=acct_type
        self.bal=bal
    def deposit(self,amt):
        self.bal=self.bal+amt
        print("The amount ",amt," is deposited")
        print("Current balance:",self.bal)
    def withdraw(self,amt):
        self.bal=self.bal-amt
        print("The amount ",amt," is withdrawn")
        print("Current balance:",self.bal)
account=bank(1234,"seetha","savings",1000)
account.deposit(500)
account.withdraw(200)
