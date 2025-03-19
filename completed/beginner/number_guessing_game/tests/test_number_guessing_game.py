import unittest
from unittest.mock import patch, MagicMock
from number_guessing_game import (
    generate_secret_number,
    get_user_guess,
    check_guess,
    main
)


class TestNumberGuessingGame(unittest.TestCase):
    def setUp(self):
        """
        Set up test fixtures before each test method.
        """
        # Create a fixed secret number for testing
        self.test_secret_number = 42

        # Create a list of test guesses
        self.test_guesses = {
            'correct': 42,
            'too_high': 50,
            'too_low': 30,
            'invalid': 'not a number',
            'out_of_range': 150
        }

    def test_generate_secret_number(self):
        """
        Test that generate_secret_number returns a number between 1 and 100.
        """
        # Test multiple times to ensure consistency
        for _ in range(100):
            number = generate_secret_number()
            self.assertIsInstance(number, int)
            self.assertGreaterEqual(number, 1)
            self.assertLessEqual(number, 100)

    @patch('builtins.input')
    def test_get_user_guess_valid_input(self, mock_input):
        """
        Test get_user_guess with valid input.
        """
        # Test with a valid number
        mock_input.return_value = "42"
        result = get_user_guess()
        self.assertEqual(result, 42)

    @patch('builtins.input')
    def test_get_user_guess_invalid_input(self, mock_input):
        """
        Test get_user_guess with invalid input.
        """
        # Test with invalid input followed by valid input
        mock_input.side_effect = ["not a number", "150", "42"]
        result = get_user_guess()
        self.assertEqual(result, 42)

    def test_check_guess_correct(self):
        """
        Test check_guess when guess is correct.
        """
        result = check_guess(
            self.test_guesses['correct'], self.test_secret_number)
        self.assertTrue(result)

    def test_check_guess_too_high(self):
        """
        Test check_guess when guess is too high.
        """
        result = check_guess(
            self.test_guesses['too_high'], self.test_secret_number)
        self.assertFalse(result)

    def test_check_guess_too_low(self):
        """
        Test check_guess when guess is too low.
        """
        result = check_guess(
            self.test_guesses['too_low'], self.test_secret_number)
        self.assertFalse(result)

    @patch('builtins.input')
    def test_main_game_flow(self, mock_input):
        """
        Test the main game flow.
        """
        # Mock inputs for a complete game
        mock_input.side_effect = [
            "50",  # too high
            "30",  # too low
            "42",  # correct
            "n"    # don't play again
        ]

        # Mock print to capture output
        with patch('builtins.print') as mock_print:
            main()

            # Verify the game flow
            mock_print.assert_any_call("Your guess is too high")
            mock_print.assert_any_call("Your guess is too low")
            mock_print.assert_any_call(
                "Congratulations! You guessed the correct number!")
            mock_print.assert_any_call("Hope you enjoyed playing goodbye!")


if __name__ == '__main__':
    unittest.main()
