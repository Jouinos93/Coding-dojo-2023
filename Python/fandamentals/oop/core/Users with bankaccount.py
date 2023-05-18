class BankAccount:
    def init(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        elif self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        return(f"Balance: ${self.balance}")

    def yield_interest(self):
        self.balance = self.balance * self.int_rate + self.balance
        return self

class User:
    def init(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount (int_rate = 0.02, balance = 0)
        # self.account2 = BankAccount ("savings",int_rate = 0.02, balance = 0) would use this to add separate account

    def transfer_money(self, amount, other_user):
        self.account.balance = self.account.balance - amount
        other_user.account.balance = other_user.account.balance + amount 
        print(f"{self.name} just transferred {amount} dollars to {other_user.name}")
        return self

    def display_account_info(self):
        print(f"Name: {self.name}, {self.account.display_account_info()}")
        return self

Demo = User("Demo","Demo@gmail.com")
yassine = User("yassine","yassine@dogmail.com")

yassine.account.deposit(100)
yassine.display_account_info()
Demo.account.deposit(500)

yassine.transfer_money(500,Demo)
Demo.account.deposit(100).withdraw(50).display_account_info()