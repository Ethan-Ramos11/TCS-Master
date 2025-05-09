from math_quiz import (
    pick_numbers,
    pick_operation,
    valid_division,
    create_question,
    display_question,
    check_answer,
    get_right_answer,
    get_num_range
)
import unittest
from unittest.mock import patch
import random
import sys
import os

# Add the parent directory to the path so we can import the math_quiz module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestMathQuiz(unittest.TestCase):
    def test_get_num_range(self):
        """Test that get_num_range returns correct ranges for each difficulty"""
        # Test easy difficulty
        lower, upper = get_num_range('easy')
        self.assertEqual(lower, 0)
        self.assertEqual(upper, 20)

        # Test medium difficulty
        lower, upper = get_num_range('medium')
        self.assertEqual(lower, 0)
        self.assertEqual(upper, 50)

        # Test hard difficulty
        lower, upper = get_num_range('hard')
        self.assertEqual(lower, 0)
        self.assertEqual(upper, 1000)

        # Test invalid difficulty
        result = get_num_range('invalid')
        self.assertEqual(result, -1)

    def test_pick_numbers(self):
        """Test that pick_numbers returns two numbers within the specified range"""
        test_ranges = [
            (0, 20),   # Easy
            (0, 50),   # Medium
            (0, 1000)  # Hard
        ]

        for lower, upper in test_ranges:
            for _ in range(50):  # Test multiple times due to randomness
                num_one, num_two = pick_numbers(lower, upper)
                self.assertGreaterEqual(num_one, lower)
                self.assertLessEqual(num_one, upper)
                self.assertGreaterEqual(num_two, lower)
                self.assertLessEqual(num_two, upper)

    def test_pick_operation(self):
        """Test that pick_operation returns a valid operation"""
        valid_operations = ['+', '-', '*', '/']
        for _ in range(100):  # Test multiple times due to randomness
            operation = pick_operation()
            self.assertIn(operation, valid_operations)

    def test_valid_division(self):
        """Test the valid_division function"""
        # Test valid division cases
        self.assertTrue(valid_division(10, 2))
        self.assertTrue(valid_division(100, 10))
        self.assertTrue(valid_division(1, 1))

        # Test invalid division cases
        self.assertFalse(valid_division(10, 3))
        self.assertFalse(valid_division(7, 2))
        self.assertFalse(valid_division(1, 2))

    def test_create_question(self):
        """Test that create_question returns valid question components"""
        for _ in range(100):  # Test multiple times due to randomness
            question = create_question()
            self.assertEqual(len(question), 3)
            num_one, num_two, operation = question

            # Check number ranges
            self.assertGreaterEqual(num_one, 1)
            self.assertLessEqual(num_one, 100)
            self.assertGreaterEqual(num_two, 1)
            self.assertLessEqual(num_two, 100)

            # Check operation validity
            self.assertIn(operation, ['+', '-', '*', '/'])

            # If operation is division, check if it's valid
            if operation == '/':
                self.assertTrue(valid_division(num_one, num_two))

    def test_display_question(self):
        """Test the display_question function"""
        test_cases = [
            ([5, 3, '+'], '5 + 3 = ?'),
            ([10, 2, '-'], '10 - 2 = ?'),
            ([4, 6, '*'], '4 * 6 = ?'),
            ([20, 5, '/'], '20 / 5 = ?')
        ]

        for question_info, expected in test_cases:
            self.assertEqual(display_question(question_info), expected)

    def test_check_answer(self):
        """Test the check_answer function"""
        self.assertTrue(check_answer(5, 5))
        self.assertTrue(check_answer(0, 0))
        self.assertTrue(check_answer(-5, -5))
        self.assertFalse(check_answer(5, 4))
        self.assertFalse(check_answer(0, 1))
        self.assertFalse(check_answer(-5, 5))

    def test_get_right_answer(self):
        """Test the get_right_answer function"""
        test_cases = [
            ([5, 3, '+'], 8),
            ([10, 2, '-'], 8),
            ([4, 6, '*'], 24),
            ([20, 5, '/'], 4),
            ([0, 5, '+'], 5),    # Test with zero
            ([10, 0, '+'], 10),  # Test with zero
            ([100, 50, '-'], 50)  # Test with larger numbers
        ]

        for question_info, expected in test_cases:
            self.assertEqual(get_right_answer(question_info), expected)

    @patch('builtins.input')
    def test_main_with_difficulty(self, mock_input):
        """Test the main function with different difficulty levels"""
        # Test easy difficulty
        mock_input.side_effect = ['1', '5']  # Choose easy difficulty, answer 5
        with patch('sys.stdout') as mock_stdout:
            from math_quiz import main
            main()
            output = mock_stdout.getvalue()
            self.assertIn('Easy (numbers 0-20)', output)

        # Test medium difficulty
        # Choose medium difficulty, answer 5
        mock_input.side_effect = ['2', '5']
        with patch('sys.stdout') as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn('Medium (numbers 0-50)', output)

        # Test hard difficulty
        mock_input.side_effect = ['3', '5']  # Choose hard difficulty, answer 5
        with patch('sys.stdout') as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn('Hard (numbers 0-1000)', output)

        # Test invalid input
        # Invalid input, then easy, then answer 5
        mock_input.side_effect = ['4', '1', '5']
        with patch('sys.stdout') as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn('Please enter a number between 1 and 3', output)


if __name__ == '__main__':
    unittest.main()
