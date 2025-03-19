class TicTacToe:
    def __init__(self):
        """
        Initialize a new Tic Tac Toe game.
        Creates an empty 3x3 board.
        """
        # TODO: Initialize the board
        pass

    def make_move(self, row, col, player):
        """
        Make a move on the board.

        Args:
            row (int): Row index (0-2)
            col (int): Column index (0-2)
            player (str): Player mark ('X' or 'O')

        Returns:
            bool: True if move was valid and made, False otherwise
        """
        # TODO: Implement move validation and placement
        pass

    def check_winner(self):
        """
        Check if there is a winner.

        Returns:
            str: 'X' if X wins, 'O' if O wins, None if no winner
        """
        # TODO: Implement win condition checking
        pass

    def is_board_full(self):
        """
        Check if the board is full.

        Returns:
            bool: True if board is full, False otherwise
        """
        # TODO: Implement board full check
        pass

    def display_board(self):
        """
        Display the current state of the board.
        """
        # TODO: Implement board display
        pass


def main():
    """
    Main function to run the game.
    Handles the game loop and player turns.
    """
    # TODO: Implement main game loop
    pass


if __name__ == "__main__":
    main()
