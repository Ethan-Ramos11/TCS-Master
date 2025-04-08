import random
def get_input(modifier):
    while True:
        ans = input(
            f"Do you need to include {modifier}? (y/n) ").strip().lower()
        if ans not in ["y", "n"]:
            print("Invalid entry try again")
        return ans
