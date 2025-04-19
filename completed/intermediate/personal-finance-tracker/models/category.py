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
        if self.name and self.name.isalnum():
            return True
        return False

    def is_expense_category(self) -> bool:
        """
        Checks if this is an expense category.
        Returns True for expense categories, False for income categories.
        """
        return self.category_type == "expense"

    def update_category(self, new_name: Optional[str] = None,
                        new_description: Optional[str] = None,
                        new_type: Optional[str] = None) -> None:
        """
        Updates category details. Only updates provided fields.
        Others remain unchanged.
        """
        if new_name and new_name.isalnum():
            self.name = new_name
        if new_description:
            self.description = new_description
        if new_type and new_type in ["expense", "income"]:
            self.category_type = new_type

    def to_dict(self) -> dict:
        """
        Converts category to dictionary format for storage/serialization.
        Useful for saving to JSON or database.
        """
        info = {
            "name": self.name,
            "description": self.description,
            "type": self.category_type
        }
        return info

    @classmethod
    def from_dict(cls, data: dict) -> 'Category':
        """
        Creates a Category instance from a dictionary.
        Useful for loading from JSON or database.
        """
        if not all(key in data for key in ["name", "description", "type"]):
            raise ValueError("Dictionary missing fields ")
        else:
            return cls(data["name"], data["description"], data["type"])

    def __eq__(self, other: 'Category') -> bool:
        """
        Defines how to compare two categories for equality.
        Two categories might be equal if they have the same name.
        """
        return self.name == other.name and self.description == other.description and self.category_type == other.category_type

    def __str__(self) -> str:
        """
        Returns a string representation of the category.
        This is more Pythonic than having a print_category method.
        """
        if self.description and self.category_type:
            return f"Category: {self.name}\nDescription: {self.description}\nType: {self.category_type}"
        elif self.description:
            return f"Category: {self.name}\nDescription: {self.description}"
        elif self.category_type:
            return f"Category: {self.name}\nType: {self.category_type}"
        else:
            return f"Category: {self.name}"


