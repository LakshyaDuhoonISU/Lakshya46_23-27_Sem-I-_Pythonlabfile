# Build a simulation of an ATM system with classes for accounts, transactions, and
# users. Implement methods for withdrawing cash, checking balances, and handling
# PIN verification.
class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def withdraw_cash(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: {amount}")
            return amount
        else:
            return 0

    def deposit_money(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: {amount}")
            return amount
        else:
            return 0

    def check_balance(self):
        return self.balance

    def view_transaction_history(self):
        return self.transaction_history

class Transaction:
    def __init__(self, source_account, target_account, amount):
        self.source_account = source_account
        self.target_account = target_account
        self.amount = amount

class User:
    def __init__(self, username, accounts):
        self.username = username
        self.accounts = accounts

    def verify_pin(self, account_number, pin):
        for account in self.accounts:
            if account.account_number == account_number and account.pin == pin:
                return True
        return False

class ATMSimulation:
    def __init__(self):
        self.users = []

    def add_user(self, username, accounts):
        user = User(username, accounts)
        self.users.append(user)
        return user

    def perform_transaction(self, source_account, target_account, amount):
        transaction = Transaction(source_account, target_account, amount)
        return transaction

def display_menu():
    print("\n1. Check Balance")
    print("2. Withdraw Cash")
    print("3. Deposit Money")
    print("4. View Transaction History")
    print("5. Exit")

def main():
    atm_system = ATMSimulation()

    # Create accounts
    account1 = Account("123456789", "1234", 1000)
    account2 = Account("987654321", "5678", 500)

    # Create users
    user1 = atm_system.add_user("Alice", [account1])
    user2 = atm_system.add_user("Bob", [account2])

    while True:
        print("\n---- ATM Menu ----")
        user_input_account_number = input("Enter your account number: ")
        user_input_pin = input("Enter your PIN: ")

        for user in atm_system.users:
            if user.verify_pin(user_input_account_number, user_input_pin):
                print("\nPIN Verified!")
                source_account = None
                for account in user.accounts:
                    if account.account_number == user_input_account_number:
                        source_account = account

                if source_account:
                    while True:
                        display_menu()
                        choice = input("Enter your choice (1/2/3/4/5): ")

                        if choice == '1':
                            #Check bank balance
                            print(f"\nYour current balance: {source_account.check_balance()}")
                        elif choice == '2':
                            #Withdraw money
                            withdrawal_amount = int(input("Enter withdrawal amount: "))
                            withdrawn_amount = source_account.withdraw_cash(withdrawal_amount)

                            if withdrawn_amount > 0:
                                print(f"Withdrawal successful. Remaining balance: {source_account.check_balance()}")
                            else:
                                print("Invalid withdrawal amount or insufficient balance.")
                        elif choice == '3':
                            #Deposit money
                            deposit_amount = int(input("Enter deposit amount: "))
                            deposited_amount = source_account.deposit_money(deposit_amount)

                            if deposited_amount > 0:
                                print(f"Deposit successful. Updated balance: {source_account.check_balance()}")
                            else:
                                print("Invalid deposit amount.")
                        elif choice == '4':
                            #Check transaction history
                            transaction_history = source_account.view_transaction_history()
                            print("\nTransaction History:")
                            for transaction in transaction_history:
                                print(transaction)
                        elif choice == '5':
                            #Exit
                            print("Exiting ATM. Thank you!")
                            exit()
                        else:
                            print("Invalid choice. Please try again.")

                else:
                    print("Invalid account number.")
                break
        else:
            print("PIN verification failed. Exiting...")
            break

if __name__ == "__main__":
    main()