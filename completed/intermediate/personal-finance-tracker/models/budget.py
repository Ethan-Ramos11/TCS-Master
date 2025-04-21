from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime
from category import Category


@dataclass
class Budget:
    category: Category
    amount_limit: float
    time_period: str  # "monthly", "yearly", weekly.
    start_date: datetime
    end_date: Optional[datetime]
    current_spending: float = 0.0

    def validate_amount(self) -> bool:
        """
        Validates if the budget amount is valid:
        - Must be positive
        - Must be a valid number
        """
        return self.amount_limit > 0 and type(self.amount_limit) == float

    def update_spending(self, amount: float) -> None:
        """
        Updates the current spending amount.
        Validates the amount before updating.
        """
        if type(amount) != float or amount < 0:
            raise ValueError("Invalid entry for spending amount")
        self.current_spending += amount

    def get_remaining_amount(self) -> float:
        """
        Calculates how much budget is remaining.
        Returns the difference between limit and current spending.
        """
        return self.amount_limit - self.current_spending

    def get_spending_percentage(self) -> float:
        """
        Calculates what percentage of the budget has been spent.
        Returns a value between 0 and 100.
        """
        return round(self.current_spending/self.amount_limit, 0)

    def is_over_budget(self) -> bool:
        """
        Checks if the current spending exceeds the budget limit.
        """
        return self.current_spending > self.amount_limit

    def reset_budget(self) -> None:
        """
        Resets the current spending to zero.
        Useful for starting a new budget period.
        """
        self.current_spending = 0

    def update_budget(self, new_amount: Optional[float] = None,
                      new_time_period: Optional[str] = None,
                      new_end_date: Optional[datetime] = None) -> None:
        """
        Updates budget details. Only updates provided fields.
        Others remain unchanged.
        """
        if type(new_amount) == float and new_amount > 0 and new_amount != self.amount_limit:
            self.amount_limit = new_amount
        if type(new_time_period) == str and new_time_period in ["monthly", "yearly", "weekly"] and new_time_period != self.time_period:
            self.time_period = new_time_period
        if type(new_end_date) == datetime and new_end_date != self.end_date:
            self.end_date = new_end_date

    def to_dict(self) -> dict:
        """
        Converts budget to dictionary format for storage/serialization.
        Useful for saving to JSON or database.
        """
        info = {
            "category": self.category,
            "amount_limit": self.amount_limit,
            "time_period": self.time_period,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "current_spending": self.current_spending
        }
        return info

    @classmethod
    def from_dict(cls, data: dict) -> 'Budget':
        """
        Creates a Budget instance from a dictionary.
        Useful for loading from JSON or database.
        """
        if not all(key in data for key in ["category",
                                           "amount_limit",
                                           "time_period",
                                           "start_date",
                                           "end_date",
                                           "current_spending"]):
            raise ValueError("Dictionary missing fields")
        return cls(data["category"],
                   data["amount_limit"],
                   data["time_period"],
                   data["start_date"],
                   data["end_date"],
                   data["current_spending"])

    def __eq__(self, other: 'Budget') -> bool:
        """
        Defines how to compare two budgets for equality.
        Two budgets might be equal if they have the same category and time period.
        """
        

    def __str__(self) -> str:
        """
        Returns a string representation of the budget.
        Should include category, limit, current spending, and remaining amount.
        """
        pass
