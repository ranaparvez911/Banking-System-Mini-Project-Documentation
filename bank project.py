class BankAccount:
    def __init__(self, account_number, account_holder, initial_deposit=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_deposit
        self.transactions = [("Initial Deposit", initial_deposit)]

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(("Deposit", amount))
            print(f"Deposited {amount} to account {self.account_number}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(("Withdrawal", amount))
            print(f"Withdrew {amount} from account {self.account_number}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")
        return self.balance

    def add_transaction(self, description, amount):
        self.transactions.append((description, amount))

    def print_statement(self):
        print(f"Transaction history for account {self.account_number}:")
        for transaction, amount in self.transactions:
            print(f"{transaction}: {amount}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account_holder, initial_deposit=0):
        account_number = len(self.accounts) + 1
        account = BankAccount(account_number, account_holder, initial_deposit)
        self.accounts[account_number] = account
        print(f"Account {account_number} opened for {account_holder} with initial deposit {initial_deposit}.")
        return account

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer(self, sender_account_number, receiver_account_number, amount):
        sender = self.get_account(sender_account_number)
        receiver = self.get_account(receiver_account_number)
        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f"Transferred {amount} from account {sender_account_number} to account {receiver_account_number}")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Invalid account number(s).")

    def admin_check_total_deposit(self):
        total_deposits = sum(account.balance for account in self.accounts.values())
        print(f"Total deposits in the bank: {total_deposits}")
        return total_deposits

    def admin_check_total_accounts(self):
        total_accounts = len(self.accounts)
        print(f"Total number of accounts: {total_accounts}")
        return total_accounts

if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\nBanking System Menu")
        print("1. Open a New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Account Balance")
        print("5. Transfer Money")
        print("6. View Transaction History")
        print("7. Admin: View Total Deposits")
        print("8. Admin: View Total Accounts")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter account holder's name: ")
            deposit = float(input("Enter initial deposit: "))
            bank.open_account(name, deposit)

        elif choice == "2":
            acc_num = int(input("Enter account number: "))
            account = bank.get_account(acc_num)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            acc_num = int(input("Enter account number: "))
            account = bank.get_account(acc_num)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            acc_num = int(input("Enter account number: "))
            account = bank.get_account(acc_num)
            if account:
                account.check_balance()
            else:
                print("Account not found.")

        elif choice == "5":
            sender_acc = int(input("Enter sender's account number: "))
            receiver_acc = int(input("Enter receiver's account number: "))
            amount = float(input("Enter amount to transfer: "))
            bank.transfer(sender_acc, receiver_acc, amount)

        elif choice == "6":
            acc_num = int(input("Enter account number: "))
            account = bank.get_account(acc_num)
            if account:
                account.print_statement()
            else:
                print("Account not found.")

        elif choice == "7":
            bank.admin_check_total_deposit()

        elif choice == "8":
            bank.admin_check_total_accounts()

        elif choice == "9":
            print("Exiting Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
