from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime
from category import Category


@dataclass
class Budget:
    category: Category
    amount_limit: float
    time_period: str  # "monthly", "yearly", etc.
    start_date: datetime
    end_date: Optional[datetime]
    current_spending: float = 0.0

    def validate_amount(self) -> bool:
        """
        Validates if the budget amount is valid:
        - Must be positive
        - Must be a valid number
        """
        return self.amount_limit > 0 and type(self.amount_limit) == float:

    def update_spending(self, amount: float) -> None:
        """
        Updates the current spending amount.
        Validates the amount before updating.
        """
        pass

    def get_remaining_amount(self) -> float:
        """
        Calculates how much budget is remaining.
        Returns the difference between limit and current spending.
        """
        pass

    def get_spending_percentage(self) -> float:
        """
        Calculates what percentage of the budget has been spent.
        Returns a value between 0 and 100.
        """
        pass

    def is_over_budget(self) -> bool:
        """
        Checks if the current spending exceeds the budget limit.
        """
        pass

    def reset_budget(self) -> None:
        """
        Resets the current spending to zero.
        Useful for starting a new budget period.
        """
        pass

    def update_budget(self, new_amount: Optional[float] = None,
                      new_time_period: Optional[str] = None,
                      new_end_date: Optional[datetime] = None) -> None:
        """
        Updates budget details. Only updates provided fields.
        Others remain unchanged.
        """
        pass

    def to_dict(self) -> dict:
        """
        Converts budget to dictionary format for storage/serialization.
        Useful for saving to JSON or database.
        """
        pass

    @classmethod
    def from_dict(cls, data: dict) -> 'Budget':
        """
        Creates a Budget instance from a dictionary.
        Useful for loading from JSON or database.
        """
        pass

    def __eq__(self, other: 'Budget') -> bool:
        """
        Defines how to compare two budgets for equality.
        Two budgets might be equal if they have the same category and time period.
        """
        pass

    def __str__(self) -> str:
        """
        Returns a string representation of the budget.
        Should include category, limit, current spending, and remaining amount.
        """
        pass
