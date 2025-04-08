import json


class Index_Card:
    def __init__(self, name, value):
        # TODO: Initialize card attributes
        pass

    def display_card(self) -> None:
        # TODO: Display the card in a formatted way
        # TODO: Show front (name) first
        # TODO: Allow flipping to show back (value)
        pass

    def update_name(self, new_name):
        # TODO: Update the card's name
        # TODO: Validate the new name
        pass

    def update_value(self, new_value):
        # TODO: Update the card's value
        # TODO: Validate the new value
        pass

    def __eq__(self, other):
        # TODO: Implement equality comparison
        pass

    def __hash__(self):
        # TODO: Implement hashing for set operations
        pass


class Index_Card_Set:
    def __init__(self, name: str):
        # TODO: Initialize card set attributes
        pass

    def add_card(self, name, value):
        # TODO: Create and add a new card to the set
        # TODO: Check for duplicates
        pass

    def add_existing_card(self, card) -> bool:
        # TODO: Add an existing card to the set
        # TODO: Validate card type
        # TODO: Check for duplicates
        pass

    def remove_card(self, card: Index_Card):
        # TODO: Remove a card from the set
        # TODO: Handle case where card doesn't exist
        pass

    def display_cards(self):
        # TODO: Display all cards in the set
        # TODO: Handle empty set case
        pass

    def upload_to_file(self, filename):
        # TODO: Save the card set to a JSON file
        # TODO: Handle file operations safely
        pass

    @staticmethod
    def load_from_file(filename):
        # TODO: Load a card set from a JSON file
        # TODO: Handle file operations safely
        # TODO: Validate file format
        pass


def main():
    # TODO: Implement main program flow
    # TODO: Create or load card set
    # TODO: Provide menu for card set management
    pass


def manage_card_set(card_set):
    # TODO: Implement card set management menu
    # TODO: Add/remove cards
    # TODO: Display cards
    # TODO: Save to file
    pass


if __name__ == "__main__":
    main()
