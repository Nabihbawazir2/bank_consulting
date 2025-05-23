from config import DEFAULT_BALANCE, WITHDRAWAL_LIMIT
from datetime import datetime

class Account:
    def __init__(self, owner: str, balance: float = DEFAULT_BALANCE):
        self.owner = owner
        self.balance = balance
        self.transaction_history = []  # Stores transaction logs
        self.locked = False  # Flag to lock/unlock account

    def deposit(self, amount: float) -> None:
        self._check_locked()
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self._log_transaction("Deposit", amount)

    def withdraw(self, amount: float) -> None:
        self._check_locked()
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > WITHDRAWAL_LIMIT:
            raise ValueError("Withdrawal amount exceeds the allowed limit")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self._log_transaction("Withdrawal", -amount)

    def transfer_to(self, other_account: 'Account', amount: float) -> None:
        self._check_locked()
        if not isinstance(other_account, Account):
            raise TypeError("Recipient must be an Account instance")
        self.withdraw(amount)
        other_account.deposit(amount)
        self._log_transaction(f"Transfer to {other_account.owner}", -amount)
        other_account._log_transaction(f"Transfer from {self.owner}", amount)

    def get_balance(self) -> float:
        return self.balance

    def lock(self) -> None:
        self.locked = True

    def unlock(self) -> None:
        self.locked = False

    def is_locked(self) -> bool:
        return self.locked

    def get_transaction_history(self) -> list:
        return self.transaction_history.copy()

    def _log_transaction(self, action: str, amount: float) -> None:
        self.transaction_history.append({
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "amount": amount,
            "balance": self.balance
        })

    def _check_locked(self) -> None:
        if self.locked:
            raise PermissionError("Account is locked")

    def __str__(self):
        return f"Account({self.owner}, Balance: {self.balance:.2f}, Locked: {self.locked})"
