import random


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
        if ans not in ["y", "n"]:
            print("Invalid entry try again")
        return ans
