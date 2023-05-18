class BankAccount:
    def __init__ (self, int_rate, balance):
        self.interest_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self

    def display_account_info(self):
        print("Balance: $" + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
            return self

# Create 2 accounts

 Account 1 
account1=BankAccount(0.02,500)
account1.deposit(100).deposit(10).deposit(20).display_account_info()
account1.withdraw(10).display_account_info()
account1.yield_interest(10).display_account_info()


#Account 2 

account2=BankAccount(0.02,900)
account2.deposit(200).deposit(100).display_account_info()
account2.withdraw(500).withdraw(50).withdraw(20).withdraw(10).display_account_info()
account2.yield_interest(10).display_account_info()


