import random

# Predefined character sets
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SPECIAL = "!@#$%^&*()_+-=[]{}|;:,.<>?"


def enough_chars(num_chars, modifiers):
    mods = 0
    for val in modifiers.values():
        if val == "y":
            mods += 1

    if num_chars >= (mods + 1):
        return True
    return False


def get_input(modifier):
    while True:
        ans = input(
            f"Do you need to include {modifier}? (y/n) ").strip().lower()
        if ans in ["y", "n"]:
            return ans
        print("Invalid entry try again")


def generate_password(num_char, modifiers):
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


def main():
    print("Welcome to the password generator.")
    print("First enter how many characters you need")
    print("Then any modifiers you need such as numbers, special characters, and uppercase letters")
    while True:
        try:
            num_char = int(
                input("How many characters does the password need? "))
        except ValueError:
            print("Please enter a valid number")
            continue
        uppercase = input("Do you need to include uppcase letters? (y/n) ")
