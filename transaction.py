from datetime import datetime

class Transaction:
    def __init__(self, action: str, amount: float, balance: float):
        self.timestamp = datetime.now().isoformat()
        self.action = action
        self.amount = amount
        self.balance = balance

    def __repr__(self):
        return f"{self.timestamp} | {self.action} | {self.amount:.2f} | Balance: {self.balance:.2f}"

class Ledger:
    def __init__(self):
        self.history = []

    def record(self, action: str, amount: float, balance: float):
        self.history.append(Transaction(action, amount, balance))

    def get_history(self):
        return [str(tx) for tx in self.history]
