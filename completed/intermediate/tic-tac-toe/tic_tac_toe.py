class TicTacToe:
    def __init__(self):
        """
        Initialize a new Tic Tac Toe game.
        Creates an empty 3x3 board.
        """
        self.previous_result = None
        self.results = {"X": 0, "O": 0, "Tie": 0}
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
        win_con = {(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                   (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)}
        for con in win_con:
            if self.board[con[0]] == self.board[con[1]] == self.board[con[2]] != "_":
                self.results[self.board[con[0]]] += 1
                self.previous_result = self.board[con[0]]
                return self.board[con[0]]
        return None

    def is_board_full(self):
        """
        Check if the board is full.

        Returns:
            bool: True if board is full, False otherwise
        """
        return "_" not in self.board

    def display_board(self):
        """
        Display the current state of the board.
        """
        s = ""
        for idx, cell in enumerate(self.board):
            s += f"|{cell}"
            if idx % 3 == 2:
                s += "|\n"
        print(s)


def main():
    """
    Main function to run the game.
    Handles the game loop and player turns.
    """


if __name__ == "__main__":
    main()
