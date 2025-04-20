from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime
from transaction import Transaction
from category import Category


@dataclass
class Account:

    name: str
    balance: float
    account_type: str
    description: Optional[str]
    transactions: List[Transaction]

    def validate_balance(self) -> bool:
        """
        Validates if the account balance is valid:
        - Must be a valid number
        - Can be negative (for credit accounts)
        """
        return type(self.balance) == float

    def add_transaction(self, transaction: Transaction) -> None:
        """
        Adds a transaction to the account and updates the balance.
        Validates transaction before adding.
        """
        if transaction in self.transactions:
            print("Transaction already in the account")
        self.transactions.append(transaction)

    def remove_transaction(self, transaction: Transaction) -> None:
        """
        Removes a transaction from the account and updates the balance.
        Raises error if transaction not found.
        """
        if transaction not in self.transactions:
            raise KeyError(f"Print {transaction} not found")
        else:
            self.transaction.remove(transaction)

    def get_transactions_by_date(self, start_date: datetime,
                                 end_date: datetime) -> List[Transaction]:
        """
        Returns all transactions within the specified date range.
        """
        transactions_in_date_range = []
        if start_date > end_date:
            print("Invalid date range")
            return None
        for transaction in self.transactions:
            if start_date <= transaction.date <= end_date:
                transactions_in_date_range.append(transaction)
        return transactions_in_date_range

    def get_transactions_by_category(self, category: Category) -> List[Transaction]:
        """
        Returns all transactions matching the specified category.
        """
        transactions_with_category = []
        for transaction in self.transactions:
            if transaction.category == category:
                transactions_with_category.append(transaction)
        return transactions_with_category

    def get_balance_at_date(self, date: datetime) -> float:
        """
        Calculates the account balance as of a specific date.
        """

    def update_account(self, new_name: Optional[str] = None,
                       new_balance: Optional[float] = None,
                       new_type: Optional[str] = None,
                       new_description: Optional[str] = None) -> None:
        """
        Updates account details. Only updates provided fields.
        Others remain unchanged.
        """
        if type(new_name) == str and self.name != new_name:
            self.name = new_name
        if type(new_balance) == float and self.balance != new_balance:
            self.balance = new_balance
        if new_type and new_type in ["chekcing", "savings", "credit"]:
            self.account_type = new_type
        if type(new_description) == str and new_description != self.description:
            self.description = new_description

    def to_dict(self) -> dict:
        """
        Converts account to dictionary format for storage/serialization.
        Useful for saving to JSON or database.
        """
        pass

    @classmethod
    def from_dict(cls, data: dict) -> 'Account':
        """
        Creates an Account instance from a dictionary.
        Useful for loading from JSON or database.
        """
        pass

    def __eq__(self, other: 'Account') -> bool:
        """
        Defines how to compare two accounts for equality.
        Two accounts might be equal if they have the same name and type.
        """
        pass

    def __str__(self) -> str:
        """
        Returns a string representation of the account.
        Should include name, type, and current balance.
        """
        pass
