class BankAccountSimulation:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposited: {amount}\nYour balance: {self.balance}')
        else:
            print('Invalid input or amount !')

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Insufficient funds\nYour balance: {self.balance}')
        elif amount > 0:
            self.balance -= amount
            print(f'Withdrawed: {amount}\nYour balance: {self.balance}')
        else:
            print('Invalid input or amount !')

    def check_balance(self):
        print(f'Your balance: {self.balance}')



