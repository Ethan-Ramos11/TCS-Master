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
            amount (float): Amount to deposit

        Returns:
            bool: True if deposit successful, False otherwise
        """
        if self.is_logged_in:
            if amount > 0:
                self.balance += amount
                self.check_balance()
                return True
            else:
                print("You entered an invalid deposit amount")
        else:
            print("Please login before you deposit money")
        return False

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (float): Amount to withdraw

        Returns:
            bool: True if withdrawal successful, False otherwise
        """
        # TODO: Verify user is logged in
        # TODO: Validate amount
        # TODO: Check sufficient funds
        # TODO: Update balance
        # TODO: Record transaction
        # TODO: Return success status
        pass

    def transfer(self, amount, recipient_account):
        """
        Transfer money to another account.

        Args:
            amount (float): Amount to transfer
            recipient_account (str): Recipient's account number

        Returns:
            bool: True if transfer successful, False otherwise
        """
        # TODO: Verify user is logged in
        # TODO: Validate amount
        # TODO: Check sufficient funds
        # TODO: Update both balances
        # TODO: Record transaction
        # TODO: Return success status
        pass

    def get_transaction_history(self):
        """
        Get list of recent transactions.

        Returns:
            list: List of transaction records
        """
        # TODO: Verify user is logged in
        # TODO: Return transaction history
        pass

    def change_pin(self, old_pin, new_pin):
        """
        Change user's PIN.

        Args:
            old_pin (str): Current PIN
            new_pin (str): New PIN

        Returns:
            bool: True if PIN change successful, False otherwise
        """
        # TODO: Verify user is logged in
        # TODO: Validate old PIN
        # TODO: Validate new PIN format
        # TODO: Update PIN
        # TODO: Return success status
        pass


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
