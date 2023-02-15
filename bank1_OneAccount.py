# Non OOP
# Bank Version 1
# Single Account

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ').lower()

    if action.startswith('b'):
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            print(f'Your balance is: {accountBalance}')
    
    elif action.startswith('d'):
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userPassword = input('Please enter the password: ')

        if not userDepositAmount.isdigit():
            print('Deposit must be a number!')
        elif int(userDepositAmount) < 0:
            print('You cannot deposit a negative amount!')
        elif userPassword != accountPassword:
            print('Incorrect Password!')
        else:
            accountBalance += int(userDepositAmount)
            print(f'Your new balance is: {accountBalance}')

    elif action.startswith('w'):
        print('Withdrawal:')
        userWithdrawalAmount = input('Please enter amount to withdrawal: ')
        userPassword = input('Please enter the password: ')

        if not userWithdrawalAmount.isdigit():
            print('Withdrawal must be a number!')
        elif int(userWithdrawalAmount) < 0:
            print('You cannot withdraw a negative amount!')
        elif userPassword != accountPassword:
            print('Incorrect Password!')
        elif int(userWithdrawalAmount) > accountBalance:
            print('You cannot withdraw MORE than the amount in your balance')
        else:
            accountBalance -= int(userWithdrawalAmount)
            print(f'Your new balance is: {accountBalance}')

    elif action.startswith('s'):
        print('Show Account:')
        print()
        print(f'      Account Name:     {accountName}')
        print(f'      Account Password: {accountPassword}')

    elif action.startswith('q'):
        break
    else:
        print('Invalid option')
