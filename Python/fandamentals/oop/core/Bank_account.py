class BankAccount:
    def __init__ (self, int_rate, balance):
        self.interest_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5

    def display_account_info(self):
        print("Balance: $" + str(self.balance))

    def yield_interest(self):
        if self.balance >= 0:
            self.balance += self.balance * self.interest_rate

# Create 2 accounts
account1 = BankAccount()
account2 = BankAccount()

# Account 1 transactions
account1.deposit()
account1.deposit()
account1.deposit()
account1.withdraw()
account1.yield_interest()
account1.display_account_info()  

# Account 2 transactions
account2.deposit()
account2.deposit()
account2.withdraw()
account2.withdraw()
account2.withdraw()
account2.withdraw()
account2.yield_interest()
account2.display_account_info()


#manque les fonctions