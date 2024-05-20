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
    


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
        return self


user_1 = User("Sarra", "mail@gmail.com")
user_1.make_deposit(500).make_deposit(600).display_user_balance()

user_2 = User("Nour", "nour@gmail.com")
user_2.make_deposit(1000).display_user_balance().make_withdrawal(300).display_user_balance()
