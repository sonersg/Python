# Encapsulation


class BadBankAccount:
    def __init__(self, balance) -> None:
        self.balance = balance


bad_account = BadBankAccount(22.2)
bad_account.balance = -1
print(bad_account.balance)


class BankAccount:
    def __init__(self, balance) -> None:
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive!")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount


# We provided getter property but no setter
# so, it is not possible to modify from outside

account = BankAccount(0.0)
print(account.balance)
# account.balance = -1
account.deposit(333.3)
print(account.balance)
account.withdraw(111.1)
print(account.balance)
account.withdraw(999.9)
print(account.balance)
