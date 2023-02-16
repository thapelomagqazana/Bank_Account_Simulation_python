# Account class

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Incorrect Password!')
            return None
        
        if amountToDeposit < 0:
            print('You cannot deposit a negative amount!')
            return None

        self.balance += amountToDeposit
        return self.balance

    def withdrawal(self, amountToWithdraw, password):
        if password != self.password:
            print('Incorrect Password!')
            return None

        if amountToWithdraw > self.balance:
            print('You cannot withdraw more than what is in your balance!')
            return None

        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount!')
            return None

        self.balance -= amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print('Incorrect Password!')
            return None
        return self.balance

    # Added for debugging    
    def show(self):
        print(f'    Name:     {self.name}')
        print(f'    Balance:  {self.balance}')
        print(f'    Password: {self.password}')
        print()