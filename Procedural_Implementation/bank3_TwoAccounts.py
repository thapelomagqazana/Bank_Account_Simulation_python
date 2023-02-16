# Non-OOP
# Bank 3
# Two Accounts

account0Name = ''
account0Balance = 0
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password = ''
nAccounts = 0

def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password
    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password
    

def show():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if account0Name != '':
        print('Account 0')
        print(f'     Name:     {account0Name}')
        print(f'     Balance:  {account0Balance}')
        print(f'     Password: {account0Password}')
        print()
    if account1Name != '':
        print('Account 1')
        print(f'     Name:     {account1Name}')
        print(f'     Balance:  {account1Balance}')
        print(f'     Password: {account1Password}')
        print()

def getBalance(accountNumber, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    
    if accountNumber == 0:
        if account0Password != password:
            print('Incorrect password!')
            return None
        return account0Balance

    elif accountNumber == 1:
        if account1Password != password:
            print('Incorrect password!')
            return None
        return account1Balance

def deposit(accountNumber, amountToDeposit, password):    
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if not amountToDeposit.isdigit():
            print('Deposit must be a number!')
            return None
        if int(amountToDeposit) < 0:
            print('You cannot deposit a negative amount!')
            return None
        if password != account0Password:
            print('Incorrect Password!')
            return None
        account0Balance += int(amountToDeposit)
        return account0Balance
    
    elif accountNumber == 1:
        if not amountToDeposit.isdigit():
            print('Deposit must be a number!')
            return None
        if int(amountToDeposit) < 0:
            print('You cannot deposit a negative amount!')
            return None
        if password != account1Password:
            print('Incorrect Password!')
            return None
        account1Balance += int(amountToDeposit)
        return account1Balance

def withdrawal(accountNumber, amountToWithdraw, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if not amountToWithdraw.isdigit():
            print('Withdrawal must be a number!')
            return None
        if int(amountToWithdraw) < 0:
            print('You cannot withdraw a negative amount!')
            return None
        if password != account0Password:
            print('Incorrect Password!')
            return None
        if int(amountToWithdraw) > account0Balance:
            print('You cannot withdraw MORE than the amount in your balance')
            return None
        account0Balance -= int(amountToWithdraw)
        return account0Balance

    elif accountNumber == 1:
        if not amountToWithdraw.isdigit():
            print('Withdrawal must be a number!')
            return None
        if int(amountToWithdraw) < 0:
            print('You cannot withdraw a negative amount!')
            return None
        if password != account1Password:
            print('Incorrect Password!')
            return None
        if int(amountToWithdraw) > account1Balance:
            print('You cannot withdraw MORE than the amount in your balance')
            return None
        account1Balance -= int(amountToWithdraw)
        return account1Balance

newAccount(nAccounts, 'Joe', 0, 'soup')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ').lower().strip()

    if action.startswith('b'):
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(nAccounts, userPassword)
        if theBalance is not None:
            print(f'Your balance is: {theBalance}')

    elif action.startswith('d'):
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userPassword = input('Please enter the password: ')
        theDeposit = deposit(nAccounts, userDepositAmount,userPassword)
        if theDeposit is not None:
            print(f'Your new balance is: {theDeposit}')

    elif action.startswith('w'):
        print('Withdrawal:')
        userWithdrawalAmount = input('Please enter amount to withdrawal: ')
        userPassword = input('Please enter the password: ')
        theWithdrawal = withdrawal(nAccounts, userDepositAmount,userPassword)
        if theWithdrawal is not None:
            print(f'Your new balance is: {theWithdrawal}')

    elif action.startswith('q'):
        print('Done!')
        break

    elif action.startswith('s'):
        print('Your Account:')
        show()

    else:
        print('Invalid option')