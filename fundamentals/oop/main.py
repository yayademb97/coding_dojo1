class BankAccount:

    all_accounts = []
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        # Append all instances to all accounts list
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a 5$")
            self.balance -=5
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def print_account(cls):
        for acc in cls.all_accounts:
            print(f"Balance: {acc.balance}, Interest rate: {acc.int_rate}")
#User-CLASS
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0) #Abstraction

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw1(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"{self.name} Balance: {self.account.balance}")
        return self

acc1 = BankAccount()

# acc1.deposit(200).withdraw(50).display_account_info().yield_interest().display_account_info()

acc2 = BankAccount(0.04, 3000)
acc3 = BankAccount(0.03, 2000)

# acc2.deposit(200).withdraw(50).display_account_info().yield_interest().display_account_info()

# print("********************************************************************************************")
BankAccount.print_account()

john = User("John", "john@gmail.com")
john.display_user_balance().make_deposit(500).make_deposit(200).make_withdraw1(300).display_user_balance()



