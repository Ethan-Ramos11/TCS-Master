import unittest
from ..tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        """Set up a new game instance for each test."""
        self.game = TicTacToe()

    def test_initial_board(self):
        """Test that the board is empty at the start."""
        # TODO: Implement test
        pass

    def test_valid_move(self):
        """Test that valid moves are accepted."""
        # TODO: Implement test
        pass

    def test_invalid_move(self):
        """Test that invalid moves are rejected."""
        # TODO: Implement test
        pass

    def test_win_horizontal(self):
        """Test win condition in horizontal direction."""
        # TODO: Implement test
        pass

    def test_win_vertical(self):
        """Test win condition in vertical direction."""
        # TODO: Implement test
        pass

    def test_win_diagonal(self):
        """Test win condition in diagonal direction."""
        # TODO: Implement test
        pass

    def test_board_full(self):
        """Test that the board is full."""
        # TODO: Implement test
        pass

    def test_no_winner(self):
        """Test that there is no winner."""
        # TODO: Implement test
        pass


if __name__ == '__main__':
    unittest.main()
