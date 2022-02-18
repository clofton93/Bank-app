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
        print(self.int_rate)
        print(self.balance)
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
        print(self.balance)