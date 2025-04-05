class Index_Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def print_index_card(self):
        while True:
            print(f"{self.value}")
            input("")
            print(f"{self.name}")
            if input("Flip card again? (y/n) ").lower() != "y":
                break

    def update_name(self, new_name):
        if self.name == new_name:
            print("Please enter a new name for the flash card")
            return False
        self.name = new_name
        print(f"Name successfully updated to {new_name}")
        return True

    def update_value(self, new_value):
        if self.value == new_value:
            print("Please enter a new value for the flash card")
            return False
        self.value = new_value
        print(f"value successfully updated to {new_value}")
        return True

    def __eq__(self, other):
        if not isinstance(other, Index_Card):
            return False
        return self.name == other.name and self.value == other.value

    def __hash__(self):
        return hash((self.name, self.value))


class Index_Card_Set:
    def __init__(self, name: str):
        self.set_name = name
        self.cards = set()

    def add_card(self, name, value):
        new_card = Index_Card(name, value)
        if not new_card in self.cards:
            self.cards.add(new_card)
            print(f"Successfully added {name}")
            return True
        print("Card is already in the set")
        return False

    def add_existing_card(self, card) -> bool:
        if not isinstance(card, Index_Card):
            print("Must add an index card")
            return False
        elif not card in self.cards:
            self.cards.add(card)
            print(f"Successfully add {card.name}")
            return True
        print("Card is already in set")
        return False

    def remove_card(self, card: Index_Card):
        try:
            self.cards.remove(card)
            print("Your card was successfully removed")
            return True
        except KeyError:
            print("Card does not exist")
            return False

    def display_cards(self):
        if not self.cards:
            print("No cards in the set")
        for card in self.cards:
            card.print_index_card()
            print("-" * 50)


def main():
    print("Welcome to the index card system")
    print("-" * 50)

    choice = input(
        "Do you want to (1) create a new set or (2) load existing one? (1/2): ")

    if choice == "1":
        name = input("Enter the new set's name: ")
        card_set = Index_Card_Set(name)
        print(f"Created new set: {name}")
    elif choice == "2":
        filename = input("Enter the filename to load: ")
        try:
            card_set = Index_Card_Set.load_from_file(filename)
        except:
            print("Error loading file name. Creating new card set")
            name = input("Enter the new set's name: ")
            card_set = Index_Card_Set(name)
            print(f"Created new set: {name}")
    else:
        print("Invalid choice. Creating a default set.")
        card_set = Index_Card_Set("My Card Set")
