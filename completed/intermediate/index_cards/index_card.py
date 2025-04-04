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


class index_card_set:
    def __init__(self, name):
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
