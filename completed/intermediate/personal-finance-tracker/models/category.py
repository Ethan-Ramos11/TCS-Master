from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Category:
    name: str
    description: Optional[str]
    category_type: str = "expense"  # Default to expense type

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def validate_name(self) -> bool:
        """
        Validates if the category name is proper:
        - Not empty
        - No special characters
        - Within length limits
        """
        pass

    def is_expense_category(self) -> bool:
        """
        Checks if this is an expense category.
        Returns True for expense categories, False for income categories.
        """
        pass

    def update_category(self, new_name: Optional[str] = None,
                        new_description: Optional[str] = None,
                        new_type: Optional[str] = None) -> None:
        """
        Updates category details. Only updates provided fields.
        Others remain unchanged.
        """
        pass

    def to_dict(self) -> dict:
        """
        Converts category to dictionary format for storage/serialization.
        Useful for saving to JSON or database.
        """
        info = {
            "name": self.name,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Category':
        """
        Creates a Category instance from a dictionary.
        Useful for loading from JSON or database.
        """
        pass

    def __eq__(self, other: 'Category') -> bool:
        """
        Defines how to compare two categories for equality.
        Two categories might be equal if they have the same name.
        """
        return self.name == other.name and self.description == other.description

    def __str__(self) -> str:
        """
        Returns a string representation of the category.
        This is more Pythonic than having a print_category method.
        """
        if self.description:
            print(f"Category: {self.name}\nDescription: {self.description}")
        else:
            print(f"Category: {self.name}")


test = Category("Test category", "This is a test category")
