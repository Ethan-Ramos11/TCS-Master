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
            cell (int): Cell index (1-9)

        Returns:
            bool: True if move was valid and made, False otherwise

        Raises:
            ValueError: If cell is not between 1 and 9
        """
        if not 1 <= cell <= 9:
            raise ValueError("Move must be between 1 and 9")
        if self.board[cell - 1] != '_':
            return False
        self.board[cell - 1] = self.current_player
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

    def display_results(self):
        """
        Display the current game statistics.
        """
        print("\nGame Statistics:")
        print(f"Player X wins: {self.results['X']}")
        print(f"Player O wins: {self.results['O']}")
        print(f"Ties: {self.results['Tie']}")

    def reset_board(self):
        """
        Reset the board for a new game.
        """
        self.board = ['_'] * 9
        self.current_player = "X"


def main():
    """
    Main function to run the game.
    Handles the game loop and player turns.
    """
    print("Welcome to Tic Tac Toe!")
    print("Enter a number from 1-9 to make your move:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print("Enter 'q' to quit")
    print()
    game = TicTacToe()

    while True:
        game.display_board()
        try:
            move = input(f"Player {game.current_player} make your move: ")
            if move.lower() == 'q':
                print("\nThanks for playing!")
                print("\nFinal Statistics:")
                print("----------------")
                print(f"Player X wins: {game.results['X']}")
                print(f"Player O wins: {game.results['O']}")
                print(f"Draws: {game.results['Tie']}")
                break

            if not move.isdigit():
                print("Please enter a valid number!")
                continue

            move = int(move)
            if not game.make_move(move):
                print("That position is already taken!")
                continue

            winner = game.check_winner()
            if winner:
                game.display_board()
                print(f"Player {winner} wins!")
                game.display_results()
                play_again = input(
                    "\nWould you like to play again? (y/n): ").lower()
                if play_again != 'y':
                    break
                game.reset_board()
                continue
            elif game.is_board_full():
                game.display_board()
                print("It's a tie!")
                game.results["Tie"] += 1
                game.display_results()
                play_again = input(
                    "\nWould you like to play again? (y/n): ").lower()
                if play_again != 'y':
                    break
                game.reset_board()
                continue

        except ValueError:
            print("Invalid entry! Please enter a number between 1 and 9 or 'q' to quit.")
        except KeyboardInterrupt:
            print("\nGame ended by user.")
            game.display_results()
            break


if __name__ == "__main__":
    main()
