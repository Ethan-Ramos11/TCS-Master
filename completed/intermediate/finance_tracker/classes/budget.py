from .transactions import Transactions


class Budget:
    def __init__(self, name: str, max_amount: int, curr_amount: int, time_frame: str):
        self.name = name
        self.max_amount = max_amount
        self.curr_amount = curr_amount
        self.time_frame = time_frame
        self.transactions = []

    def add_transaction(self, transaction: Transactions):
        self.transactions.append(transaction)
        self.current_amount -= transaction.amount

    def remove_transaction(self, transaction: Transactions) -> bool:
        if transaction in self.transactions:
            self.transactions.remove(transaction)
            self.curr_amount += transaction.amount
            return True
        else:
            return False
        
    
