class BankAccount():
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.amount =  amount
        self.balance = self.balance + amount 
        print("Account balance updated:", self.balance)
        
    def withdraw(self, amount):
        if self.balance >= self.amount:
            self.balance = self.balance - amount
            print("Account Balance Updated :", self.balance)
        
        elif self.balance < self.amount:
            self.balance =  self.balance - 5
            print("Insufficient Funds Charging a $5 fee:", self.balance)
            
    def display_account_info(self):
        print("Account Information:", self.int_rate, self.balance)
        return self
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        print("Account Balance Updated:", self.balance)
        return self
        
account1  = BankAccount(0.04,35)
account2 = BankAccount(0.05,25)
account3 = BankAccount(0.04,100)

account1.deposit(20)
account1.deposit(50)
account1.deposit(500)
account1.withdraw(400)
account1.yield_interest().display_account_info()

account2.deposit(400)
account2.deposit(100)
account2.withdraw(25)
account2.withdraw(22.5)
account2.withdraw(57)
account2.withdraw(45)
account2.yield_interest().display_account_info()