# bank_account.py

class BankAccount:
    """A simple bank account class to manage deposits and withdrawals."""

    def __init__(self, initial_balance=0):
        """Initialize the bank account with a given balance."""
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount to the account."""
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account if funds are sufficient."""
        if amount > self.balance:
            return False  # Insufficient funds
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self.balance -= amount
            return True  # Successful withdrawal

    def display_balance(self):
        """Display the current balance of the account."""
        print(f"Current balance: ${self.balance:.2f}")
