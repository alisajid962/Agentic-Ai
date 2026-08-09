class BankAccount:
    def account_type(self):
        print("Generic Account ")

class SavingAccount(BankAccount):
    def account_type(self):
        print("Saving Account")
class CurrentAccount(BankAccount):
    def account_type(self):
        print("Current Account ")


ob1 = SavingAccount()
ob1.account_type()

ob2 = CurrentAccount()
ob2.account_type()
