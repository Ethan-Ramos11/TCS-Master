from tic_tac_toe import TicTacToe
import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        """Set up a new game instance for each test."""
        self.game = TicTacToe()

    def test_initial_board(self):
        """Test that the board is empty at the start."""
        self.assertEqual(self.game.board, ['_'] * 9)
        self.assertEqual(self.game.current_player, "X")
        self.assertEqual(self.game.results, {"X": 0, "O": 0, "Tie": 0})

    def test_valid_move(self):
        """Test that valid moves are accepted."""
        # Test first move
        self.assertTrue(self.game.make_move(1))
        self.assertEqual(self.game.board[0], "X")
        self.assertEqual(self.game.current_player, "O")

        # Test second move
        self.assertTrue(self.game.make_move(2))
        self.assertEqual(self.game.board[1], "O")
        self.assertEqual(self.game.current_player, "X")

    def test_invalid_move(self):
        """Test that invalid moves are rejected."""
        # Test out of range move
        with self.assertRaises(ValueError):
            self.game.make_move(10)

        # Test occupied position
        self.game.make_move(1)  # X plays
        # O tries to play same position
        self.assertFalse(self.game.make_move(1))

    def test_win_horizontal(self):
        """Test win condition in horizontal direction."""
        # X plays top row
        self.game.make_move(1)  # X
        self.game.make_move(4)  # O
        self.game.make_move(2)  # X
        self.game.make_move(5)  # O
        self.game.make_move(3)  # X
        self.assertEqual(self.game.check_winner(), "X")

    def test_win_vertical(self):
        """Test win condition in vertical direction."""
        # X plays first column
        self.game.make_move(1)  # X
        self.game.make_move(2)  # O
        self.game.make_move(4)  # X
        self.game.make_move(5)  # O
        self.game.make_move(7)  # X
        self.assertEqual(self.game.check_winner(), "X")

    def test_win_diagonal(self):
        """Test win condition in diagonal direction."""
        # X plays diagonal
        self.game.make_move(1)  # X
        self.game.make_move(2)  # O
        self.game.make_move(5)  # X
        self.game.make_move(3)  # O
        self.game.make_move(9)  # X
        self.assertEqual(self.game.check_winner(), "X")

    def test_board_full(self):
        """Test that the board is full."""
        # Fill the board without a winner
        moves = [1, 2, 3, 5, 4, 6, 8, 7, 9]
        for move in moves:
            self.game.make_move(move)
        self.assertTrue(self.game.is_board_full())

    def test_no_winner(self):
        """Test that there is no winner."""
        # Fill the board without a winner
        moves = [1, 2, 3, 5, 4, 6, 8, 7, 9]
        for move in moves:
            self.game.make_move(move)
        self.assertIsNone(self.game.check_winner())
        self.assertTrue(self.game.is_board_full())

    def test_reset_board(self):
        """Test that the board resets properly."""
        # Make some moves
        self.game.make_move(1)
        self.game.make_move(2)
        self.game.make_move(3)

        # Reset the board
        self.game.reset_board()

        # Check board is empty and player is X
        self.assertEqual(self.game.board, ['_'] * 9)
        self.assertEqual(self.game.current_player, "X")


if __name__ == '__main__':
    unittest.main()
