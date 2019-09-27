class User(object):
    def __init__(self):
        self.name = "Richard"
        self.email = "rkim2195@gmail.com"
        self.account_balance = 0

    def make_deposit(self, amount):	
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print("User: {}, Balance: {}".format(self.name, self.account_balance))
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance += interest
        return self

user1 = User()
user2 = User()
user3 = User()

user1.make_deposit(10).make_deposit(20).make_deposit(30).make_withdrawal(5).display_user_balance()

user2.make_deposit(10).make_deposit(20).make_withdrawal(5).make_withdrawal(5).display_user_balance()

user3.make_deposit(3).make_withdrawal(1).make_withdrawal(1).make_withdrawal(1).display_user_balance()

user1.transfer_money(user3, 55).display_user_balance()
user3.display_user_balance()
account1 = BankAccount(.5, 0)
account2 = BankAccount(.5, 0)

account1.deposit(1).deposit(1).deposit(1).withdraw(2).yield_interest().display_account_info()

account2.deposit(1).deposit(1).withdraw(.25).withdraw(.25).withdraw(.25).withdraw(.25).yield_interest().display_account_info()