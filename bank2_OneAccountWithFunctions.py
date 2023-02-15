# Non-OOP
# Bank_2
# Single account

accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password

def show():
    global accountName, accountBalance, accountPassword

    print(f'   Account Name:     {accountName}')
    print(f'   Account Balance:  {accountBalance}')
    print(f'   Account Password: {accountPassword}')

def getBalance(password):
    global accountName, accountBalance, accountPassword

    if password != accountPassword:
        print('Incorrect Password!')
        return None
    return accountBalance

def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword

    if not amountToDeposit.isdigit():
        print('Deposit must be a number!')
        return None
    if int(amountToDeposit) < 0:
        print('You cannot deposit a negative amount!')
        return None
    if password != accountPassword:
        print('Incorrect Password!')
        return None
    accountBalance += int(amountToDeposit)
    return accountBalance

def withdrawal(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword

    if not amountToWithdraw.isdigit():
        print('Withdrawal must be a number!')
        return None
    if int(amountToWithdraw) < 0:
        print('You cannot withdraw a negative amount!')
        return None
    if password != accountPassword:
        print('Incorrect Password!')
        return None
    if int(amountToWithdraw) > accountBalance:
        print('You cannot withdraw MORE than the amount in your balance')
        return None
    accountBalance -= int(amountToWithdraw)
    return accountBalance

newAccount('Joe', 0, 'soup')
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
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print(f'Your balance is: {theBalance}')

    elif action.startswith('d'):
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userPassword = input('Please enter the password: ')
        theDeposit = deposit(userDepositAmount,userPassword)
        if theDeposit is not None:
            print(f'Your new balance is: {theDeposit}')

    elif action.startswith('w'):
        print('Withdrawal:')
        userWithdrawalAmount = input('Please enter amount to withdrawal: ')
        userPassword = input('Please enter the password: ')
        theWithdrawal = withdrawal(userDepositAmount,userPassword)
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