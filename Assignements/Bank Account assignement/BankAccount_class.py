class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
            
    def display_account_info(self):
        print(f"Balance : {self.balance}§")
        return self
        
    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.balance * self.int_rate
        return self
    @classmethod
    def display_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()
    
account_1 = BankAccount(0.02, 500)
account_2 = BankAccount(0.05,2000)

account_1.deposit(20).deposit(25).deposit(50).withdraw(500).yield_interest().display_account_info()
account_2.deposit(100).deposit(300).withdraw(50).withdraw(20).withdraw(10).withdraw(30).yield_interest().display_account_info()

BankAccount.display_all_accounts()       