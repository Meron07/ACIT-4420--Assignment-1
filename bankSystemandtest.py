class BankAccount:

    # Initializes the bank account with an account holder's name and an optional initial balance.
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # Depostits a positive amount to the account news balance.
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Withdraws a positive amount from the account if sufficient funds exist, otherwise prints an error message.
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def account_info(self):
        #returns a string with the account holder's name and current balance.
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        #initializes the savings account with an interest rate.
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        # Applies interest to the current balance and print the new balance.
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}")


class CheckingAccount(BankAccount):
    # withdraw an amount plus a transaction fee if sufficient funds exist, other wise prints an error message.
    def __init__(self, account_holder, balance=0, transaction_fee=1):
        super().__init__(account_holder, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        total = amount + self.transaction_fee
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if total <= self.balance:
            self.balance -= total
            print(f"Withdrew ${amount} + fee ${self.transaction_fee}. New balance: ${self.balance}")
        else:
            print("Insufficient funds for withdrawal plus transaction fee.")


# Create accounts
acc1 = BankAccount("Alice")
acc2 = SavingsAccount("Bob", 1000, 0.05)
acc3 = CheckingAccount("Charlie", 500, 2)

print("\n--- Standard Account ---")
acc1.deposit(200)
acc1.withdraw(50)
acc1.withdraw(200)  # over-withdraw test
print(acc1.account_info())

print("\n--- Savings Account ---")
acc2.deposit(500)
acc2.apply_interest()
acc2.withdraw(2000)  # insufficient funds
print(acc2.account_info())

print("\n--- Checking Account ---")
acc3.deposit(100)
acc3.withdraw(50)  # includes fee
acc3.withdraw(600)  # insufficient funds
print(acc3.account_info())

