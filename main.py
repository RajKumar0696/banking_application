from account import Account
from current import CurrentAccount
from saving import SavingsAccount
from bank import Bank


# menu function
def menu():
    choice = -1

    while choice < 0 or choice > 5:
        print("1. Create an Account")
        print("2. Check Account Balance")
        print("3. Deposit an Amount")
        print("4. Withdraw an Amount")
        print("5. Transfer an Amount")
        print("0. Exit")
        choice = int(input("Enter choice:-->"))
    return choice


# Create an account
def createAccount(bank):
    # Menu to user to select account type
    choise = -1

    while choise < 0 or choise > 2:
        print("Select Account Type")
        print("1. current account")
        print("2. saving account")
        print("0. back to main")
        choise = int(input("Enter choise:-->"))
        print("Enter below details:")
        print("Your name:")
        print("2. saving account")

    if choise == 1:
        current = CurrentAccount(Bank.getNextAccountNumber(),Name=input("Enter your Name:"))
        bank.add_account(current)
        print("Successfully created a current account:", current.getAccountNumber(),current.Name)


    elif choise == 2:
        saving = SavingsAccount(Bank.getNextAccountNumber(),Name=input("Enter your Name:"))
        bank.add_account(saving)
        print("Successfully created a saving account:", saving.getAccountNumber(),saving.Name)


# check balance
def checkBalance(bank):
    accountNumber = int(input("Enter account number:"))
    bank.checkBalance(accountNumber)


# deposit function
def doDeposit(bank):
    accountNumber = int(input("Enter account number:"))
    amount = float(input("Enter an amount to deposit:"))
    bank.deposit(accountNumber, amount)


# Withdraw function
def doWithdraw(bank):
    accountNumber = int(input("Enter account number:"))
    amount = float(input("Enter an amount to deposit:"))
    bank.withdraw(accountNumber, amount)


# Transfer function
def doTransfer(bank):
    fromAccountNumber = int(input("Enter From account number:"))
    toAccountNumber = int(input("Enter an To account number:"))
    amount = float(input("Enter an amount to transfer:"))
    bank.transfer(fromAccountNumber, toAccountNumber, amount)


# press the green button in the gutter to run the script.
if __name__ == '__main__':
    bank = Bank()
    choice = -1

    while choice != 0:
        choice = menu()
        print()

        if choice == 1:  # create an account
            createAccount(bank)
        elif choice == 2:  # check balance
            checkBalance(bank)
        elif choice == 3:  # deposit an amount
            doDeposit(bank)
        elif choice == 4:  # withdraw an amount
            doWithdraw(bank)
        elif choice == 5:  # transfer an amount
            doTransfer(bank)
        else:
            print("GoodBye....")
