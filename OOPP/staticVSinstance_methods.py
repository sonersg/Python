# Static vs instance methods


class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance: ${self._balance}")

    @staticmethod  # decorator
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


account = BankAccount("Zeleha", 222)
account.deposit(28)

print(BankAccount.is_valid_interest_rate(1))
print(BankAccount.is_valid_interest_rate(7))
