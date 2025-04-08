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
    mods = 0
    for val in modifiers.values():
        if val == "y":
            mods += 1

    if num_chars >= (mods + 1):
        return True
    return False


def get_input(modifier):
    """
    Get user input for whether to include a specific character type in the password.

    Args:
        modifier (str): The type of character being asked about (e.g., 'uppercase letters')

    Returns:
        str: 'y' if the character type should be included, 'n' if not
    """
    while True:
        ans = input(
            f"Do you need to include {modifier}? (y/n) ").strip().lower()
        if ans in ["y", "n"]:
            return ans
        print("Invalid entry try again")


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
    val_chars = LOWERCASE
    s = [random.choice(LOWERCASE)]

    for mod, val in modifiers.items():
        if val == "y":
            if mod == "uppercase":
                s.append(random.choice(UPPERCASE))
                val_chars += UPPERCASE
            if mod == "special characters":
                s.append(random.choice(SPECIAL))
                val_chars += SPECIAL
            if mod == "numbers":
                s.append(random.choice(NUMBERS))
                val_chars += NUMBERS

    remaining = num_char - len(s)
    if remaining > 0:
        s.extend(random.choices(val_chars, k=remaining))

    random.shuffle(s)
    return "".join(s)

