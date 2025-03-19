class TicTacToe:
    def __init__(self):
        """
        Initialize a new Tic Tac Toe game.
        Creates an empty 3x3 board.
        """
        # TODO: Initialize the board
        self.winner = None
        self.current_player = "X"
        self.board = ['_'] * 9

    def make_move(self, cell):
        """
        Make a move on the board.

        Args:
            cell (int): Cell index (0-8)

        Returns:
            bool: True if move was valid and made, False otherwise
        """
        if self.board[cell] != '_':
            return False
        self.board[cell] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

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
