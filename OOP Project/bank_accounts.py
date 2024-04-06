

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

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning transfer...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete...\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted: {error}")

class InterestRewardAcc(BankAccount):
    def deposit(self, amount):
        self.balance += amount * 1.05
        print("\nDeposit complete.")
        self.getBalance()

class SavingsAcc(InterestRewardAcc):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
