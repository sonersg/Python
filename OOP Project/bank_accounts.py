

class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created. \nBalance: {self.balance:.2f}₺")

    def getBalance(self):
        print(f"\nAccount '{self.name}' has balance: {self.balance:.2f}₺")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, '{self.name}' has only {self.balance:.2f}₺")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
