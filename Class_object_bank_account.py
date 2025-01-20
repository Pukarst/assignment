#   Class and Objects:  Bank Account

wel=('Welcome to the  Banking System')
print(wel.upper().center(50,'*'))

class Bank_Account:
    def __init__(self,account_number,account_holder,balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance

    def deposite_amount(self,amount):
        self.balance+=amount
        print(f'The deposite amount is {amount}. The remaining balance is {self.balance}')


    def withdraw_amount(self,amount):
        if amount>self.balance:
            print('The account do not contain the sufficient balance.Please enter the correct amount.') 

        elif amount<=self.balance:
            self.balance-=amount
            print(f'The withdrawn amount is{amount}. The remaining balance is{self.balance}')

obj=Bank_Account(141514151415,'XYZ',0)
obj.deposite_amount(int(input('Enter the amount to deposite--->')))
obj.withdraw_amount(int(input('Enter the amount to withdraw--->')))