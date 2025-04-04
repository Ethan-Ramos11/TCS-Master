
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
    
     
