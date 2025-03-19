import unittest
from tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        """Set up a new game for each test."""
        self.game = TicTacToe()

    def test_initial_board(self):
        """Test that the board is empty at start."""
        # TODO: Implement initial board test
        pass

    def test_valid_move(self):
        """Test that valid moves are accepted."""
        # TODO: Implement valid move test
        pass

    def test_invalid_move(self):
        """Test that invalid moves are rejected."""
        # TODO: Implement invalid move test
        pass

    def test_win_horizontal(self):
        """Test horizontal win condition."""
        # TODO: Implement horizontal win test
        pass

    def test_win_vertical(self):
        """Test vertical win condition."""
        # TODO: Implement vertical win test
        pass

    def test_win_diagonal(self):
        """Test diagonal win condition."""
        # TODO: Implement diagonal win test
        pass

    def test_board_full(self):
        """Test board full condition."""
        # TODO: Implement board full test
        pass

    def test_no_winner(self):
        """Test no winner condition."""
        # TODO: Implement no winner test
        pass


if __name__ == '__main__':
    unittest.main()
