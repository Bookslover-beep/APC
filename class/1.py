#Creates two BankAccount objects for two different account holders.
#Demonstrates the functionality of the methods by performing some deposits, withdrawals, and transfers between the accounts. 
#The class should have the following attributes and methods: 
#Attributes: 
#account_holder: The name of the person who owns the account. 
#balance: The current balance in the account (initial balance should be 0). 
#account_number: A unique number for the account (you can generate this automatically by keeping track of a class-level counter). 
#Methods: 
#1.deposit(amount): Adds the specified amount to the account balance. 
#2.withdraw(amount): Subtracts the specified amount from the balance, but only if the account has sufficient funds. Otherwise, print an error message. 
#3.display_balance(): Prints the current account balance. 
#4.transfer(amount, other_account): Transfers the specified amount from this account to another account, if sufficient balance is available. Otherwise, print an error message. 

class BankAccount:
    account_counter = 1000

    def __init__(self, account_holder):
        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into Account {self.account_number}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from Account {self.account_number}")
        else:
            print(f"Insufficient funds in Account {self.account_number}")

    def display_balance(self):
        print(f"Account {self.account_number} ({self.account_holder}) Balance: {self.balance}")

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transferred {amount} from Account {self.account_number} to Account {other_account.account_number}")
        else:
            print(f"Transfer failed: Insufficient funds in Account {self.account_number}")


acc1 = BankAccount("Prajakta")
acc2 = BankAccount("Shraddha")

acc1.deposit(5000)
acc2.deposit(2000)

acc1.display_balance()
acc2.display_balance()

acc1.withdraw(1000)
acc1.transfer(1500, acc2)

acc1.display_balance()
acc2.display_balance() 