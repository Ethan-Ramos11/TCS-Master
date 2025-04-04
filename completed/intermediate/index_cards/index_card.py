
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
    