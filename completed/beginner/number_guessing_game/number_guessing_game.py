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
    if guess == secret_number:
        print("Congratulations! You guessed the correct number!")
        return True
    elif guess < secret_number:
        print("Your guess is too low")
        return False
    else:
        print("Your guess is too high")
        return False


def main():
    """
    Main function to run the number guessing game.
    """
    print("Welcome to my random number guessing game!")
    print("The computer will randomly pick a number between 1-100")
    print("You will enter your guess and will be told if your guess is too low or high")
    print("The round ends when you guess the right number")
    print("To play again type in y")
    while True:
        random_number = generate_secret_number()
        guess = get_user_guess()

        while not check_guess(guess, random_number):
            guess = get_user_guess()
        con = input("Would you like to play again? (y/n) ").lower()
        if con != "y":
            break
    print("Hope you enjoyed playing goodbye!")


if __name__ == "__main__":
    main()
