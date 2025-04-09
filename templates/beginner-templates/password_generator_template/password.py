import random

# Predefined character sets
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SPECIAL = "!@#$%^&*()_+-=[]{}|;:,.<>?"


def enough_chars(num_chars, modifiers):
    """
    Check if the requested password length is sufficient for the selected character types.

    Args:
        num_chars (int): The requested password length
        modifiers (dict): Dictionary containing character type modifiers and their values ('y' or 'n')

    Returns:
        bool: True if the length is sufficient, False otherwise
    """
    # TODO: Implement the function to check if the password length is sufficient
    # Hint: Count how many character types are required and ensure the length is at least that + 1
    pass


def get_input(modifier):
    """
    Get user input for whether to include a specific character type in the password.

    Args:
        modifier (str): The type of character being asked about (e.g., 'uppercase letters')

    Returns:
        str: 'y' if the character type should be included, 'n' if not
    """
    # TODO: Implement the function to get user input
    # Hint: Use a while loop to keep asking until valid input is received
    pass


def generate_password(num_char, modifiers):
    """
    Generate a random password based on the specified length and character requirements.

    Args:
        num_char (int): The desired length of the password
        modifiers (dict): Dictionary containing character type modifiers and their values ('y' or 'n')
            Keys can be 'uppercase', 'numbers', or 'special characters'

    Returns:
        str: A randomly generated password containing at least one of each requested character type
             and additional random characters to meet the length requirement
    """
    # TODO: Implement the password generation function
    # Hint:
    # 1. Start with a list containing at least one lowercase character
    # 2. Add required character types based on modifiers
    # 3. Fill the remaining length with random characters from allowed sets
    # 4. Shuffle the final password
    pass


def main():
    print("Welcome to the Password Generator!")
    print("This program will help you create secure passwords.")
    print("-" * 50)

    while True:
        print("\nPassword Requirements:")
        mods = {}
        uppercase = get_input("uppercase letters")
        nums = get_input("numbers")
        special_characters = get_input("special characters")

        mods["uppercase"] = uppercase
        mods["numbers"] = nums
        mods["special characters"] = special_characters

        while True:
            try:
                num_char = int(
                    input("\nHow many characters should the password have? "))
                if not enough_chars(num_char, mods):
                    print("Password length must be at least 4 characters.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        password = generate_password(num_char, mods)
        print("\nGenerated Password:", password)
        print("-" * 50)

        if input("\nGenerate another password? (y/n): ").lower() != 'y':
            print("\nThank you for using the Password Generator!")
            break


if __name__ == "__main__":
    main()
