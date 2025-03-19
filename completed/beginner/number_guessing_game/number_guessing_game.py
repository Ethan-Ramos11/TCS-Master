import random


def generate_secret_number():
    """
    Generate a random number between 1 and 100.

    Returns:
        int: The secret number to guess
    """
    return random.randint(1, 100)


def get_user_guess():
    """
    Get input from the user for their guess.

    Returns:
        int: The user's guess
    """
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if guess in range(1, 101):
                return guess
            print("Your guess is out of the range, try again.")
        except ValueError:
            print("Please enter a valid integer")


def check_guess(guess, secret_number):
    """
    Check if the guess is correct and provide feedback.

    Args:
        guess (int): The user's guess
        secret_number (int): The secret number to guess

    Returns:
        bool: True if guess is correct, False otherwise
    """
    # TODO: Compare guess with secret number
    # TODO: Print appropriate feedback (too high, too low, correct)
    # TODO: Return True if guess is correct, False otherwise
    pass


def main():
    """
    Main function to run the number guessing game.
    """
    # TODO: Display welcome message
    # TODO: Start game loop
    # TODO: Handle game end
    pass


if __name__ == "__main__":
    main()
