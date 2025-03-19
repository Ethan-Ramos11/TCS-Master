import unittest
from unittest.mock import patch
from rps import (
    get_player_choice,
    get_computer_choice,
    determine_winner,
    update_stats,
    display_stats
)


class TestRockPaperScissors(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.stats = {"player": 0, "computer": 0, "tie": 0}

    @patch('builtins.input', side_effect=['r'])
    def test_valid_player_choice(self, mock_input):
        """Test that valid player choices are accepted."""
        choice = get_player_choice()
        self.assertIn(choice, {'r', 'p', 's'})

    @patch('builtins.input', side_effect=['invalid', 'r'])
    def test_invalid_player_choice(self, mock_input):
        """Test that invalid choices are rejected until valid input is provided."""
        choice = get_player_choice()
        self.assertEqual(choice, 'r')

    def test_computer_choice(self):
        """Test that computer choices are valid."""
        choice = get_computer_choice()
        self.assertIn(choice, {'r', 'p', 's'})

    def test_winner_determination(self):
        """Test all possible game outcomes."""
        # Test player wins
        self.assertEqual(determine_winner('r', 's'), 'player')
        self.assertEqual(determine_winner('s', 'p'), 'player')
        self.assertEqual(determine_winner('p', 'r'), 'player')

        # Test computer wins
        self.assertEqual(determine_winner('s', 'r'), 'computer')
        self.assertEqual(determine_winner('p', 's'), 'computer')
        self.assertEqual(determine_winner('r', 'p'), 'computer')

        # Test ties
        self.assertEqual(determine_winner('r', 'r'), 'tie')
        self.assertEqual(determine_winner('p', 'p'), 'tie')
        self.assertEqual(determine_winner('s', 's'), 'tie')

    def test_stats_update(self):
        """Test that statistics are properly updated."""
        # Test player win
        update_stats(self.stats, 'player')
        self.assertEqual(self.stats['player'], 1)

        # Test computer win
        update_stats(self.stats, 'computer')
        self.assertEqual(self.stats['computer'], 1)

        # Test tie
        update_stats(self.stats, 'tie')
        self.assertEqual(self.stats['tie'], 1)

    @patch('builtins.print')
    def test_display_stats(self, mock_print):
        """Test that statistics are displayed correctly."""
        self.stats = {'player': 2, 'computer': 1, 'tie': 0}
        display_stats(self.stats)
        mock_print.assert_called_once_with(
            "Wins: 2, Losses: 1, Draws: 0")


if __name__ == '__main__':
    unittest.main()
