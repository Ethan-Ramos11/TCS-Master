import random


def get_player_choice():
    """
    Get the player's choice (rock, paper, or scissors).

    Returns:
        str: Player's choice ('r', 'p', or 's')
    """
    choice = ""
    while choice.lower() not in {"r", "p", "s"}:
        choice = input(
            "Enter your choice r for rock, p for paper, or s for scissors")
    return choice


def get_computer_choice():
    """
    Generate the computer's choice.

    Returns:
        str: Computer's choice ('r', 'p', or 's')
    """
    return random.choice(["r", "p", "s"])


def determine_winner(player_choice, computer_choice):
    """
    Determine the winner of the round.

    Args:
        player_choice (str): Player's choice
        computer_choice (str): Computer's choice

    Returns:
        str: 'player', 'computer', or 'tie'
    """
    conditions = {("r", "s"), ("s", "p"), ("p", "r")}
    if (player_choice, computer_choice) in conditions:
        return "player"
    elif player_choice == computer_choice:
        return "tie"
    else:
        return "computer"


def update_stats(stats, result):
    """
    Update game statistics based on the round result.

    Args:
        stats (dict): Current game statistics
        result (str): Round result ('player', 'computer', or 'tie')
    """
    stats[result] += 1


def display_stats(stats):
    """
    Display current game statistics.

    Args:
        stats (dict): Current game statistics
    """
    print(
        f"Wins: {stats["player"]}, Losses: {stats["computer"]}, Draws: {stats["tie"]}")


def main():
    """
    Main function to run the game.
    Handles the game loop and player interaction.
    """
    stats = {"player": 0,
             "computer": 0,
             "tie": 0}
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Enter your choice: 'r', 'p', or 's'")
    print("Type 'quit' at any time to exit the game\n")

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {player_choice}")
        print(f"The computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        update_stats(stats, result)

        if result == "tie":
            print("It was a draw")
        elif result == "computer":
            print("The computer won. Better luck next time.")
        else:
            print("Nice you won!")
        display_stats(stats)

        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again != "y":
            break

    print("\n=== Final Game Summary ===")
    print(f"Total games played: {sum(stats.values())}")
    print(f"Wins: {stats['player']}")
    print(f"Losses: {stats['computer']}")
    print(f"Draws: {stats['tie']}")
    print("\nThanks for playing! Goodbye!")


if __name__ == "__main__":
    main()
