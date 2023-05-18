from Bank_account import BankAccount

class User(BankAccount):
    def init(self,name,int_rate,balance):
        super().init(self)
        self.name=name
        self.int_rate=int_rate
        self.balance=balance


    def make_deposit(self, amount):
        super().deposit(amount)
        return self


    def make_withdrawal(self, amount):
        super().withdraw(amount)
        return self

    def display_user_balance(self):
        print(f'Your balance now is {self.balance}')
        return self


