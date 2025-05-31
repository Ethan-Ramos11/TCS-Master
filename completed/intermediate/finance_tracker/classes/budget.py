from .transactions import Transactions
from enum import Enum


class BudgetStatus(Enum):
    Over = 1
    Exact = 0
    Under = -1


class TimeFrameStatus(Enum):
    Week = 7
    Month = 30
    Year = 365


class Budget:
    def __init__(self, name: str, max_amount: int, curr_amount: int, time_frame: TimeFrameStatus):
        self.name = name
        self.max_amount = max_amount
        self.curr_amount = curr_amount
        self.time_frame = time_frame
        self.transactions = []

    def add_transaction(self, transaction: Transactions):
        self.transactions.append(transaction)
        self.curr_amount += transaction.amount

    def remove_transaction(self, transaction: Transactions) -> bool:
        if transaction in self.transactions:
            self.transactions.remove(transaction)
            self.curr_amount -= transaction.amount
            return True
        else:
            return False

    def check_budget(self) -> int:
        if self.curr_amount > self.max_amount:
            return BudgetStatus.Over
        elif self.curr_amount == self.max_amount:
            return BudgetStatus.Exact
        else:
            return BudgetStatus.Under

    def reset_budget(self):
        self.transactions = []
        self.curr_amount = 0

    def update_name(self, new_name) -> bool:
        if new_name == self.name:
            return False
        self.name = new_name
        return True

    def update_max(self, new_max) -> bool:
        if new_max == self.max_amount:
            return False
        self.max_amount = new_max
        return True

    def update_time_frame(self, new_timeframe: TimeFrameStatus) -> bool:
        if self.time_frame == new_timeframe:
            return False
        self.time_frame = new_timeframe
        return True
