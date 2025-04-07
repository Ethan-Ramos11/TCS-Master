import json


class Index_Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def display_card(self) -> None:
        card_width = max(len(self.name), len(self.value)) + 10

        def draw_card(content):
            print("+" + "-" * card_width + "+")
            print("|" + " " * card_width + "|")

            # Center the content
            padding = (card_width - len(content)) // 2
            print("|" + " " * padding + content + " " *
                  (card_width - padding - len(content)) + "|")

            print("|" + " " * card_width + "|")
            print("+" + "-" * card_width + "+")

        while True:
            draw_card(self.name)
            input("\nPress Enter to flip the card...")

            print("\n" * 3)

            draw_card(self.value)

            if input("\nFlip card again? (y/n): ").lower() != "y":
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
            card.display_card()
            print("-" * 50)

    def upload_to_file(self, filename):
        try:
            card_set_data = {
                "set_name": self.set_name,
                "cards": []
            }
            for card in self.cards:
                card_data = {
                    "name": card.name,
                    "value": card.value
                }
                card_set_data["cards"].append(card_data)

            with open(filename, "w") as file:
                json.dump(card_set_data, file, indent=4)
            print(f"Successfully uploaded {self.set_name} to {filename}")
            return True
        except Exception as e:
            print(f"Error saving card set: {e}")

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, "r") as file:
                card_set_data = json.load(file)
            card_set = Index_Card_Set(card_set_data["set_name"])

            for card in card_set_data["cards"]:
                new_card = Index_Card(card["name"], card["value"])
                card_set.add_existing_card(new_card)
            print(f"Successfully loaded card set from {filename}")
            return card_set

        except Exception as e:
            print(f"Error loading card set: {e}")
            raise


def main():
    print("Welcome to the Index Card System!")
    print("-" * 50)

    while True:
        choice = input(
            "Do you want to (1) create a new set, (2) load existing one, or (3) exit? (1/2/3): ")

        if choice == "1":
            name = input("Enter the new set's name: ")
            card_set = Index_Card_Set(name)
            print(f"Created new set: {name}")
            manage_card_set(card_set)
        elif choice == "2":
            filename = input("Enter the filename to load: ")
            try:
                card_set = Index_Card_Set.load_from_file(filename)
                manage_card_set(card_set)
            except:
                print("Error loading file. Creating new card set")
                name = input("Enter the new set's name: ")
                card_set = Index_Card_Set(name)
                print(f"Created new set: {name}")
                manage_card_set(card_set)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def manage_card_set(card_set):
    while True:
        print("\nCard Set Management")
        print("-" * 50)
        print(f"Current Set: {card_set.set_name}")
        print("1. Add a new card")
        print("2. Remove a card")
        print("3. Display all cards")
        print("4. Save set to file")
        print("5. Return to main menu")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            name = input("Enter card name: ")
            value = input("Enter card value: ")
            card_set.add_card(name, value)
        elif choice == "2":
            name = input("Enter card name to remove: ")
            value = input("Enter card value to remove: ")
            card_to_remove = Index_Card(name, value)
            card_set.remove_card(card_to_remove)
        elif choice == "3":
            card_set.display_cards()
        elif choice == "4":
            filename = input("Enter filename to save (include .json): ")
            card_set.upload_to_file(filename)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
