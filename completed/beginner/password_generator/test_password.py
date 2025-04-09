import unittest
from unittest.mock import patch
from password import enough_chars, generate_password, get_input


class TestPasswordGenerator(unittest.TestCase):
    def test_enough_chars(self):
        # Test cases for enough_chars function
        test_cases = [
            # All modifiers, sufficient length
            (4, {"uppercase": "y", "numbers": "y",
             "special characters": "y"}, True),
            # All modifiers, insufficient length
            (3, {"uppercase": "y", "numbers": "y",
             "special characters": "y"}, False),
            # One modifier, sufficient length
            (2, {"uppercase": "y", "numbers": "n",
             "special characters": "n"}, True),
            # One modifier, insufficient length
            (1, {"uppercase": "y", "numbers": "n",
             "special characters": "n"}, False),
            # No modifiers, sufficient length
            (5, {"uppercase": "n", "numbers": "n",
             "special characters": "n"}, True),
        ]

        for num_chars, modifiers, expected in test_cases:
            with self.subTest(num_chars=num_chars, modifiers=modifiers):
                self.assertEqual(enough_chars(num_chars, modifiers), expected)

    def test_generate_password(self):
        # Test password generation with different combinations
        test_cases = [
            (8, {"uppercase": "y", "numbers": "y", "special characters": "y"}),
            (6, {"uppercase": "y", "numbers": "n", "special characters": "n"}),
            (10, {"uppercase": "n", "numbers": "y", "special characters": "n"}),
            (12, {"uppercase": "n", "numbers": "n", "special characters": "y"}),
        ]

        for num_chars, modifiers in test_cases:
            with self.subTest(num_chars=num_chars, modifiers=modifiers):
                password = generate_password(num_chars, modifiers)

                # Check length
                self.assertEqual(len(password), num_chars)

                # Check character types based on modifiers
                if modifiers["uppercase"] == "y":
                    self.assertTrue(any(c.isupper() for c in password))
                if modifiers["numbers"] == "y":
                    self.assertTrue(any(c.isdigit() for c in password))
                if modifiers["special characters"] == "y":
                    self.assertTrue(
                        any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password))

                # Always check for lowercase
                self.assertTrue(any(c.islower() for c in password))

    @patch('builtins.input', side_effect=['y', 'n', 'invalid', 'y'])
    def test_get_input(self, mock_input):
        # Test get_input function with valid and invalid inputs
        result = get_input("uppercase letters")
        self.assertEqual(result, "y")

        result = get_input("numbers")
        self.assertEqual(result, "n")

        # Test with invalid input followed by valid input
        result = get_input("special characters")
        self.assertEqual(result, "y")


if __name__ == '__main__':
    unittest.main()
