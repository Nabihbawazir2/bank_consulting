from config import DEFAULT_BALANCE, WITHDRAWAL_LIMIT
from transaction import Ledger
from security import Lockable

class Account(Lockable):
    def __init__(self, owner: str, balance: float = DEFAULT_BALANCE):
        super().__init__()
        self.owner = owner
        self.balance = balance
        self.ledger = Ledger()

    def deposit(self, amount: float):
        self._check_locked()
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self.ledger.record("Deposit", amount, self.balance)

    def withdraw(self, amount: float):
        self._check_locked()
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > WITHDRAWAL_LIMIT:
            raise ValueError("Exceeds withdrawal limit")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.ledger.record("Withdrawal", -amount, self.balance)

    def transfer_to(self, other_account: 'Account', amount: float):
        self._check_locked()
        if not isinstance(other_account, Account):
            raise TypeError("Must be an Account instance")
        self.withdraw(amount)
        other_account.deposit(amount)
        self.ledger.record(f"Transfer to {other_account.owner}", -amount, self.balance)
        other_account.ledger.record(f"Transfer from {self.owner}", amount, other_account.balance)

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.ledger.get_history()

    def __str__(self):
        return f"Account({self.owner}, Balance: {self.balance:.2f}, Locked: {self.is_locked()})"
