class ATM:
    def __init__(self):
        """
        Initialize the ATM system with default values.
        """
        self.balance = 0.0
        self.transaction_history = []
        self.is_logged_in = False
        self.pin = "1234"

    def login(self, pin):
        """
        Authenticate user with PIN.

        Args:
            pin (str): User's PIN

        Returns:
            bool: True if login successful, False otherwise
        """
        if self.pin == pin:
            self.is_logged_in = True
            print("You are now logged in")
            return True
        print("Invalid pin")
        return False

    def logout(self):
        """
        Log out the current user.

        Returns:
            bool: True if logout successful, False otherwise
        """
        if self.is_logged_in:
            self.is_logged_in = False
            print("You were successfully logged out")
            return True
        print("You are not logged in")
        return False

    def check_balance(self):
        """
        Get current account balance.

        Returns:
            float: Current balance
        """
        if self.is_logged_in:
            print(f"Your balance is ${self.balance:.2f}")
            return self.balance
        print("Please login before you access the balance")
        return self.balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): Amount to deposit (assumed to be validated)

        Returns:
            bool: True if deposit successful, False otherwise
        """
        if not self.is_logged_in:
            print("Please log in first.")
            return False

        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount:.2f}")
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (float): Amount to withdraw (assumed to be validated)

        Returns:
            bool: True if withdrawal successful, False otherwise
        """
        if not self.is_logged_in:
            print("Please log in first.")
            return False

        if amount > self.balance:
            print("Insufficient funds.")
            return False
        if amount < 0:
            print("Cannot withdraw a negative amount")
            return False
        self.balance -= amount
        self.transaction_history.append(f"Withdrew ${amount:.2f}")
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True

    def transfer(self, amount, recipient_account):
        """
        Transfer money to another account.

        Args:
            amount (float): Amount to transfer
            recipient_account (ATM): Recipient's ATM account

        Returns:
            bool: True if transfer successful, False otherwise
        """
        if not self.is_logged_in:
            print("Please log in first.")
            return False

        if not isinstance(recipient_account, ATM):
            print("Invalid recipient account.")
            return False

        if amount <= 0:
            print("Amount must be greater than 0.")
            return False

        if amount > self.balance:
            print("Insufficient funds.")
            return False

        self.balance -= amount
        recipient_account.balance += amount

        self.transaction_history.append(
            f"Transferred ${amount:.2f} to account")
        recipient_account.transaction_history.append(
            f"Received ${amount:.2f} transfer")

        print(f"Transferred ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True

    def get_transaction_history(self):
        """
        Get list of recent transactions.

        Returns:
            list: List of transaction records
        """
        if self.is_logged_in:
            return self.transaction_history
        print("Please login")
        return None

    def change_pin(self, old_pin, new_pin):
        """
        Change user's PIN.

        Args:
            old_pin (str): Current PIN
            new_pin (str): New PIN

        Returns:
            bool: True if PIN change successful, False otherwise
        """
        if not self.is_logged_in:
            print("Please log in first.")
            return False

        if self.pin != old_pin:
            print("Current PIN is incorrect.")
            return False

        if not new_pin.isdigit() or len(new_pin) != 4:
            print("Invalid new PIN format. PIN must be 4 digits.")
            return False

        if new_pin == old_pin:
            print("New PIN must be different from current PIN.")
            return False

        self.pin = new_pin
        print("PIN successfully updated.")
        return True


def main():
    """
    Main function to run the ATM system.
    """
    # TODO: Create ATM instance
    # TODO: Display welcome message
    # TODO: Implement main menu loop
    # TODO: Handle user input
    # TODO: Process menu options
    # TODO: Handle program exit
    pass


if __name__ == "__main__":
    main()
