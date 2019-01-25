class CheckingAccount:
    def __init__(self, owner):    # method, not function, constructor
        self.owner = owner        # attribute
        self.balance = 0.0        # attribute

    def deposit(self, amount):    # method
        self.balance += amount

    def withdraw(self, amount):   # method
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Balance of {} is insufficient.".format(
                self.owner))


account1 = CheckingAccount("Toon Verstraelen")
account1.deposit(2000.0)
account1.deposit(3000.0)
print(account1.balance)    # This will print 5000.0
account1.withdraw(4000.0)
account1.withdraw(4000.0)  # This would raise the ValueError


class HappyAccount(BankAccount):
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Your balance is negative. Happy shopping!")


account2 = HappyAccount("Paul Ayers")
account2.deposit(2000.0)
account2.deposit(3000.0)
print(account2.balance)    # This will print 5000.0
account2.withdraw(4000.0)
account2.withdraw(4000.0)  # This will print "Your balance is ...".



def print_balance(account):
    print("The balance on the account of {} is {}.".format(account.owner, account.balance))
