class BankAccount:
    def __init__(self, balance, bank_account):
        self.balance = balance
        self.bank_account = bank_account

    def deposit(self):
        amount = float(input("Enter a deposit amount: "))
        while True:
            if amount > 0:
                self.balance += amount
                print(f'${amount} has been added to your account!\nYour current balance: ${self.balance:.2f}')
                break
            else:
                print("Invalid input! Try again.")
                amount = float(input("Enter a valid deposit amount: "))  # Ask for a valid input again

    def withdraw(self):
        amount = float(input("Enter a withdraw amount: "))
        while True:
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                return f'${amount} has been withdrawn from your account!\nYour current balance: ${self.balance:.2f}'
            else:
                print("Invalid input or insufficient funds! Try again.")
                amount = float(input("Enter a valid withdraw amount: "))  # Ask for a valid amount again

    def check_balance(self):
        return f'Your current balance: ${self.balance:.2f}'


def main():
    n = int(input("Enter account number: "))
    x = float(input("Enter your balance: "))
    account = BankAccount(x, n)

    print("----- Welcome to Bank Account Simulation -----")
    print("1. To check your balance")
    print("2. To deposit money")
    print("3. To withdraw money")
    print("4. To exit")

    while True:
        choice = input("Enter your choice: ").lower()
        if choice == "1":
            print("----- Here is your Balance -----")
            print(account.check_balance())
        elif choice == "2":
            print("----- Entering deposit account -----")
            account.deposit()
        elif choice == "3":
            print("----- Entering withdraw account -----")
            print(account.withdraw())  # Print the result of the withdrawal
        elif choice == "4":
            print("Exiting the system.....")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
