from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime
from category import Category
from account import Account


@dataclass
class Transaction:
    name: str
    id: str
    amount: float
    category: Category
    date: datetime
    transaction_type: str
    account: Account
    description: Optional[str]

    def validate_amount(self) -> bool:
        """
        Validates if the transaction amount is valid:
        - Must be positive
        - Must be a valid number
        """
        return type(self.amount) == float and self.amount > 0

    def is_income(self) -> bool:
        """
        Checks if this is an income transaction.
        Returns True for income transactions, False for expenses.
        """
        return self.transaction_type == "income"

    def is_expense(self) -> bool:
        """
        Checks if this is an expense transaction.
        Returns True for expense transactions, False for income.
        """
        return self.transaction_type == "expense"
    def update_transaction(self, new_name: Optional[str] = None,
                           new_amount: Optional[float] = None,
                           new_category: Optional[Category] = None,
                           new_description: Optional[str] = None,
                           new_type: Optional[str] = None) -> None:
        """
        Updates transaction details. Only updates provided fields.
        Others remain unchanged.
        """
        pass

    def to_dict(self) -> dict:
        """
        Converts transaction to dictionary format for storage/serialization.
        Useful for saving to JSON or database.
        """
        pass

    @classmethod
    def from_dict(cls, data: dict) -> 'Transaction':
        """
        Creates a Transaction instance from a dictionary.
        Useful for loading from JSON or database.
        """
        pass

    def __eq__(self, other: 'Transaction') -> bool:
        """
        Defines how to compare two transactions for equality.
        Two transactions might be equal if they have the same name and amount.
        """
        pass

    def __str__(self) -> str:
        """
        Returns a string representation of the transaction.
        Should include name, amount, date, and type.
        """
        return self.transaction_type == "income"pass
