

from bank_accounts import *

Soner = BankAccount(50, "Soner")
Ömer = BankAccount(60, "Ömer")

Soner.getBalance()
Ömer.getBalance()

Ömer.deposit(100)

Soner.withdraw(2000)
Soner.withdraw(20)

Soner.transfer(30, Ömer)

jim = InterestRewardAcc(1000, "Jim")
jim.deposit(100)
jim.getBalance()

kim = SavingsAcc(1000, "Kim")
kim.deposit(100)
kim.getBalance()
Soner.getBalance()
kim.transfer(100, Soner)
