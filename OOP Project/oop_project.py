

from bank_accounts import *

Soner = BankAccount(50, "Soner")
Ömer = BankAccount(60, "Ömer")

Soner.getBalance()
Ömer.getBalance()

Ömer.deposit(100)

Soner.withdraw(2000)
Soner.withdraw(20)
